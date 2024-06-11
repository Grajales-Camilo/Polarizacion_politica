import matplotlib.pyplot as plt

# Crear un gráfico con subplots para cada escenario
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Títulos de los subplots
titles = ['Incremento de 5 Puntos', 'Decremento de 5 Puntos', 'Desplazamiento hacia el Centro', 'Polarización Aumentada']
curules_proyectadas = [2097.62, 1590.38, 1966.11, 1778.25]
colors = ['blue', 'red', 'green', 'purple']

# Crear los subplots
for i, ax in enumerate(axs.flatten()):
    ax.bar([titles[i]], [curules_proyectadas[i]], color=colors[i])
    ax.set_ylim(1500, 2200)
    ax.set_ylabel('Curules Proyectadas')
    ax.set_title(titles[i])
    ax.grid(axis='y', linestyle='--', linewidth=0.7)

# Ajustar el layout
plt.tight_layout()

# Mostrar el gráfico
plt.show()
