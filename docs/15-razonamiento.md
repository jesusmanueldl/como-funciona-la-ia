# 15. Entrenar un modelo de lenguaje pequeño

## Un primer modelo que aprende qué caracteres suelen seguirse

¿Puede una computadora producir texto sin guardar frases completas? Empezaremos con un modelo de **bigramas de caracteres**: para cada carácter cuenta qué carácter lo sigue. Este sistema no es una red neuronal Transformer ni un LLM, pero enseña con claridad la lógica de usar un contexto para predecir la continuación.

### Construimos un corpus

Supón que el pequeño conjunto de textos contiene: «casa», «cama», «casa». Si el contexto es la letra `c`, la continuación observada es `a` en los tres casos. Con la letra `a` aparecen distintas continuaciones. El modelo cuenta esas transiciones y obtiene frecuencias.

### Probabilidad condicional

Si el carácter anterior es $c$, estimamos:

$$P(x_{t}=a\mid x_{t-1}=c)=\frac{N(c,a)}{\sum_j N(c,j)},$$

con $N(c,a)$ igual al número de veces que observamos la transición `c`→`a`. En el conjunto pequeño, la probabilidad de `a` después de `c` sería 1. Esto no significa que la secuencia sea imposible de otra manera en el mundo: **solo refleja los ejemplos observados**.

### Evitar el problema de lo nunca visto

Si una transición no apareció, su frecuencia sería cero. Podemos agregar una pequeña cantidad a los conteos, una técnica llamada *suavizado*, para evitar probabilidades nulas y hacer que el procedimiento sea más flexible.

### Generar texto

Elegimos un carácter inicial. Consultamos las probabilidades de las posibles continuaciones y seleccionamos una. Repetimos con el nuevo carácter. El resultado puede parecer una palabra o producir secuencias extrañas: un bigrama solo mira un carácter de historia y no entiende el significado de una oración.

### ¿Es entrenamiento?

Sí, en el sentido amplio de **estimar parámetros estadísticos a partir de datos**, aunque no utilizamos gradientes. El parámetro aquí podría ser una probabilidad de transición. Otros modelos, como redes neuronales, aprenden pesos mediante optimización. Este contraste es importante: **no todo modelo de lenguaje es una red neuronal profunda**.

### Experimento

Ejecuta `ejemplos/modelo_lenguaje_pequeno.py` del repositorio, si está disponible. Cambia su corpus y observa cómo cambian las transiciones. La nueva versión educativa `ejemplos/bigramas_explicados.py` de este paquete imprime conteos y probabilidades para que puedas comprobarlas manualmente.

**Pregunta resuelta.** Si después de `a` observamos `s` tres veces y `m` una vez, sin suavizado: $P(s\mid a)=3/4=0.75$ y $P(m\mid a)=1/4=0.25$.

**No confundir:** un modelo de bigramas no tiene capacidad de razonamiento comparable a un sistema moderno. Sirve para comprender una pieza del problema: predicción de secuencias.

**Siguiente:** [qué significa modelo de lenguaje](16-ia-llm-agentes.md).
