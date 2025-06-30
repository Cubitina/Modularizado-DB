Aplicación para la Administración de Productos de un negocio

Esta aplicación busca ser una herramienta para poder administrar de forma eficiente los productos de un pequeño negocio de manera simple y amigable. 

La app:
Primeros Pasos:
Antes de comenzar a utilizar nuestra aplicación deberá clonar el repositorio de https://github.com/Cubitina/Modularizado-DB en su computadora.
La primera vez que quiera utilizar el programa deberá ejecutar el archivo “instalar.py” en su terminal. 
![Instalación de la aplicación](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/01_instalacion.png)
Cuando le consulte si desea instalarla, escriba en la terminal “si”. Esto permitirá que se instale la base de datos con la que trabajará la aplicación. Una vez realizada esta operación, la misma aplicación los redireccionará al menú principal.
![Instalación de base de datos](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/02_instalacion.png)
Cabe destacar que este procedimiento se debe realizar una sola vez. Cuando ya tiene la base de datos instalada, para iniciar el programa deberá ejecutar el archivo “main.py”. Este los llevará directamente el menú principal.

Menú principal:
![Menú principal de la app](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/03_menu_principal.png)
Esta es la puerta de entrada de la aplicación. En él encontrará 7 opciones:
1)	Opción para agregar productos.
2)	Visualización de datos.
3)	Búsqueda de productos.
4)	Modificación de un producto.
5)	Eliminación de un producto.
6)	Esta opción le permite limpiar la pantalla de la consola para una mejor visualización.
7)	Opción para salir de la aplicación.

Para acceder alguna de las opciones solamente tiene que digitar el número deseado. Si ingresa letras o simplemente presiona Enter, la app le mostrará un mensaje de error y le pedirá que ingrese el número indicado.

Función Nº1 – Agregar un producto:
En esta opción se le pedirá que ingrese el nombre del producto, tipo, el valor y su stock. La app está configurada para que el nombre del producto sea único a fin de evitar duplicación de entradas. Asimismo, si usted no ingresa un dato o valor, la app le mostrará un mensaje de error y le pedirá que vuelva a ingresar la información. En los casos que deba ingresar datos numéricos como en precio y stock, si ingresa un texto la app le mostrará un mensaje de error y le pedirá que vuelva ingresar el dato pedido. En caso de que usted quiera salir de la carga del producto, en cualquiera de las instancias solicitadas podrá ingresar la palabra “fin” y la app lo llevará al menú principal nuevamente.
Una vez realizada la carga del producto, la app le muestra un mensaje de registro exitoso y luego le muestra todos los detalles.
![Pantalla de registro de producto](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/04_agregar_prod.png)
En caso de que usted quiera salir de la carga del producto, en cualquiera de las instancias solicitadas podrá ingresar la palabra “fin”. En caso de haber realizado un registro de producto, le mostrará un listado general de sus productos y lo redireccionará hacia el menú principal. Si no realizó ningún registro, simplemente regresa al menú principal.

Función Nº2 – Visualización de datos:
Una vez cargados sus productos, en la función Nº2 del menú principal podrá visualizar diferentes listados de sus productos de acuerdo con las necesidades, como ser por orden de precio ascendente o por orden alfabético. 
![Menú de la Función Nº2 - Visualizaciones](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/05_funcion_2.png)
Cuando ingresa a esta opción, tendrá otro menú de opciones:
1)	Listado completo de productos.
2)	Listado de productos por precio ascendente.
3)	Listado de productos por precio descendente.
4)	Listado de productos por orden alfabéticos ascendente.
5)	Listado de productos por orden alfabéticos descendente.
6)	Listado de productos bajos en stock.
7)	Gráfico de torta por tipo de productos en su listado.
8)	Gráfico de barras de productos y precios.
9)	Gráfico de barras de productos y stock.
10)	Regresar al menú principal.

Dentro de las opciones tiene la de obtener un listado de productos que poseen 5 o menos unidades de stock, a fin de poder alertar sobre la necesidad de un restock. Si bien este listado se puede solicitar, cuando se solicita un listado general, esos productos bajos en stock se encontrarán resaltados con un fondo amarillo para una visualización destacada. 
![Visualización de alerta de bajo stock](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/06_Alerta_bajo_stock.png)

