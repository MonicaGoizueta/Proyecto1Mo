# Proyecto2Mo


### Objective

El objetivo de este proyecto es crear un Dashboard ofreciendo visibilidad sobre algunos índices que resultan de real interés en algunas ciudades de los Estados en análisis, y la posible afectación en el precio/m2 de todas las casas en venta de estas ciudades analizadas.


### Alcance

Los Estados en análisis son: Washington, California y Oregón.
Las 11 Ciudades analizadas son: 

    - Del Estado Washington: 
        Bellevue, Olympia, Redmond, Seattle, Tacoma, Vancouver
        
    - Del Estado California:
        Anaheim, Irvine, Long Beach, Pasadena
    
    - Del Estado Oregón:
        Portland


Se tiene en consideración un análisis del mercado de casas en venta en 11 ciudades de 3 Estados de US y algunos índices interesantes de cada ciudad analizada. 

Se estudiarán algunas de las siguientes variables:
 
 - Precio/m2 de vivienda
 - Ciudad
 - Estado
 - Código Postal
 - Índice de poder adquisitivo
 - Índice de seguridad
 - Índice de sanidad
 - Índice de contaminación
 - Índice de calidad de vida


### Working Plan

1) Hemos partido de un CSV que limpiamos en el Primer Proyecto de Ironhack y que hemos decidido aprovechar por el gran partido que le podíamos sacar. El CSV que hemos utilizado fue primero exportado de Kagle con la información de las viviendas en venta de varias ciudades de 3 Estados de EEUU (https://www.kaggle.com/ialjadani/houses-prices-in-selected-area-in-usa), y enriqueciendolo con Selenium, para introducir índices de las ciudades cuyo análisis queríamos realizar. 

2) El motivo por el que quisimos centrar nuestro estudio en únicamente 11 ciudades es para centrar y simplificar el análisis. Además, es importante indicar que las 11 ciudades han sido seleccionadas de manera que nos quedamos y vamos a analizar las 11 ciudades más importantes y relevantes de los Estados de Washington, California y Oregón. 

3) Mediante Python hemos creado e iniciado las clases. Además hemos definido las variables que tenemos en nuestro CSV que hemos utilizado, y creado tablas y conexiones entre ellas en SQL.

4) Posteriormente hemos insertado los datos de nuestro CSV.

5) Por último hemos creado el Dashboard sacando algunas conclusiones muy interesantes.


### Structure of the project files


La estructura de este proyecto se compone de las siguientes carpetas:
(los notebooks no mencionados a condinuación forman parte del primer proyecto de limpieza de datos)

 1. Data
 
    a) 03.1 Datos_limpitos_.csv 
    
Es el CSV que hemos utilizado para el Dashboard. Surge de una transfromación y limpieza que realizamos en el primer proyecto y que hemos utilizado para el segundo proyecto de Ironhack.
    

 2. A folder of notebooks: 
 
     a) 05. Data-To-SQL.ipynb

En este notebook, hemos partido de un CSV que limpiamos en el Priyecto inicial de Ironhack.Con este CSV, lo que hemos realizado es crear e iniciar las clases. Además hemos definido las variables que tenemos en nuestro CSV que hemos utilizado, y creado tablas y conexiones entre ellas.

También, hemos insertado los datos de nuestras columnas del CSV en las tablas que hemos creado en Workbench SQL, creando así un EER Diagram.

 3. Images
 
    a) EER Diagram
    
Es el diagram que hemos creado en SQL mediante queries lanzadas en python. Muestra todos los datos de nuestro CSV mediante tablas conectadas entre sí.

Para ello mostramos un pantallazo de como se verían las conexiones

 4. Tableau
 
    a) Dashboard_CasasEEUU_VF_
 
Hemos realizado un Dashboard de doble pestaña que se muestra en la siguiente URL: https://public.tableau.com/app/profile/monica2410/viz/Dashboard_CasasEEUU_VF_/Dashboard1?publish=yes

En primer lugar mostramos el precio medio por metro cuadrado de la vivienda por Ciudad / Estado, además de la media de los índices de los Estados analizados. 
 
En segundo lugar, ampliamos el detalle, mostrando el precio medio por metro cuadrado de la vivienda por código postal, donde se ve una clara diferencia de las zonas donde es más cara la vivienda por metro cuadrado. Además mostramos en detalle la media de los índices de los Estados analizados por código postal. Esto permite una mejor visión de las grandes o pequeñas diferencias dentro de un mismo Estado y una misma ciudad.

Para ambas pestañas del Dashboard, el colorido dentro de las gráficas de barras muestra un azul más intenso para las ciudads/ códigos postales donde el precio/m2 es superio.
Por otro lado, para los mapas, el colorido difiere. Mostrando color verde para los Estados / códigos postales con mayor índice, y rojo para los de menor índice.
 