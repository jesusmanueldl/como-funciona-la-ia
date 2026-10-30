"""Red lineal didáctica: entrena, guarda un checkpoint y lo restaura."""

import json
from pathlib import Path


def entrenar(datos, tasa=0.1, epocas=20):
    w, b = 0.0, 0.0
    for _ in range(epocas):
        for x, y in datos:
            pred = w * x + b
            error = pred - y
            w -= tasa * 2 * error * x
            b -= tasa * 2 * error
    return {"w": w, "b": b}


def predecir(modelo, x):
    return modelo["w"] * x + modelo["b"]


def guardar(modelo, ruta):
    Path(ruta).write_text(json.dumps(modelo, indent=2), encoding="utf-8")


def cargar(ruta):
    return json.loads(Path(ruta).read_text(encoding="utf-8"))


if __name__ == "__main__":
    datos = [(0.0, 1.0), (1.0, 3.0), (2.0, 5.0)]
    modelo = entrenar(datos)
    ruta = Path("/tmp/ia-checkpoint.json")
    guardar(modelo, ruta)
    restaurado = cargar(ruta)
    print("pesos entrenados:", modelo)
    print("predicción restaurada:", round(predecir(restaurado, 3.0), 3))
