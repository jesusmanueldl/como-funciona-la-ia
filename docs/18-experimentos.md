# 18. Transformers y mecanismo de atención, desde la intuición

## ¿Por qué importa la palabra que apareció antes?

Lee «Ana dejó la taza en la mesa porque **estaba** mojada». ¿Qué estaba mojado: la taza o la mesa? Para interpretar «estaba» necesitamos analizar su relación con otras partes de la oración. Un mecanismo de **atención** permite que las representaciones de ciertos tokens se combinen utilizando información de otros tokens.

### Tres nombres extraños: Query, Key y Value

En atención, cada token se transforma mediante matrices aprendidas en tres representaciones: **consulta** (*query*, Q), **clave** (*key*, K) y **valor** (*value*, V). Una analogía limitada: la consulta pregunta qué información busca; las claves ayudan a evaluar qué piezas son relevantes; los valores contienen información que se combina.

### La fórmula formal

$$\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^{\mathsf T}}{\sqrt{d_k}}\right)V.$$

$Q$, $K$ y $V$ son matrices. $K^{\mathsf T}$ es la transpuesta de $K$; $d_k$ es la dimensión de las claves; $\sqrt{d_k}$ escala las puntuaciones; *softmax* convierte puntuaciones en pesos que suman 1 por fila. Luego esos pesos combinan los vectores de $V$.

### Cálculo diminuto con una consulta

Tomemos una consulta $q=[1,0]$, dos claves $k_1=[1,0]$, $k_2=[0,1]$, y valores escalares ilustrativos $v_1=10$, $v_2=20$. Como $d_k=2$, las puntuaciones escaladas son $1/\sqrt2\approx0.7071$ y $0$. Tras softmax:

$$
\begin{aligned}
\alpha_1&=\frac{e^{0.7071}}{e^{0.7071}+e^0}\approx0.6698,\\
\alpha_2&\approx0.3302.
\end{aligned}
$$

La salida ponderada será aproximadamente $0.6698(10)+0.3302(20)=13.302$. Este cálculo solo ilustra una consulta; las arquitecturas reales trabajan con matrices y múltiples posiciones.

### ¿Qué significa atención causal?

Cuando un modelo genera texto de izquierda a derecha, no debe utilizar tokens futuros que aún no existen. Una **máscara causal** evita que ciertas posiciones atiendan a posiciones posteriores. Otros modelos utilizan distintos esquemas de atención.

### Varias cabezas y capas

La **atención multicabeza** realiza varios cálculos de atención con proyecciones aprendidas diferentes. Los resultados se combinan. Un bloque Transformer también incluye transformaciones *feed-forward*, conexiones residuales y normalizaciones. No basta con atención para describir el bloque completo.

### Posiciones y límites

Como la secuencia tiene orden, el modelo necesita información posicional. Las variantes implementan esa información de distintas formas. El tamaño de contexto y el costo de atención dependen de la arquitectura y configuración.

**Ejercicio.** Si las dos puntuaciones antes de softmax fueran iguales, sus pesos serían $0.5$ y $0.5$, y los valores 10 y 20 producirían 15.

**Error frecuente:** atención matemática no es sinónimo de atención humana consciente. **Siguiente:** [qué es un LLM](19-preguntas-frecuentes.md).
