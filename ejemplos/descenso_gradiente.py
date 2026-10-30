"""Entrenamiento reproducible de y = 2x con un solo ejemplo."""

def paso(w, x, objetivo, tasa):
    prediccion = w * x
    error = prediccion - objetivo
    perdida = error ** 2
    gradiente = 2 * error * x
    nuevo_w = w - tasa * gradiente
    return nuevo_w, prediccion, error, perdida, gradiente

if __name__ == "__main__":
    x, objetivo, tasa, w = 1.0, 2.0, 0.1, 0.0
    print("iteración | x | esperado | predicción | error | gradiente | peso antes | peso después")
    for i in range(3):
        antes = w
        w, pred, error, loss, gradiente = paso(w, x, objetivo, tasa)
        print(f"{i + 1:9} | {x:.1f} | {objetivo:.1f} | {pred:.4f} | {error:.4f} | {gradiente:.4f} | {antes:.4f} | {w:.4f} | pérdida={loss:.4f}")
