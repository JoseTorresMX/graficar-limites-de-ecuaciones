# Importamos los modulos necesarios.
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

# Creamos una función.
def y_func(x, t):
    return np.sin(t*x)/x

#Preparar los valores de (π) y (t) que se necesita para graficar la funcion. 
x_valores = np.linspace(-2*np.pi, 2*np.pi, 400)
t_valores = [1, 2, 3]

#Crar un figura con un tamaño especifico.
fig=plt.figure(figsize=(10, 6))
#Crear un subgráfico en la figura que se definio anteriormente.
#Y se configuran las posiciones de los ejes en el subgráfico.
ax=fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')

#Se ocultan los bordes derecho y superiror del gráfico
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#Se establecen la posición de kas marcas de los ejes en el subgráfico.
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#Bucle 'for' que cacula los valores de 'y' para cada valor de 't'
#en la lista 't_valores' utilizando la función 'y_func'
for t in t_valores:
    y_valores = y_func(x_valores, t)
    plt.plot(x_valores, y_valores, label=f't = {t}')
#Se establece el limite de 'x' en 0.
#Se calculan los valores de la función en el 'limite x=0' para cuando 't',
#tome cada valor en la lista 't_valores'
#Luego se traza un punto, en este caso ROJO en cada uno de esos puntos de la gráfica.
x_limite = 0
y_limite_valores = [
    np.sin(t*x_limite)/x_limite if x_limite != 0 else 1 for t in t_valores]
plt.scatter([x_limite]*len(t_valores), y_limite_valores,color='red', label='Limite en x=0')

#Con un 'for', se agrega anotaciones a los puntos del limite en 'x=0' en la gráfica,
#esto indicando el valor o valores ocrrespondientes a 't'.
for i, t in enumerate(t_valores):
    plt.annotate(f'Limite en x=0 cuanto t={t}', xy=(x_limite, y_limite_valores[i]), xytext=(
        -50, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='blue'))

#Se configura las propiedades de la gráfica antes de ser mostrada.
plt.title("Gráfica de y = sin(tx)/x para diferentes valores de t con el límite en x=0")
plt.xlabel('x')
plt.ylabel('y')

#Con 'xticks' se configura las marcar del eje 'x'
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],['-2π', '-π', '0', 'π', '2π'])

#Se definenen los límites de los ejes y de la grafica
plt.ylim(-1, 3)
plt.legend()
plt.grid(False)
plt.show()

#Correr app Streamlit
st.pyplot(fig)
