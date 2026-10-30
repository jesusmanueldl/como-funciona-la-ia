# 22. ¿Qué es la cuantización?

## Bits antes que nombres

Un bit puede representar dos estados; ocho bits forman un byte. FP32, FP16, BF16 e INT8 describen formas distintas de representar números. Cuantizar significa usar una representación de menor precisión, normalmente con escalas que permiten recuperar una aproximación útil.

Para $N$ parámetros de $b$ bits, el mínimo teórico de almacenamiento es:

$$
\text{bytes} = \frac{N \times b}{8}.
$$

Con $1{,}000{,}000$ parámetros INT8 se obtienen $1{,}000{,}000$ bytes antes de metadatos. El tamaño real puede ser mayor por escalas, alineación, activaciones y cachés.

## Qué cambia y qué no

La cuantización no elimina parámetros ni equivale a entrenar. Puede ahorrar memoria y mover un modelo a hardware más pequeño, pero una precisión menor puede alterar algunas salidas. El efecto depende del método, las capas y los datos de evaluación.

## Práctica

Calcula el tamaño teórico de un modelo de 7 mil millones de parámetros en FP16 y Q4. Después explica por qué tus dos resultados no describen por sí solos la memoria durante inferencia.
