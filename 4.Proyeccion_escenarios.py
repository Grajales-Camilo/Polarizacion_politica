import pandas as pd

# Cargar el archivo CSV
file_path = 'd:/ModelosPoliticos/Polaridad_ordenado.csv'
data = pd.read_csv(file_path, delimiter=';')

# Definición de escenarios
coeficiente = 0.63
intercepto = -11.86

escenarios = {
    'Incremento_5': data['Tendencia'] + 5, # Si la campaña se mueve un poco a la derecha👨🏾‍💼➡️
    'Decremento_5': data['Tendencia'] - 5, # Si la campaña se mueve un poco a la izquierda ⬅️👨🏾‍💼
    'Centro': data['Tendencia'].apply(lambda x: 50 if x < 25 or x > 75 else x), # Si los extremos se moderan ➡️👨🏾‍💼⬅️
    'Polarizacion': data['Tendencia'].apply(lambda x: 0 if x < 25 else (100 if x > 75 else x)) # Si las tendencias políticas se polarizan ⬅️👨🏾‍💼➡️
}

# Usando la ecuación de regresión lineal calculamos la cantidad de curules 
proyecciones = {}
for escenario, tendencias in escenarios.items():
    proyecciones[escenario] = coeficiente * tendencias + intercepto

# Suma total de curules proyectadas para cada escenario
curules_proyectadas = {escenario: sum(proyeccion) for escenario, proyeccion in proyecciones.items()}

# Mostrar los resultados detallados
print(curules_proyectadas)

