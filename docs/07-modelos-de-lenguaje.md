# 7. ¿Qué es un modelo de lenguaje?

Un modelo de lenguaje asigna probabilidades a secuencias. En predicción del siguiente token estima:

$$
P\left(x_t \mid x_1, x_2, \ldots, x_{t-1}\right).
$$

La barra significa “probabilidad de $x_t$ dado el contexto anterior”. Con “El cielo es”, tokens como “azul” pueden recibir mayor probabilidad que una palabra sin relación. Eso es una predicción estadística, no una consulta a una lista de frases completas.

Un token puede ser una palabra, fragmento, carácter o byte según el tokenizador. La división “Hola, ¿cómo estás?” en `Hola`, `,`, `¿cómo`, `estás`, `?` es ilustrativa: cada tokenizador real puede dividirla de otra forma.

El vocabulario asigna un entero a cada token. El texto se convierte en IDs, los IDs en vectores y el modelo calcula una distribución para el siguiente ID.

**Errores frecuentes:** token no es sinónimo de palabra; el modelo no necesita guardar todas las respuestas; una probabilidad alta no implica verdad.

**Práctica:** ejecuta `ejemplos/tokenizacion.py` y cambia el texto. Preguntas: ¿por qué una palabra rara puede ocupar varios tokens?, ¿qué información aporta el contexto?

[Siguiente →](08-embeddings.md)
