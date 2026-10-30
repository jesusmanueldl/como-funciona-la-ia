"""Entrenamiento de y = w*x para un solo ejemplo."""

def paso(w, x, objetivo, tasa):
    prediccion = w * x
    error = prediccion - objetivo
    perdida = error ** 2
    gradiente = 2 * error * x
    return w - tasa * gradiente, prediccion, perdida

if __name__ == "__main__":
    w = 1.0
    for i in range(2):
        w, pred, loss = paso(w, 2.0, 4.0, 0.1)
        print(f"iteración {i + 1}: w={w:.2f}, predicción={pred:.2f}, pérdida={loss:.2f}")
