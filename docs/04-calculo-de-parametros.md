# 4. ¿Cómo se calcula el número de parámetros?

## Neuronas y capas densas

Una neurona con tres entradas tiene tres pesos y un sesgo: `3+1=4`. Una capa densa con `n_entrada` entradas y `n_salida` neuronas tiene una matriz de pesos de tamaño `n_entrada × n_salida` y un sesgo por neurona:

\[
P=(n_{entrada}\times n_{salida})+n_{salida}.
\]

Para 3 entradas y 4 neuronas: `(3×4)+4=16`. La matriz contiene 12 pesos; el vector de sesgos contiene 4 valores.

```mermaid
flowchart LR
  I[3 entradas] --> W[Pesos 3 × 4 = 12]
  W --> O[4 salidas]
  B[4 sesgos] --> O
```

En una red `3 → 4 → 2`: primera capa `16`; segunda `(4×2)+2=10`; total `26`.

## Tensores y Transformers

Un tensor de forma `3×4×5` tiene `3×4×5=60` elementos. En arquitecturas de lenguaje, aparecen embeddings, proyecciones de query/key/value, capas feed-forward, normalizaciones y, según el diseño, vocabularios y pesos compartidos.

Un embedding de vocabulario `V` y dimensión `d` aporta `V×d`. Una proyección lineal de entrada `d_in` a `d_out` aporta `d_in×d_out+d_out`. Una normalización suele aportar dos vectores de tamaño `d`, aunque el detalle depende de la arquitectura.

El total real depende de dimensiones, capas, si hay sesgos, pesos compartidos y componentes opcionales. `1B`, `7B` y `70B` suelen ser cifras redondeadas, no identificadores exactos.

## No confundir escalas

Cantidad de parámetros no es cantidad de neuronas. Tampoco es cantidad de tokens de entrenamiento ni de respuestas guardadas. Dos modelos con igual número de parámetros pueden diferir en datos, arquitectura, entrenamiento y calidad.

## Ejercicio reproducible

```python
def parametros_densa(entradas, salidas):
    return entradas * salidas + salidas

print(parametros_densa(3, 4))  # 16
print(parametros_densa(4, 2))  # 10
```

## Resumen y práctica

Cuenta pesos por conexiones y sesgos por unidad de salida. Preguntas: ¿cuántos elementos hay en una matriz `3×4`? ¿qué cambia al compartir pesos? ¿por qué el nombre “7B” no basta para calcular memoria exacta?

[Siguiente: entrenamiento →](05-entrenamiento.md)
