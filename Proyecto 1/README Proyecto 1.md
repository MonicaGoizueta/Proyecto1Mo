# Proyecto1Mo


# Objetive

El objetivo de este proyecto es hacer un análisis del mercado de casas en venta en 12 ciudades de 3 Estados de US: Washington, California y Oregón, y algunos índices interesantes de cada ciudad analizada. 

Se estudiarán algunas de las siguientes variables:
 
 - Precio de vivienda
 - Espacio de vivienda
 - Número de habitaciones
 - Número de baños
 - Dirección de la vivienda, Ciudad, Estado, Código Postal
 - Índice de poder adquisitivo
 - Índice de seguridad
 - Índice de sanidad
 - Índice de clima
 - índice costo de vida
 - Índice de relación precio ingresos propiedades
 - Índice de costo de desplazamiento
 - Índice de contaminación
 - Índice de calidad de vida

Se responderán a las siguientes hipótesis:

1) Hipótesis 1: El precio de la casa está directamente relacionado con los metros cuadrados de la misma.

2) Hipótesis 2: Dentro de un Estado, las ciudades con un índice de Contaminación más elevado son las que tienen un índice de Salud más bajo.

3) Hipótesis 3: Las casas tienen el mismo número de cuartos que de cuartos de baño.

4) Hipótesis 4: Existe una relación directa entre la Seguridad y la Calidad de vida de una ciudad. A más seguridad, más calidad de vida.

5) Hipótesis 5: El Estado donde el precio medio por m2 sea mayor, será el Estado que tenga el mayor indice de poder Adquisitivo.
 
 
# Working plan 

1) Hemos partido de un CSV inicial, exportado de Kagle (https://www.kaggle.com/ialjadani/houses-prices-in-selected-area-in-usa), con información de viviendas en venta de muchísimas ciudades de Washington, California y Oregón, en EEUU. 

2) Este CSV inicial lo enriqueceremos con Selenium. Para ello, extrairemos de una página web de índices de calidad de ciudades a nivel mundial (https://es.numbeo.com/calidad-de-vida/iniciar-página), los índices de 11 ciudades de EEUU. 

El motivo por el que vamos a centrar nuestro estudio en únicamente 11 ciudades es para centrar y simplificar el análisis. Además, es importante indicar que las 11 ciudades han sido seleccionadas de manera que nos quedamos y vamos a analizar las 11 ciudades más importantes y relevantes de los Estados de Washington, California y Oregón. 

Sobre la información extraida de Selenium vamos a hacer una limpieza muy grande de formatos para poder obtener un DataFrame limpito y que podamos usar para enriquecer el CSV incial mediante un mergeo.

3) Realizaremos un análisis exploartorio para analizar nuestro DataFrame y localizar posibles errores o aspectos de mejora de cara a sacar posibles insights que nos ayuden a sacar conclusiones.

4) Realizaremos la transformación de nuestro DataFrame, tratando de solventar errores, homogeneizar columnas, solventar valores nulos, etc. Para ello haremos uso de alguna funciones que crearemos.

5) Trabajaremos en la visualización y obtención de conclusiones. Para ello hemos planteado unas hipótesis que resolveremos en último instante.


### Structure of the project files
​
La estructura de este proyecto se compone de las siguientes carpetas:

 1. A folder of notebooks: 
 
     a) 01. CSV inicial_Selenium_Mergeo.ipynb --> Aquí hemos realizado lo siguiente:

- Hemos partido de un CSV inicial que nos hemos descargado de Kaggle, que expone información de casas en venta en ciudades de los Estados de Washington, California y Oregón.
             
- Mediante Selenium, hemos extraido la información de varios índices (de calidad, poder adquisitivo, contaminación, etc.) de las 11 ciudades más importantes (6 de Washington, 4 de California y 1 de Oregón). Esta información que hemos extraido la hemos limpiado para tener un DataFrame limpio para poder hacer el mergeo.

- Hemos mergeado el CSV inicial con el DataFrame que hemos realizado con la información obtenida mediante Selenium.
     
     b) 02. Análisis_Exploratorio.ipynb 
     
     c) 03. Método_de_Transformación.ipynb --> 

- Hemos realizado manipulación de columnas, estandarización del tipado de columnas, eliminación de duplicados y valores nulos, y sacado principales estadísticos generales, y diferenciando por Estado
     
     d) 04. Visualización.ipynb -->
 
 - Hemos realizado las hipótesis mencionadas anteriormente y que resolvemos a lo largo del proyecto.
 
 2. scr folder: carpeta donde tenemos un documento .py (operaciones.py) con las funciones que hemos creado para nuestro proyecto. 

 3. Data: Todos los DataFrames importados y guardados en formato CSV:
 
    a) 01.1 CSV_inicial_houses_USA.csv --> CSV inicial sacado de KAggle

    b) 01.2 Resultado_Selenium_limpio_índices_ciudades_EEUU_ --> CSV que hemos creado con información que hemos extraido mediante Selenium, y que previamente hemos limpiado.
    
    c) 01.3 Datos_enriquecidos_.csv --> Resultado del mergeo del CSV inicial enriquecido con la información extraida mediante Selenium.
    
    d) 02.1 Datos_mergeados_limpieza_inical_.csv --> Haciendo el análisis exploratorio hemos realizado una limpieza mínima, y es el CSV que hemos exportado.
    
    e) 03.1 Datos_limpitos_.csv --> Es el CSV final limpio tras la transformación!!
    
​
# Libraries
​
[sys](https://docs.python.org/3/library/sys.html)

[requests](https://pypi.org/project/requests/2.7.0/)

[pandas](https://pandas.pydata.org/)

[sidetable](https://pypi.org/project/sidetable/)
​
[selenium](https://www.selenium.dev/selenium/docs/api/py/api.html)
​
[re](https://docs.python.org/3/library/re.html)

[folium](https://pypi.org/project/folium/)

[seaborn](https://seaborn.pydata.org/)

[matplotlib](https://matplotlib.org/)

[plotly](https://plotly.com/python/)

[Geopy](https://geopy.readthedocs.io/en/stable/)







