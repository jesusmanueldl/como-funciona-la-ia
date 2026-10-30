"""Conteo de parámetros de capas densas."""

def parametros_densa(entradas, salidas):
    return entradas * salidas + salidas

def parametros_red(dimensiones):
    return sum(parametros_densa(a, b) for a, b in zip(dimensiones, dimensiones[1:]))

if __name__ == "__main__":
    print("3 -> 4:", parametros_densa(3, 4))
    print("4 -> 2:", parametros_densa(4, 2))
    print("3 -> 4 -> 2:", parametros_red([3, 4, 2]))
