import numpy as np

# Definir la función
def f(x):
    return np.cos(x)

# Puntos dados
x = np.array([0, 0.3, 0.6, 0.9])
y = f(x)

# Calcular las diferencias divididas de Newton
def diferencias_divididas(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i,j] = (coef[i+1,j-1] - coef[i,j-1]) / (x[i+j] - x[i])
    print(coef)
    return coef[0, :]

# Evaluar el polinomio de Newton en un punto dado
def eval_polinomio_newton(coef, x, x_eval):
    n = len(coef)
    polinomio = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x_eval - x[j])
        polinomio += term
    return polinomio

# Calcular las diferencias divididas
coef = diferencias_divididas(x, y)

# Polinomio de grado 1 (usando los primeros dos coeficientes)
coef_grado1 = coef[:2]
aprox_grado1 = eval_polinomio_newton(coef_grado1, x, 0.45)

# Polinomio de grado 2 (usando los primeros tres coeficientes)
coef_grado2 = coef[:3]
aprox_grado2 = eval_polinomio_newton(coef_grado2, x, 0.45)

# Valor real de f(0.45)
valor_real = f(0.45)

# Calcular el error real
error_grado1 = abs(valor_real - aprox_grado1)
error_grado2 = abs(valor_real - aprox_grado2)

# Mostrar resultados
print(f"Aproximación con polinomio de grado 1: {aprox_grado1}")
print(f"Error real con polinomio de grado 1: {error_grado1}")
print(f"Aproximación con polinomio de grado 2: {aprox_grado2}")
print(f"Error real con polinomio de grado 2: {error_grado2}")
print(f"Valor real de f(0.45): {valor_real}")
