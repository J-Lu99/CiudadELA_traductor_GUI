# CiudadELA_traductor_GUI

![Semantic description of image](/source/images/Icon.jpg)*Ícono del programa*

El _theremin_ es un instrumento musical muy curioso, pues no necesita de contacto directo, sino que detecta la posición de las manos, y según esta suena una frecuencia particular, a un volumen determinado. Creamos uno propio que, gracias a un trabajo enfocado en ello, fue la vía por la que Irene, Lázaro, Joan y Tamara (quienes son pacientes de ELA) convirtieron sus movimientos en melodías, y usándolo también se registraro estas, se tradujeran (de eso trata este repositorioa) e incluso se reprodujeron en el estudio de grabación. Todo este proceso ha sido parte del proyecto CiudadELA Camp, al que se han unido un grupo de músicos cubanos para, usando estas melodías registradas, crear canciones que serán vendidas como NFT para apoyar a los pacientes con esta enfermedad.

Puedes saprender más sobre este instrumento, qué es CiudadELA, y cómo se usó el _theremin_ en ella acá: 
<https://github.com/Nativos-B612/CiudadELA_theremin>

Aunque podemos registrar las notas que produce el _theremin_, y guardarlas en un documento, estas se verán como números, las frecuencias de distintas ondas, pues cada nota musical es eso, una onda. Estos números no son viables para que los músicos trabajen, a no ser que usen una tabla para traducirlos a la nota musical correspondiente, nota por nota, y esto puede ser bastante exasperante cuando tenemos una gran cantidad de datos.

El programa sobre el que les comentaremos surge de la necesidad de resolver ese problema, de una forma efectiva y rápida, pero que además sea intuitiva para usuarios no especializados. Sin embargo, este programa puede ser útil para músicos y programadores en general, para traducir cifrados musicales, traucir la salida de código de arduino a notas musicales, o viceversa, para hacer un reproductor.

La relación en nuestro caso se puede ver desde el inicio en el ícono, el theremin detecta los objetos lanzando ondas y recibiendo el eco, como si fuese un murciélago, de ahí que estén presentes las ondas. El porqué de la nota musical es evidente, y el color es cercano al utilizado en el logo de arduino, un lenguaje que fue utilizado para programar el _theremin_.

----

## Funcionamiento

El programa está disponible como un ejecutable, un .exe, solo tendremos que dar doble click, y sin necesidad de que veamos todo el código que lo construye, podremos interactuar con la siguiente interfaz gráfica:

![Semantic description of image](/source/images/GUI.png)

Bastará con introducir el documento que queremos traducir, y a qué cifrado queremos traducirlo.

![Semantic description of image](/source/images/Select.png)*El documento mostrado es un ejemplo, no pertenece a ningún paciente.*

¿Pero qué es esto de 'cifrado'? Si colocamos el puntero del mouse en los signos de interrogación aparecerá información necesaria en caso de que no estemos familiarizados, esto es conocido como tooltip:

![Semantic description of image](/source/images/Tooltip1.png)*Se muestra un comentario sobre cada posible opción para el cifrado*

Si te preguntas sobre la opción de traducir a arduino, es necesaria para que, luego de haberse registrado las notas, o que los músicos seleccionen algunas notas específicas, podamos volver a llevar todo eso a la notación específica que entiende el código del theremin, y esa melodía pueda ser guardada dentro de él. De esta forma podrá reproducirla, fielmente, de manera automática. Esto podemos usarlo en el proceso musical, pero también es una funcionalidad que puede ser necesaria para otros programadores que quieran incluir música en su código, de esta manera buscan las notas musicales en su notación normal, y las traducen rápidamente con el programa, listas para usarse. 

También pudiésemos no entender por qué solo se muestran algunos documentos, y aunque esto está relacionado al texto inicial del programa, tenemos otro tooltip:

![Semantic description of image](/source/images/Tooltip2.png)*Agrandar imagen en caso necesario.*

Una vez seleccionado el cifrado y el documento, damos _click_, o _enter_ en 'Traducir', y tomará menos de un segundo, incluso si son miles de notas. ¿Nos ahorramos tiempo eh?

![Semantic description of image](/source/images/Sign.png)

Vale la pena notar que también podremos traducir un documento en cifrado anglosajón al latino, y viceversa. Esta es otra cualidad que supera en sí los propósitos de este proyecto, es útil en general para cualquier persona haciendo música. 

La forma original de nuestro programa es esta:

![Semantic description of image](/source/images/Code.png)*La barra colocada a la derecha es una vista en miniatura de todo el código.*

Unas 300 líneas de código, de las cuáles 2/3 están destinadas a crear la interfaz gráfica con la que trabaja el usuario, y dar todo tipo de efectos, por ejemplo: su paleta de colores; al presionar enter ir a la siguiente casilla, deseleccionar todas las casillas al dar click en el fondo; eliminar el cartel de 'traducido' luego de un tiempo para que sigamos trabajando; dejar colocado el cifrado en el que estamos trabajando cuando vayamos a introducir un próximo documento; hacer que los tooltips se eliminen al mover el mouse del signo de interrogación, etc. Todo esto puede parecer lo normal, pero esa es la idea, que el programa recree la experiencia normal de un usuario. Este código lo puedes encontrar en _Softwares_.

En todo el proceso para determinar qué era necesario programar en pos de una experiencia de usuario óptima, así como en la creación de la paleta de colores usada y el propio ícono, trabajó la diseñadora [Maria Paula Lista Jorge][identifier].

El programa en caso de querer copiarlo cuenta con un instalador, que solo pesa 200 MB, y es muy sencillo de seguir, a la vez que rápido. Lo podrás solicitar al equipo de Nativos B 6 12.

<!-- Identifiers-->
[identifier]: https://www.instagram.com/maripepa_44/



