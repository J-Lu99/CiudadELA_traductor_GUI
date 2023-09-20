# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 04:11:58 2023

@author: José Luis
"""

#%% Librerías

from tkinter import*
from tkinter import ttk,font,filedialog
from functools import partial
from ttkbootstrap import Style

import os,csv,sys, pandas as pd

#%% General

general_directory=os.getcwd()+'\\Notas\\'

notes_dict_C={0:'--',147:'D3', 165:'E3',175:'F3',196:'G3',220:'A3',247:'B3', 262:'C4', 294:'D4',
            330:'E4',349:'F4',392:'G4', 440:'A4',494:'B4', 523:'C5', 587:'D5',
            659:'E5',698:'F5', 784:'G5', 880:'A5',988:'B5', 1047:'C6', 1175:'D6',
            1319:'E6', 1568:'G6',1760:'A6', 2093:'C7', 2349:'D7'}


notes_dict_Do={0:'--',147:'Re3', 165:'Mi3',175:'Fa3',196:'Sol3',220:'La3',247:'Si3', 262:'Do4',
               294:'Re4',330:'Mi4',349:'Fa4',392:'Sol4', 440:'La4',494:'Si4', 523:'Do5', 587:'Re5',
                659:'Mi5',698:'Fa5', 784:'Sol5', 880:'La5',988:'Si5', 1047:'Do6', 1175:'Re6',
                1319:'Mi6', 1568:'Sol6',1760:'La6', 2093:'Do7', 2349:'Re7'}

list_do=list(notes_dict_Do.values())
list_c=list(notes_dict_C.values())
latin_to_ardu={list_do[i] : 'NOTE_'+(list_c[i])  for i in range(len(list_do))}
anglo_to_ardu={list_c[i] : 'NOTE_'+(list_c[i])  for i in range(len(list_c))}
anglo_to_latin={list_c[i] : list_do[i]  for i in range(len(list_c))}
latin_to_anglo={list_do[i] : list_c[i]  for i in range(len(list_do))}
#%% Funtions
def traduction(frec,sistem):
    if sistem== 'Anglosajón':
        if frec=='--':
               return '--'
        elif frec=='Adaptar':
            return 'Adaptar'
        else:
            if frec in list_do: return latin_to_anglo[frec] 
            else:
                frec=int(frec)
                if frec in notes_dict_C : return notes_dict_C[frec]
                else: return 'Adaptar'

    if sistem== 'Latino':
        if frec=='--':
            return '--'
        elif frec=='Adaptar':
            return 'Adaptar'
        else:
            if frec in list_c: return anglo_to_latin[frec]
            else:
                frec=int(frec)
                if frec in notes_dict_Do : return notes_dict_Do[frec]
                else: return 'Adaptar'
    
    elif sistem== 'Arduino':
        if frec=='--':
            return 0
        else:
            if frec in list_do: return latin_to_ardu[frec]
            elif frec in list_c: return anglo_to_ardu[frec]
            else: return 0
          

#%%   
def able(But,event=None):
        But['state']=NORMAL 
    
def press(doc,do,event=None):
        if (do.get()== 'Anglosajón' or do.get() == 'Latino'):
            frecs=pd.read_csv(general_directory+doc.get())
            if '#!' in frecs.columns : frecs=frecs.drop([0,1])
            else:frecs=pd.read_csv(general_directory+doc.get(),names=['#!'])
            
        else: frecs=pd.read_csv(general_directory+doc.get(),names=['#!'])
             
        notes=frecs['#!'].apply(lambda x : traduction (x,do.get())).tolist()
        notes.append(0)
        if not os.path.isdir(general_directory+'Traducidos\\'):
             os.mkdir(general_directory+'Traducidos\\')
             
        if do.get()=='Arduino':
            with open(general_directory+'Traducidos\\'+do.get()+'_'+doc.get()[:-4]+'.txt','w') as f:
                f.write(",".join(str(note) for note in notes))

        else:
            with open(general_directory+'Traducidos\\'+do.get()+'_'+doc.get(),'w') as f:
                write=csv.writer(f)
                for note in notes : 
                    write.writerow([note])
        doc.set('')     
       
def blur(frame,Event):
    if Event.widget==frame:
        frame.focus()
        
def return_focus(wid1,wid2,entry_doc,But,Event):    
    wid2.focus()

 
def des_wid(inter,wid,label_done,Event=None):
    if 'label_done' in globals(): 
        inter.destroy(wid)

class splash(object):
    def __init__(self,widget,text):
        self.widget=widget
        self.text=text
        self.id=None
        self.tw=None
        
    def hidesign(self):
            tw=self.tw
            self.tw=None
            if tw: tw.destroy()   
#%% Tooltip class
class tooltip(splash):
    """Create a tooltip for a given widget"""
    def __init__(self,widget,text):
        super().__init__(widget,text)
        self.waittime=500
        self.wraplength=160
        self.widget.bind('<Enter>',self.enter)
        self.widget.bind('<Leave>',self.leave)
        self.widget.bind('<ButtonPress>', self.leave)

    def showtip(self,event=None):
            x=y=0
            x,y,cx,cy=self.widget.bbox('insert')
            x +=self.widget.winfo_rootx() +25
            y +=self.widget.winfo_rooty() +20
            cx+=40
            cy+=40
            #create top lavel
            self.tw=Toplevel(self.widget)
            self.tw.attributes('-alpha',0.85)
            #remove title bar
            self.tw.wm_overrideredirect(True)
            self.tw.wm_geometry("+%d+%d" % (x,y))
            label= Label(self.tw,text=self.text, justify='left',background='#daeeef',font=font.Font(family="Lato",size=11),
                         relief='flat',borderwidth=1,wraplength=self.wraplength)
            label.pack(ipadx=1)
        
    def unschedule(self):
            id=self.id
            self.id=None
            if id:
                self.widget.after_cancel(id)
    def schedule(self):
            self.unschedule()
            self.id=self.widget.after(self.waittime,self.showtip)
    def enter(self,event=None):
            self.schedule()
    def leave(self, event=None):
            self.unschedule()
            self.hidesign()

#%% Splash sign class
class interactive_widget(splash):
    """Create a sign for a given widget,
        and asign a function to it"""   
    def __init__(self,widget,text,entry1,entry2,frame,width_frame,height_frame,function):
        super().__init__(widget,text)
        self.widget.bind('<ButtonPress>',self.enter)
        self.widget.bind('<Return>',self.enter)
        self.waittime=800
        self.wraplength=100
        self.width_frame=width_frame
        self.height_frame=height_frame
        self.width=200
        self.height=100
        self.entry1=entry1
        self.entry2=entry2
        self.frame=frame
        self.t=text
        self.function=function
        
    
        
    def showsign(self,event=None):
            x=y=0

            x=self.frame.winfo_rootx() + (self.width_frame/2)-(self.width/2)
            y=self.frame.winfo_rooty() + (self.height_frame/2)-(self.height/2)
            
            #create top lavel
            self.tw=Toplevel(self.widget)
            self.tw.attributes('-alpha',0.9)
            self.tw.configure(background='#a7c6c1')
            #remove title bar
            self.tw.wm_overrideredirect(True)
            self.tw.wm_geometry("%dx%d+%d+%d" % (self.width,self.height,x,y))
            
            label= ttk.Label(self.tw,text=self.t, justify='left',background='#a7c6c1',
                         relief='flat',borderwidth=1,wraplength=self.wraplength,font=font.Font(family="Lato",size=16),foreground='white')

            label.grid(row=1,column=1,padx=50,pady=40,sticky='w')
            

    def enter(self,event=None):
            try:
                self.function(self.entry1,self.entry2)
            except:
                self.t='    Error'
            finally:
                self.showsign()
                self.leave()
                self.t=self.text
    def leave(self, event=None):
            self.id=self.widget.after(self.waittime,self.hidesign)

         
#%% GUI

def main():
    inter=Tk()
    doc=StringVar()
    do=StringVar()
    inter.title(string='Traductor de notas')


    
    #Responsive design
    frame=Frame(inter)
    frame.pack()
    
    win_width=575
    win_height=220
    screen_widht=inter.winfo_screenwidth()
    screen_height=inter.winfo_screenheight()
    x=(screen_widht/2)-(win_width/2)
    y=(screen_height/2)-(win_height/2)
    inter.geometry("%dx%d+%d+%d"%(win_width,win_height,x,y))
    
    
    
    #Ícono
    inter.iconbitmap(sys.executable)
    
    #Estilos
    #style= ttk.Style()

    style=Style(theme='arduino')
    

    #Intro
    
    label_intro1=ttk.Label(frame,text="*El documento a traducir debe encontrarse en la carpeta 'Notas', estando esta última",
                          font=font.Font(family="Lato",size=11))
    label_intro1.grid(row=2,column=0,sticky='W', pady=0,padx=11,columnspan=2)
    label_intro2=ttk.Label(frame,text="localizada junto al ejecutable. También en 'Notas' se guardará el nuevo documento.",
                          font=font.Font(family="Lato",size=11))
    label_intro2.grid(row=3,column=0,sticky='W', pady=1,padx=11,columnspan=2)
    
    label_space=ttk.Label(frame,text="",font=font.Font(family="Lato",size=4))
    label_space.grid(row=1,column=0,sticky='W', pady=0,padx=5,columnspan=2)
    label_space2=ttk.Label(frame,text="")
    label_space2.grid(row=4,column=0,sticky='W', pady=0,padx=5,columnspan=2)
    

    #Casillas
    
    entry_do=ttk.Spinbox(frame,textvariable=do,values=['Latino','Anglosajón','Arduino'],font=font.Font(family="Lato"),width=19,state='readonly', wrap=True)
    entry_do.grid(row=9,column=1, sticky='e', pady=5,padx=35)
    label_do=ttk.Label(frame,text="Seleccione el cifrado deseado",font=font.Font(family="Lato",size=13))
    label_do.grid(row=9,column=0, sticky='e', pady=5,padx=15)
    entry_do.focus_get()
    try:
        files=[file for file in os.listdir(general_directory) if file !='Traducidos']
    except FileNotFoundError:
        os.mkdir('Notas')
        files=[file for file in os.listdir(general_directory) if file !='Traducidos']
         
    entry_doc=ttk.Combobox(frame,values=files,textvariable=doc,font=font.Font(family="Lato"),width=20,state='readonly')
    entry_doc.grid(row=10,column=1, sticky='e', pady=5,padx=35)
    label_doc=ttk.Label(frame,text="Seleccione un documento",font=font.Font(family="Lato",size=13))
    label_doc.grid(row=10,column=0,sticky='e', pady=5,padx=15)
    
    #Button
    
    But=Button (frame, text="Traducir",state=DISABLED,font=font.Font(family="Lato",size=15),foreground='white',relief='sunken')
    But.grid(row=12,column=1, sticky='e', pady=5,padx=35)
    
   # But.bind("<Return>",partial(press,doc,do,entry_do,frame))
    entry_doc.bind("<<ComboboxSelected>>",partial(able,But))
    
    interactive_but=interactive_widget(But,'Traducido',doc,do,frame,win_width,win_height,press)
           
    #Focus
    frame.bind("<1>",partial(blur,frame))
    entry_do.focus()
    scroll=[entry_do,entry_doc,But]
    scroll_D_U=[entry_doc,But,entry_do]
    for wid in range(len(scroll[:2])): scroll[wid].bind("<Return>",partial(return_focus,scroll[wid],scroll[wid+1],entry_doc,But))
    #for wid in range(len(scroll[:2])):scroll_D_U[wid].bind("<Down>",partial(return_focus,scroll_D_U[wid],scroll_D_U[wid+1],entry_doc,But))
    #for wid in range(len(scroll[::-1])): scroll_D_U[wid].bind("<Up>",partial(return_focus,scroll_D_U[wid],scroll_D_U[wid-1],entry_doc,But))

    #Tooltips
    dotip=Label(frame, text="?",relief=FLAT,font=font.Font(family="Lato",size=10))
    dotip.grid(row=9,column=1, sticky='e', pady=5,padx=10)
    dotip_create=tooltip(dotip,\
                         "El cifrado latino es "
                         'la conocida notación: '
                         'do,re,mi,fa,sol,la,si.            '
                         'El cifrado anglosajón '
                         'correspondiente es: '
                         'C,D,E,F,G,A,B.'
                         '                                   '
                         "Arduino es el languaje " 
                         'de programación con que '
                         'está hecho el theremin,'
                         'y por lo tanto es la '
                         'notación que él reconoce. '
                         '(solo para uso avanzado)')

    doctip=Label(frame, text="?",relief=FLAT,font=font.Font(family="Lato",size=10))
    doctip.grid(row=10,column=1, sticky='e', pady=5,padx=10)
    doctip_create=tooltip(doctip,\
                         "Solo se muestran los "
                         "documentos localizados "
                         "en la carpeta 'Notas'.")
    inter.mainloop()


#%% Play

if __name__=="__main__":
    
    main()     



# %%

