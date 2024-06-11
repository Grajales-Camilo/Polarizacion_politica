import matplotlib.pyplot as plt

# Datos de los escenarios y curules proyectadas
escenarios = ['Incremento_5', 'Decremento_5', 'Centro', 'Polarizacion']
curules_proyectadas = [2097.62, 1590.38, 1966.11, 1778.25]

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(escenarios, curules_proyectadas, color=['blue', 'red', 'green', 'purple'])

# Añadir etiquetas y título
plt.xlabel('Escenario')
plt.ylabel('Curules Proyectadas')
plt.title('Proyección de Curules bajo Diferentes Escenarios de Cambio en la Tendencia Política')
plt.grid(axis='y', linestyle='--', linewidth=0.7)

# Mostrar el gráfico
plt.show()