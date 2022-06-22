# Función que comprueba si se repite un número en un conjunto de números.

def has_duplicates(y):
    x = y[:]
    x.sort()
    for i in range(len(x)):
        if i == len(x) - 1:
            pass
        else:
            if x[i] == x[i + 1]:
                return(True)

# Función que genera números aleatorios del 1 al 365 para n_personas, lo repite n_muestras veces y obtiene cuántas veces al menos 2 personas tienen el mismo cumpleaños.

from random import randint

def bird_paradox(n_personas, n_muestras):
    bd = []
    for i in range(n_muestras):
        x = []
        for j in range(n_personas):
            x.append(randint(1, 365))  
        bd.append(x)
    y = 0
    for i in range(len(bd)):
        if has_duplicates(bd[i]):
            y = y + 1
    return(y)

#Si generamos aleatoriamente cumpleaños para 23 personas 1 millón de veces:

n_duplicas = bird_paradox(n_personas = 23, n_muestras = 1000000)

print('Hay al menos dos personas que cumplen el mismo día el ' + str(round((n_duplicas / 1000000) * 100, 3)) + ' % de las veces.')