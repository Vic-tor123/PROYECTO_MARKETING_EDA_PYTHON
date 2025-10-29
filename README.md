# PROYECTO MARKETING BANCARIO (EDA)
<img src="imagenes/portada.png" alt="Portada" width="500">



Análisis exploratorio de datos de campañas de marketing directo de un banco Portugués realizadas mediante llamadas telefónicas para vender depósitos a plazo.

## Descripción del Proyecto
Este proyecto analiza 43,000 registros de contactos telefónicos realizados entre 2015 y 2019. El objetivo es identificar qué características influyen en que un cliente acepte o rechace el producto bancario ofrecido.
El análisis incluye exploración de variables demográficas, de campaña y económicas, detección de correlaciones y outliers.

## Dataset
El dataset contiene información de 43,000 clientes con una tasa de conversión del 11.27%. Las variables principales incluyen:
* Variables demográficas: edad, profesión, estado civil, educación, ingresos, número de hijos.
* Variables de campaña: duración de llamada, número de contactos, días desde último contacto, resultado de campañas anteriores, tipo de contacto.
* Variables económicas: tasa de variación del empleo, índice de precios, índice de confianza del consumidor, euribor, número de empleados.
Variable objetivo: aceptación del producto (sí/no).

## Estructura del Repositorio
```
marketing-campaign-analysis/
│
├── Datos.Originales/
│   ├── bank-aditional.csv
│   └──customer-details.xlsx 
│                              
├── Datos/
│   ├── df_data_limpios.csv
│   ├── df_data_no_nulos.csv                  
│   └── df_data_unificada.csv
│
├── notebooks/
│   ├── 01.Unificacion_datos.ipynb
│   ├── 02.Eda_preliminar.ipynb
│   ├── 03.Limpieza.ipynb
│   ├── 04.Nulos.ipynb
│   └── 05.Analisis.ipynb
│
├── src/
│   ├── sp_eda.py
│   ├── sp_limpieza.py
│   ├── sp_nulos.py
│   └── sp.visualizaciones_eda.py
│
├──imagenes/
│   └── portada.png
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Herramientas
* Python 3.x 

* Jupyter Notebook / JupyterLab 

* Visual Studio Code

* Git / GitHub

* Pandas 

* NumPy 

* Matplotlib 

* Seaborn 
* Plotly 

* Scikit-learn 

## Estructura de datos

* **age:** La edad del cliente.
* **job:** La ocupación o profesión del cliente.
* **marital:** El estado civil del cliente.
* **education:** El nivel educativo del cliente.
* **default:** Indica si el cliente tiene algún historial de incumplimiento de  pagos (1: Sí, 0: No).
* **housing:** Indica si el cliente tiene un préstamo hipotecario (1: Sí, 0: No).
* **loan:** Indica si el cliente tiene algún otro tipo de préstamo (1: Sí, 0: No).
* **contact:** El método de contacto utilizado para comunicarse con el cliente.
* **duration:** La duración en segundos de la última interacción con el cliente.
* **campaign:** El número de contactos realizados durante esta campaña para este cliente.
* **pdays:** Número de días que han pasado desde la última vez que se contactó con el cliente durante esta campaña.
* **previous:** Número de veces que se ha contactado con el cliente antes de esta campaña.
* **poutcome:** Resultado de la campaña de marketing anterior.
* **emp.var.rate:** La tasa de variación del empleo.
* **cons.price.idx:** El índice de precios al consumidor.
* **cons.conf.idx:** El índice de confianza del consumidor.
* **euribor3m:** La tasa de interés de referencia a tres meses.
* **y:** Indica si el cliente ha suscrito un producto o servicio (Sí/No).
* **date:** La fecha en la que se realizó la interacción con el cliente.
* **contact_month:** Mes en el que se realizó la interacción con el cliente durante la campaña de marketing.
* **ontact_year:** Año en el que se realizó la interacción con el cliente durante la campaña de marketing.
* **id_:** Un identificador único para cada registro en el dataset.
* **Income:** Representa el ingreso anual del cliente en términos monetarios.
* **Kidhome:** Indica el número de niños en el hogar del cliente.
* **Teenhome:** Indica el número de adolescentes en el hogar del cliente.
* **Dt_Customer:** Representa la fecha en que el cliente se convirtió en cliente de la empresa.
* **NumWebVisitsMonth:** Indica la cantidad de visitas mensuales del cliente al sitio web de la empresa.
* **ID:** Identificador único del cliente.
* **latitude:** Coordernadas geograficas relacionadas con la ubicacion del cliente
* **longitude:** Coordernadas geograficas relacionadas con la ubicacion del cliente

## Desarrollo del proyecto


* Exploración inicial: carga de datos y unificación de hojas de cálculo en un único archivo .xlsx. Posterior fusión de los archivos .csv y .xlsx en un solo archivo .csv.

* Inicio del EDA: identificación general de los tipos de datos por columna, detección de datos a limpiar, análisis de valores faltantes y elaboración de estadísticas descriptivas.

* Creación de la carpeta SRC: contiene los archivos de soporte .py, donde se alojan las distintas funciones creadas para ser llamadas desde los correspondientes notebooks de Jupyter.

* Limpieza de datos: homogeneización de la estructura de los datos (espacios, comas, mayúsculas, etc.) y eliminación de columnas innecesarias.

* Gestión de nulos: tratamiento de columnas categóricas y numéricas, visualización y cálculo de outliers, imputación de valores faltantes mediante IterativeImputer y KNNImputer.

* Análisis: estudio de distribuciones y frecuencias, y detección de outliers en variables numéricas y categóricas mediante histogramas, boxplots y cálculos estadísticos. Elaboración de la matriz de correlación entre variables numéricas, mapa de ubicación de clientes, gráfico de líneas para analizar la evolución de los productos ofertados a lo largo del tiempo y gráficos de dispersión para estudiar correlaciones entre variables.

## Conclusiones

### Perfil del Cliente

El cliente típico tiene 40 años, está casado y trabaja como administrativo, obrero o técnico. Más de la mitad tiene educación superior. La mayoría nunca había sido contactada en campañas anteriores.

### Efectividad de Campaña
La tasa de conversión es del 11.27%. Las llamadas típicas duran entre 2 y 5 minutos. Se realizan de media 2 o 3 intentos de contacto por cliente. El canal preferido es el teléfono móvil con un 63.71% de los contactos.

### Multicolinealidad Detectada
Las cuatro variables económicas están muy correlacionadas entre sí (correlaciones entre 0.77 y 0.91). Esto significa que miden básicamente lo mismo: el estado de la economía. Para posteriores análisis se podría prescindir de algunas de ellas.

### Desequilibrio en los resultados
El dataset tiene 88.73% de rechazos frente a 11.27% de aceptaciones. A la hora de analizar los datos se tiene menos información sobre la gente que aceptó el producto.

### Outliers Informativos
Se detectaron outliers en varias variables pero la mayoría son casos extremos válidos. Las llamadas muy largas (7.14% outliers) probablemente indican interés del cliente. Los clientes veteranos con muchos contactos previos (13.71% outliers) son un segmento importante. No se recomienda eliminar estos outliers sin analizar primero su relación con la conversión.

## Contribuciones

Si tienes alguna propuesta o corrección, no dudes en compartirla. Cualquier tipo de colaboración, ya sea en forma de código, documentación o comentarios, será apreciada y considerada. ¡Gracias por tu participación!

## Autor

* **GitHub** [Vic-tor123](https://github.com/Vic-tor123)

* **LinkedIn** [Vic-tor123LinkedIn](https://www.linkedin.com/in/victor-carballido-brea-03a52052/)