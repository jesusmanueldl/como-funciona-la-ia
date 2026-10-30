"""Neurona artificial mínima."""

def neurona(entradas, pesos, sesgo):
    z = sum(x * w for x, w in zip(entradas, pesos)) + sesgo
    return z, max(0.0, z)

if __name__ == "__main__":
    z, salida = neurona([2, 3], [0.5, -0.2], 0.1)
    print(f"z={z:.3f}; ReLU(z)={salida:.3f}")
