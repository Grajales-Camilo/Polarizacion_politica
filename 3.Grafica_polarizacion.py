import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


#Pre-procesamiento
# Paso 1: Cargar archivo
data = pd.read_csv("d:/ModelosPoliticos/Polaridad.csv", delimiter= ";")

# Paso 2: Ordenar los datos por Año y por Índice de Tendecia política
datos_ordenados = data.sort_values(by=["Año", "Tendencia"], ascending=[False, False])

# Paso 3: Guardar el dataframe ordenado
datos_ordenados.to_csv("d:/ModelosPoliticos/Polaridad_ordenado.csv", index=False, sep=';')


# Procesamiento
# Paso 4: Crear DataFrame
df = pd.DataFrame(datos_ordenados)

# Paso 5: Graficar la dispersión de la polarización política para encontrar la línea de tendencia
# Separar los datos por año para trazar la línea
years = data['Año'].unique()

# Graficar
plt.figure(figsize=(14, 8))

for year in years:
    yearly_data = data[data['Año'] == year]
    plt.scatter(yearly_data['Tendencia'], yearly_data['Curules'], label=year)

# Ajustar una curva para ilustrar la línea de tendencia
# Combinar todos los datos para que se ajusten a una única línea
all_tendencia = data['Tendencia']
all_curules = data['Curules']

# Ajustar una curva polinómica (grado 2 por simplicidad)
coefficients = np.polyfit(all_tendencia, all_curules, 2)
polynomial = np.poly1d(coefficients)
trendline = polynomial(np.arange(0, 101))

# Trazar la línea de tendencia
plt.plot(np.arange(0, 101), trendline, color='red', linestyle='-', label='Tendencia')

# Agregar etiquetas y títulos
plt.xlabel('Índice de Tendencia (0: Izquierda, 50: Centro, 100: Derecha)')
plt.ylabel('Número de Curules')
plt.title(f'Polarización Política en Colombia \n (Elecciones de Congreso 2002 - 2022)')
plt.legend()
plt.grid(True)
plt.show()
