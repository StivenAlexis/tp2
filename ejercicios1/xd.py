#Ejercicio A Lagrange
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Función para imprimir el polinomio de Lagrange
def imprimir_polinomio(polinomio):
    coeficientes = polinomio.coefficients
    grado = len(coeficientes) - 1
    polinomio_str = " + ".join([f"{coef:.5f}x^{grado-i}" if i < grado else f"{coef:.5f}"
                                for i, coef in enumerate(coeficientes)])
    polinomio_str = polinomio_str.replace("x^1", "x").replace("x^0", "")
    print(polinomio_str)

# Puntos de interpolación
puntos = np.array([[8.1, 16.94410], [8.3, 17.56492], [8.6, 18.50515], [8.7, 18.82091]])
x = puntos[:, 0]
y = puntos[:, 1]

# Generar los polinomios de Lagrange
polinomio_grado_1 = lagrange(x[:2], y[:2])
polinomio_grado_2 = lagrange(x[:3], y[:3])
polinomio_grado_3 = lagrange(x, y)

# Imprimir los polinomios
print("Polinomio de Lagrange de grado 1:")
imprimir_polinomio(polinomio_grado_1)

print("\nPolinomio de Lagrange de grado 2:")
imprimir_polinomio(polinomio_grado_2)

print("\nPolinomio de Lagrange de grado 3:")
imprimir_polinomio(polinomio_grado_3)

# Evaluar los polinomios en x = 8.4
x_evaluar = 8.4
resultado_grado_1 = polinomio_grado_1(x_evaluar)
resultado_grado_2 = polinomio_grado_2(x_evaluar)
resultado_grado_3 = polinomio_grado_3(x_evaluar)

# Calcular el error absoluto y relativo
error_absoluto_1 = abs(resultado_grado_1 - resultado_grado_3)
error_absoluto_2 = abs(resultado_grado_2 - resultado_grado_3)
error_relativo_1 = abs((resultado_grado_1 - resultado_grado_3) / resultado_grado_3)
error_relativo_2 = abs((resultado_grado_2 - resultado_grado_3) / resultado_grado_3)

print(f"\nEvaluación del polinomio de grado 1 en x={x_evaluar}: {resultado_grado_1:.8f}")
print(f"Evaluación del polinomio de grado 2 en x={x_evaluar}: {resultado_grado_2:.8f}")
print(f"Evaluación del polinomio de grado 3 en x={x_evaluar}: {resultado_grado_3:.8f}")

print(f"\nError absoluto del polinomio de grado 1 respecto al de grado 3: {error_absoluto_1:.8f}")
print(f"Error absoluto del polinomio de grado 2 respecto al de grado 3: {error_absoluto_2:.8f}")
print(f"Error relativo del polinomio de grado 1 respecto al de grado 3: {error_relativo_1:.8f}")
print(f"Error relativo del polinomio de grado 2 respecto al de grado 3: {error_relativo_2:.8f}")

# Graficar los puntos y los polinomios
x_grafico = np.linspace(min(x) - 0.1, max(x) + 0.1, 500)
y_grado_1 = polinomio_grado_1(x_grafico)
y_grado_2 = polinomio_grado_2(x_grafico)
y_grado_3 = polinomio_grado_3(x_grafico)

plt.plot(x, y, 'o', label='Puntos de interpolación')
plt.plot(x_grafico, y_grado_1, label='Polinomio grado 1')
plt.plot(x_grafico, y_grado_2, label='Polinomio grado 2')
plt.plot(x_grafico, y_grado_3, label='Polinomio grado 3')
plt.axvline(x=x_evaluar, color='gray', linestyle='--', label=f'x = {x_evaluar}')
plt.axhline(y=resultado_grado_3, color='gray', linestyle='--')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Lagrange')
plt.show()