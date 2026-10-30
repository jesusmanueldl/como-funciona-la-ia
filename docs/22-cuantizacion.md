# 22. Cuantización: por qué algunos modelos ocupan menos

## No siempre necesitamos guardar tantos decimales

Imagina una medición de 12.345678 metros. Quizá para una tarea sea suficiente guardarla como 12.35. Reducir precisión ahorra espacio, aunque introduce error. La **cuantización** utiliza una idea relacionada: representar números de un modelo con menos bits, normalmente mediante escalas y formatos específicos.

### Bits, bytes y tamaños

Un bit puede representar 0 o 1; ocho bits forman un byte. Un número FP32 ocupa usualmente 32 bits = 4 bytes. FP16 y BF16 utilizan 16 bits = 2 bytes, pero con distinta distribución de precisión y rango. INT8 utiliza 8 bits = 1 byte, normalmente junto con reglas de escala para representar pesos cuantizados.

### Cálculo teórico básico

$$T_{\text{bytes}}\approx\frac{N\,b}{8},$$

con $N$ parámetros y $b$ bits por parámetro. Para un millón de pesos:

| Representación hipotética | Bytes de pesos teóricos |
|---|---:|
| 32 bits | 4 000 000 |
| 16 bits | 2 000 000 |
| 8 bits | 1 000 000 |
| 4 bits | 500 000 |

Esta tabla es **teórica**, no una predicción exacta del tamaño de un archivo real. Puede haber escalas por bloques, metadatos, alineamiento y tensores de diferentes precisiones.

### Ejemplo de una cuantización elemental

Supongamos que representamos $0.37$ con pasos de $0.1$: el valor almacenado sería aproximadamente $0.4$ y el error $0.03$. En procedimientos reales hay escalas y puntos cero o diseños específicos para distribuir los niveles disponibles. La cuantización puede reducir memoria y acelerar operaciones compatibles, pero también alterar la precisión de predicciones.

### ¿Reduce la cantidad de parámetros?

Habitualmente no: modifica cómo se **representan** los pesos. Una matriz de mil elementos sigue teniendo mil elementos, aunque ahora cada uno ocupe menos bits en promedio. Algunos procedimientos incluyen poda o cambios estructurales, que son conceptos diferentes.

### ¿Qué es GB frente a GiB?

1 GB decimal = 1 000 000 000 bytes. 1 GiB binario = 1 073 741 824 bytes. Por eso algunas herramientas muestran números distintos para el mismo archivo.

**Ejercicio:** un modelo hipotético de 2 000 000 de parámetros a 8 bits por peso necesita al menos 2 000 000 bytes teóricos para esos pesos. ¿Sería necesariamente la RAM total? **No**: faltan otros datos de ejecución.

**Siguiente:** [memoria y razonamiento](23-memoria-razonamiento.md).
