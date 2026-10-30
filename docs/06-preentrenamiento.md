# 6. ¿Cómo se calcula el número de parámetros?

## ¿Por qué un modelo puede tener «millones» o «miles de millones» de parámetros?

Un modelo no obtiene el número de parámetros porque haya leído esa cantidad de libros o preguntas. **El total se calcula a partir de la arquitectura:** cuántas tablas, matrices y vectores de valores aprendidos contiene.

### Primero: una neurona

Si una neurona recibe tres números y usa un peso por entrada y un sesgo, tiene $3+1=4$ parámetros. Cuatro neuronas con esas tres entradas, sin compartir pesos, tienen $4\times4=16$ parámetros.

### Segundo: una capa

La fórmula para una capa densa es:

$$P=(n_{\text{entrada}}\times n_{\text{salida}})+n_{\text{salida}}.$$

Para tres entradas y cuatro salidas:

$$
\begin{aligned}
P&=(3\times4)+4\\
 &=12+4\\
 &=\boxed{16}.
\end{aligned}
$$

La matriz de pesos tiene forma $4\times3$ y, por tanto, contiene 12 números. El vector de sesgos agrega otros 4.

### Tercero: muchas capas

Una red con tamaños $3\to4\to2$ contiene dos capas densas:

$$P_{1}=3\times4+4=16,$$
$$P_{2}=4\times2+2=10,$$
$$P_{\text{total}}=16+10=26.$$

No volvemos a contar entradas que no son pesos. En modelos con parámetros compartidos, contamos valores únicos, no el número de veces que se reutilizan.

### Cuarto: matrices grandes

Una matriz de $4096\times4096$ contiene:

$$4096\times4096=16\,777\,216$$

valores. ¡Una sola matriz puede superar los 16 millones! Si una arquitectura utiliza muchas matrices de ese tamaño y otras más, la suma llega a cientos de millones o miles de millones.

### ¿Qué significan K, M y B?

En el uso habitual de tamaños de modelos, K corresponde aproximadamente a miles, M a millones y B a miles de millones (*billion* anglosajón). Un modelo etiquetado «7B» suele tener aproximadamente siete mil millones de parámetros; puede ser una cifra redondeada.

### ¿Y en un Transformer?

En un Transformer de lenguaje existen, entre otros componentes, una tabla de **embeddings**, matrices para producir consultas, claves y valores de atención, proyecciones de salida, capas feed-forward y parámetros de normalización. Una explicación simplificada del conteo por capa utiliza las dimensiones de esas matrices y suma sus elementos. La fórmula exacta depende de la variante: atención con distintas dimensiones, sesgos opcionales, pesos compartidos, vocabulario, número de capas, etc.

Como ejemplo **hipotético**, una tabla de embeddings con vocabulario de 10 000 tokens y dimensión 256 posee $10\,000\times256=2\,560\,000$ valores entrenables. No afirma cuántos necesita un modelo real; muestra la multiplicación.

### Parámetros no significan memoria ni operaciones

- **Parámetros**: cantidad de valores almacenados y aprendidos.
- **Tamaño del archivo**: depende de cuántos bits se usan por valor, compresión y metadatos.
- **FLOPs**: cantidad estimada de operaciones; depende del cálculo y el uso de pesos.
- **Memoria de ejecución**: incluye pesos, activaciones, cachés y buffers.

**Ejercicio resuelto.** Una tabla de $500\times64$ contiene $32\,000$ valores. Si agregas una capa densa de 64 entradas y 10 salidas con sesgo, suma $64\times10+10=650$. Total: $32\,650$ parámetros, si no hay otros componentes.

**Práctica:** compara estos resultados con `ejemplos/contar_parametros.py` y cambia las dimensiones. **Siguiente:** [cómo se entrenan estos números](07-modelos-de-lenguaje.md).
