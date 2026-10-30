# 8. Embeddings y representaciones numéricas

Un embedding asigna un vector a un token. Si $e = [0.8, 0.1]$, sus coordenadas no son una definición textual; son una representación útil para las operaciones aprendidas.

El producto escalar es:

$$
a \cdot b = \sum_i a_i b_i.
$$

Con $a = [1, 2]$ y $b = [3, 4]$, $a \cdot b = 1 \times 3 + 2 \times 4 = 11$. Para comparar dirección se usa a menudo la similitud coseno:

$$
\cos(\theta) = \frac{a \cdot b}{\lVert a \rVert\,\lVert b \rVert}.
$$

La matriz de embeddings tiene una fila por token y una columna por dimensión. Durante las capas, las representaciones se vuelven contextuales: el vector de una palabra puede cambiar según las palabras cercanas.

**Analogía:** coordenadas en un mapa. **Límite:** no existe un eje universal llamado “significado”; la geometría depende del entrenamiento.

Actividad: calcula a mano dos productos escalares y explica por qué una magnitud grande no siempre significa similitud.

[Siguiente →](09-transformers.md)
