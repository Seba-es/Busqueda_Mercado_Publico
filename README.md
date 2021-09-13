# Búsqueda de Productos en Mercado Público
## Este es un proyecto de prueba de automatización con Python, usando Selenium.
## Descripción del Proyecto:
### A partir de un listado de productos contenidos en un archivo excel, este script busca cada uno de los productos en la Tienda de Mercado Público, tomando en cuenta las distintas categorías existentes.
### El archivo Requerimiento_Productos.xlsx corresponde al Excel en donde estan los productos por buscar.
### Allí se pueden encontrar distintas categorías como:
#### ID: Corresponde al número de identificación del producto
#### Unidad: Nombre del departamento que realiza el requerimiento
#### Nombre del Producto: Conjunto de palabras que individualiza al producto
#### Dirección de Despacho: Lugar de entrega del producto
#### Receptor del Producto: Nombre de quién recibiría el producto
#### Convenio Marco: Corresponde al tipo de Convenio Marco, por ejemplo: Aseo, Software, Artículos de Escritorio, entre otros.
#### Link: Url del producto
### Todo la información contenida en el Excel esta puesta con la finalidad de acercarse a la realidad.
### El archivo busqueda_mpublico.py corresponde al script que realiza la búsqueda de los productos.
#### Para ejecutar el archivo busqueda_mpublico.py se necesita tener instalado un Intérprete de Python y además instalar librerias como Selenium y Pandas.
