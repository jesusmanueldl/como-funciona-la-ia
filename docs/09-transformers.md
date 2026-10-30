# 9. Tipos de aprendizaje: supervisado, autosupervisado y más

## ¿Quién le dice a la máquina la respuesta correcta?

Imagina una caja de fotografías de frutas. Algunas tienen una etiqueta que dice «manzana» o «naranja» y otras no. Según cómo utilicemos esas fotografías, distinguimos varias formas de aprendizaje.

### Supervisado: ejemplos con respuesta

Le mostramos una foto junto con su etiqueta. El sistema predice, compara con la etiqueta y ajusta parámetros para disminuir su error. Se utiliza en clasificación y regresión; por ejemplo, predecir un precio numérico en lugar de una categoría.

### No supervisado: buscar estructura sin etiquetas de destino

Le damos fotografías sin decir qué fruta representa cada una. Un algoritmo puede agrupar imágenes parecidas. El resultado no tiene por qué coincidir con las categorías humanas: quizá agrupe por color o iluminación. El objetivo es encontrar estructura, no necesariamente predecir una etiqueta.

### Autosupervisado: fabricar un objetivo a partir del propio dato

Si tenemos la secuencia «El perro duerme en la ___», podemos ocultar o predecir una parte usando el resto. El dato contiene información necesaria para construir el objetivo. Muchos modelos de lenguaje modernos utilizan tareas autosupervisadas en su preentrenamiento.

### Semisupervisado: pocos ejemplos etiquetados y muchos sin etiquetar

Quizá solo 50 fotos tengan etiquetas y otras 5 000 no. Podemos combinar ambas colecciones mediante métodos apropiados. **Semisupervisado no significa «entrenado a medias».** Esa última expresión solo describe, informalmente, cuánto ha avanzado un proceso.

### Aprendizaje por refuerzo: aprender a partir de recompensas

Un agente simulado realiza acciones en un entorno y recibe recompensas o penalizaciones. Busca una estrategia para acumular recompensas a lo largo del tiempo. No siempre recibe una respuesta correcta por cada decisión. La elección de recompensas puede llevar a comportamientos inesperados si el objetivo está mal especificado.

| Enfoque | Qué recibe | Qué trata de aprender |
|---|---|---|
| Supervisado | Entradas y etiquetas | Predecir etiquetas o valores |
| No supervisado | Entradas sin etiqueta objetivo | Encontrar estructura |
| Autosupervisado | Datos con objetivo derivado de ellos | Aprender representaciones y predicciones |
| Semisupervisado | Pocos datos etiquetados y muchos sin etiquetar | Aprovechar ambas fuentes |
| Por refuerzo | Interacciones y recompensas | Seleccionar acciones útiles |

### El mismo problema, distintas estrategias

Para clasificar correos, el supervisado usa correos etiquetados. El no supervisado podría agrupar mensajes parecidos sin llamar «spam» a ninguno. El autosupervisado puede aprender representaciones de los textos prediciendo fragmentos. El semisupervisado combina mensajes etiquetados y no etiquetados. El refuerzo podría optimizar decisiones de un sistema interactivo, pero no es la opción más directa para una primera clasificación de spam.

**Ejercicio.** Un sistema practica un videojuego y recibe puntos según sus acciones. **Solución:** es un escenario típico de aprendizaje por refuerzo. Un modelo que predice palabras a partir de textos sin etiquetas externas utiliza una tarea autosupervisada.

**Siguiente:** [un modelo antes de aprender](10-llm.md).
