"""Modelo de lenguaje de caracteres por bigramas, solo con biblioteca estándar."""

from collections import defaultdict


def entrenar(corpus):
    conteos = defaultdict(lambda: defaultdict(int))
    for anterior, siguiente in zip(corpus, corpus[1:]):
        conteos[anterior][siguiente] += 1
    return {k: dict(v) for k, v in conteos.items()}


def siguiente(modelo, caracter):
    opciones = modelo.get(caracter, {})
    return max(opciones, key=opciones.get) if opciones else " "


def generar(modelo, inicio, pasos=30):
    salida = inicio
    for _ in range(pasos):
        salida += siguiente(modelo, salida[-1])
    return salida


if __name__ == "__main__":
    corpus = "la ia aprende patrones. la ia transforma numeros. "
    modelo = entrenar(corpus)
    print(generar(modelo, "l"))
