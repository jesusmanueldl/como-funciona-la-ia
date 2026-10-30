"""Clasificador mínimo de una característica: largo de un mensaje."""


def clasificar(largo, umbral=20):
    return "largo" if largo >= umbral else "corto"


if __name__ == "__main__":
    entrenamiento = [(5, "corto"), (12, "corto"), (30, "largo"), (45, "largo")]
    for largo, etiqueta in entrenamiento:
        predicha = clasificar(largo)
        print(f"{largo:2} caracteres: esperada={etiqueta:6} predicha={predicha}")
