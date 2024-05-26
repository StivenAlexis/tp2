#Ejercicio C Newton
import numpy as np

# Definir la función
def funcion_Raiz(x):
    return np.sqrt(1+x)

# Puntos dados
puntos_x = np.array([0, 0.3, 0.6, 0.9])
valores_y = funcion_Raiz(puntos_x)

# Calcular las diferencias divididas de Newton
def calcular_diferencias_divididas(puntos_x, valores_y):
    n = len(valores_y)
    matriz_diferencias = np.zeros([n, n])
    matriz_diferencias[:,0] = valores_y
    
    for j in range(1, n):
        for i in range(n - j):
            matriz_diferencias[i,j] = (matriz_diferencias[i+1,j-1] - matriz_diferencias[i,j-1]) / (puntos_x[i+j] - puntos_x[i])
    print(matriz_diferencias)
    return matriz_diferencias[0, :]

# Evaluar el polinomio de Newton en un punto dado
def evaluar_polinomio_newton(coeficientes, puntos_x, x_evaluar):
    n = len(coeficientes)
    polinomio = coeficientes[0]
    for i in range(1, n):
        termino = coeficientes[i]
        for j in range(i):
            termino *= (x_evaluar - puntos_x[j])
        polinomio += termino
    return polinomio

# Calcular las diferencias divididas
coeficientes = calcular_diferencias_divididas(puntos_x, valores_y)

# Polinomio de grado 1 (usando los primeros dos coeficientes)
coeficientes_grado1 = coeficientes[:2]
aproximacion_grado1 = evaluar_polinomio_newton(coeficientes_grado1, puntos_x, 0.45)

# Polinomio de grado 2 (usando los primeros tres coeficientes)
coeficientes_grado2 = coeficientes[:3]
aproximacion_grado2 = evaluar_polinomio_newton(coeficientes_grado2, puntos_x, 0.45)

# Valor real de f(0.45)
valor_real = funcion_Raiz(0.45)

# Calcular el error real
error_grado1 = abs(valor_real - aproximacion_grado1)
error_grado2 = abs(valor_real - aproximacion_grado2)

# Mostrar resultados
print(f"Aproximación con polinomio de grado 1: {aproximacion_grado1}")
print(f"Error real con polinomio de grado 1: {error_grado1}")
print(f"Aproximación con polinomio de grado 2: {aproximacion_grado2}")
print(f"Error real con polinomio de grado 2: {error_grado2}")
print(f"Valor real de f(0.45): {valor_real}")