Asimismo, tiene la posibilidad de obtener un gráfico de torta para ver qué tipo de productos tiene en su listado, gráficos de barras con referencia al precio y al stock de los productos.
![Ejemplo de gráfico de barras](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/07_visualizacion_grafico.png)
Como en el menú principal, debe ingresar el número deseado, sino le mostrará un mensaje de error.

Función Nº3 – Buscar productos:
Cuando quiera buscar algún producto podrá hacerlo ya sea por nombre, categoría, precio y código. En la búsqueda podrá ingresar texto o números.
Si el buscador no encuentra ningún producto con el parámetro dado, muestra un mensaje. En caso de encontrar, muestra el producto con todos los datos.
En caso de que desee salir del buscador, simplemente deberá presionar Enter y la app lo regresará al menú principal.
![Búsqueda de productos](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/08_busqueda_prod.png)

Función Nº4 – Modificar un producto:
En caso de querer modificar un producto podrá hacerlo para ‘nombre’, ‘categoría’, ‘precio’ y ‘stock’.
Cuando ingresa en esta opción, el programa le pedirá que busque el producto a modificar a fin de que pueda obtener el número de código que lo identifica. La modalidad de búsqueda es igual a la de la Función Nº3. Una vez que ha encontrado el producto deseado, simplemente presione Enter para seguir con el procedimiento.
![Modificar productos](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/09_mod_prod_01.png)
Luego le pedirá que ingrese el ‘cógido’ del producto a modificar. Esto es importante ya que si se equivoca de código modificará otro producto.
![Modificar productos](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/10_mod_prod_02.png)
Una vez ingresado el código aparece un menú de opciones para que seleccione que tipo de modifcación quiere realizar:
1)	Modificar nombre.
2)	Modificar tipo de producto.
3)	Modificar precio.
4)	Modificar stock.
5)	Regresar al menú de inicio.
Se selecciona la opción deseada, la app le pedirá que ingrese el nuevo valor y luego realizará la modificación mostrándole en pantalla el resultado. Luego lo redireccionará nuevamente al menú de inicio.
![Modificar productos](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/11_mod_prod_03.png)

Función Nº5 – Eliminar producto:
El procedimiento para eliminar un producto es similar a la de modificar. Primero se le pedirá que busque el producto a fin de conocer el número de código identificatorio. Una vez identificado, presione Enter para continuar con el procedimiento.
El programa le pedirá que ingrese el número de código del producto deseado. Una vez ingresado, el sistema muestra un mensaje de confirmación de eliminación ya que una vez ejecutada la acción no podrá ser revertida. Para eliminarlo deberá escribir ‘si’, en caso contrario, se cancela la eliminación, muestra un mensaje de cancelación y el programa regresa al menú principal.
![Cancelar eliminar producto](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/12_eli_prod_01.png)
Cuando escribe ‘si’ para eliminar el producto, una vez ejecutada la acción, la app le mostrará un mensaje confirmando la acción. Luego imprimirá el listado completo de productos y lo redireccionará al menú principal.
![Producto eliminado](https://github.com/Cubitina/Modularizado-DB/blob/main/imagenes/13_eli_prod_02.png)

Función Nº6 -  Limpiar la pantalla de la consola:
Esta opción le permitirá tener una mejor visual en la consola cuando ya se encuentra con mucha información.

Función Nº7 – Salir del programa:
Esta opción le permitirá salir de la app. Una vez seleccionada, el mensaje le mostrará un mensaje de despedida.


El proceso:
Esta app fue creada como proyecto del Trabajo Final Integrador del Curso “Introducción a la Programación con Python” en el marco de Talento Tech, Gobierno de la Ciudad de Buenos Aires, durante el primer cuatrimestre del ciclo lectivo 2025.
Este trabajo representa la culminación de todo lo aprendido en el curso y un poco más ya tengo una mente curiosa y muchos deseos de aprender. Esto llevó a que fueran incluidas funcionalidades que no se han visto en el curso. Por ejemplo, en la opción de búsqueda de un producto, se pedía que solamente sea por nombre y en mi proyecto es posible hacerlo para código, nombre, categoría, precio. Asimismo, en las visualizaciones, se incluyeron otras opciones como orden por precio o alfabético y las visualizaciones de gráficos que implicaron indagar sobre recursos como “Pandas” y “Seaborn”.

Autora:
@Cubitina


