"""Tokenización ilustrativa: no representa un tokenizer de producción."""

def tokenizar(texto):
    signos = ",.!?;:"
    tokens = []
    for palabra in texto.split():
        if palabra and palabra[-1] in signos:
            tokens.extend([palabra[:-1], palabra[-1]])
        else:
            tokens.append(palabra)
    return [t for t in tokens if t]

if __name__ == "__main__":
    print(tokenizar("Hola, ¿cómo estás?"))
