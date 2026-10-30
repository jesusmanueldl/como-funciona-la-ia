# 3. ¿Cómo funciona una neurona artificial?

Una máquina muy pequeña puede multiplicar una entrada, sumar un desplazamiento y producir una salida. Esa es la idea de una neurona artificial: no es una neurona biológica, sino una función que combina números.

Para una entrada usamos $y=wx+b$. Con $x=3$, $w=2$ y $b=-1$, $y=5$. Con dos entradas, la suma ponderada es $z=w_1x_1+w_2x_2+b$ y una activación produce $a=f(z)$. ReLU, por ejemplo, conserva la parte positiva: $f(z)=\max(0,z)$.

Con $x_1=2$, $x_2=3$, $w_1=0.5$, $w_2=-0.2$ y $b=0.1$, se obtiene $z=0.5$ y $a=0.5$. El programa `ejemplos/neurona.py` ejecuta exactamente esa cuenta.

## Por qué hace falta una activación

Si solo apiláramos transformaciones lineales, varias capas podrían reducirse a una sola transformación lineal. Una activación no lineal permite construir fronteras y relaciones más variadas. No convierte a la máquina en un cerebro: cambia la forma matemática de la función.

## Conceptos que se reutilizan

Los parámetros son valores numéricos que el entrenamiento ajusta para que el modelo produzca resultados más útiles. En una neurona, pesos y sesgo son parámetros entrenables.

| Concepto | ¿Se ajusta durante el entrenamiento? | Ejemplo |
|---|---:|---|
| Peso | Sí | $w = -0.2$ |
| Sesgo | Sí | $b = 0.1$ |
| Hiperparámetro | No directamente | tasa de aprendizaje $\eta$ |
| Activación | No; es resultado | $a = 0.5$ |
| Gradiente | Se calcula | $\frac{\partial L}{\partial w}$ |
| Estado del optimizador | Se actualiza, pero no es el modelo | momento acumulado |

Los parámetros no equivalen a respuestas almacenadas, palabras del vocabulario ni ejemplos completos. Son números distribuidos en matrices y tensores. En entrenamiento se inicializan, por ejemplo, con valores aleatorios pequeños; una mala escala inicial puede dificultar la optimización.

## Una intuición cuantitativa

Si $z = w_1 x_1 + w_2 x_2 + b$, aumentar $w_1$ hace que $x_1$ influya más. Cambiar $b$ mueve la frontera de activación. El efecto depende también de la escala de las entradas.

## Parámetros frente a hiperparámetros

El tamaño de lote, el número de épocas y la tasa de aprendizaje se eligen para controlar el entrenamiento. No se infieren de la misma manera que los pesos. La distinción importa: “el modelo tiene 7B parámetros” no describe por sí sola sus datos, arquitectura o calidad.

## Errores frecuentes

- Contar una activación como un parámetro.
- Llamar “peso” a cualquier número intermedio.
- Suponer que más parámetros garantizan mejor respuesta.
- Confundir el estado temporal del optimizador con parámetros finales.

## Resumen y práctica

Un parámetro es ajustable; un hiperparámetro configura el proceso. Actividad: toma una neurona con dos entradas y construye una tabla de pesos entre $-1$ y $1$; observa cómo cambia $z$.

Preguntas: ¿qué valor se ajusta para desplazar la salida sin cambiar entradas? ¿Qué ocurre si todos los pesos son cero? ¿Por qué necesitamos validar fuera de los ejemplos vistos?

[Siguiente: contar parámetros →](04-calculo-de-parametros.md)
