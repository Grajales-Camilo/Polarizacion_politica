# Medición y Proyección de la Polarización Política en Colombia

Este proyecto analiza la polarización política en Colombia a través del análisis de datos electorales al Congreso en el primer cuarto del siglo XXI. El objetivo principal es comprender cómo la tendencia política de los partidos influye en su éxito electoral y cómo los cambios en estas tendencias podrían afectar la representación política en el futuro.  


### Contenido del Repositorio: 🗄 

**1.Polaridad_ordenado.csv:** Archivo CSV que contiene los datos electorales ordenados y limpios utilizados en el análisis.

**2.Polarizacion.ipynb:** Jupyter Notebook con el código completo utilizado para el análisis, incluyendo la limpieza de datos, el cálculo de índices, la creación de gráficos y la modelación de escenarios.

**3.Grafica_polarizacion.py:** Script de Python para generar los gráficos que visualizan la polarización política, la distribución de curules y la relación entre tendencia política y éxito electoral.

**4.Proyeccion_escenarios.py:** Script de Python que implementa el modelo de regresión lineal para proyectar cambios en la representación política bajo diferentes escenarios.

**5.Graficos_escenarios.py:** Script de Python para generar las gráficas que ilustran los posibles escenarios de cambio político y su impacto en la distribución de curules.

**6.Requirements.txt:** Librerias y versiones usadas en el modelo.


### Metodología: 🤖 

*Índice de Tendencia Política:* Se crea un índice que va de 0 (izquierda) a 100 (derecha) para clasificar los partidos políticos según su ideología.

*Análisis de Datos Electorales:* Se analizan los resultados electorales al Congreso desde 2002 hasta 2022, incluyendo el número de curules obtenidas por cada partido y su posición en el índice de tendencia política.

*Correlación y Regresión:* Se estudia la correlación entre la tendencia política y el éxito electoral, y se desarrolla un modelo de regresión lineal para predecir el número de curules en función de la tendencia.

*Proyección de Escenarios:* Se simulan diferentes escenarios de cambio político, como desplazamientos hacia la izquierda, la derecha o el centro, y se proyecta cómo estos cambios podrían afectar la distribución de curules en el Congreso.


### Resultados: 📊 
Los resultados del análisis revelan una relación moderada positiva entre la tendencia política y el éxito electoral, lo que sugiere que los partidos de derecha tienden a obtener más curules. Los escenarios de proyección muestran cómo diferentes cambios en las tendencias políticas podrían alterar la representación en el Congreso, proporcionando información valiosa para la planificación estratégica de campañas y políticas.


### Instrucciones de Uso:  

1. Clonar el repositorio: `git clone https://github.com/Grajales-Camilo/Polarizacion_politica.git`
2. Instalar las dependencias necesarias: `pip install -r 6.Requirements.txt`
3. Explorar el Jupyter Notebook `Polarizacion.ipynb` para comprender el análisis en detalle.
4. Ejecutar los scripts de Python para generar gráficos y proyecciones:     
  
       python Grafica_polarizacion.py
       python Proyeccion_escenarios.py       
       python Graficos_escenarios.py  


### Contribuciones:
Las contribuciones son bienvenidas. Si encuentras errores, tienes sugerencias para mejorar el análisis o quieres agregar nuevas funcionalidades, no dudes en abrir un issue o enviar un pull request.

Visita: [¿Cómo medir la polarización política y para qué?](https://www.linkedin.com/pulse/c%2525C3%2525B3mo-medir-la-polarizaci%2525C3%2525B3n-pol%2525C3%2525ADtica-y-para-qu%2525C3%2525A9-grajales-bedoya-ezrne/?trackingId=H5xXyzb3SXaDW154ox0L6Q%3D%3D) para más información ℹ 
