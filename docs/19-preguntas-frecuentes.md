# 19. ¿Qué es un LLM y por qué su tamaño importa?

## «Grande» no es una fórmula mágica

Un LLM (*Large Language Model*, modelo de lenguaje grande) es un modelo de lenguaje de gran escala. Suele involucrar numerosos parámetros y grandes procesos de entrenamiento. **No existe un umbral universal que haga a un modelo LLM al superar exactamente cierta cifra.** El tamaño es una descripción de escala, no una prueba automática de calidad.

### ¿Qué representan los números como 1B o 7B?

En esa notación habitual, «B» significa miles de millones. Una etiqueta 7B sugiere aproximadamente 7 000 millones de parámetros; la cifra exacta puede variar. El recuento sale de sumar elementos de tensores aprendidos, no del número de respuestas almacenadas.

### ¿Por qué un modelo pequeño puede ser útil?

Un modelo pequeño puede requerir menos memoria y cómputo, responder más rápido y ser práctico para tareas delimitadas. Un modelo más grande podría afrontar tareas más complejas, pero también puede consumir más recursos y equivocarse. La calidad depende de arquitectura, datos, entrenamiento, adaptación, evaluación y contexto, no solo del número de pesos.

### Parámetros y capacidad de cómputo

Supongamos **hipotéticamente** un modelo con mil millones de parámetros representados a 16 bits cada uno. Sus pesos ocuparían al menos unos dos mil millones de bytes decimales antes de añadir otros componentes. Eso no es necesariamente la RAM total necesaria para ejecutarlo: también hay activaciones, cachés y buffers.

### ¿Qué aprende en el entrenamiento?

Patrones de secuencias, regularidades y representaciones útiles. Las conexiones entre numerosos pesos pueden ayudar a reproducir conocimiento y resolver tareas, pero eso no equivale a tener almacenada cada pregunta con una respuesta fija.

### ¿Qué significa contexto?

Es el contenido que se ofrece a la red para la inferencia: instrucciones, mensajes anteriores, documentos o tokens generados. Un modelo puede tener pesos fijos y producir una respuesta distinta cuando cambia el contexto.

### ¿Qué puede fallar?

Puede inventar fuentes, razonar erróneamente, repetir sesgos o interpretar mal la intención. Hablar con fluidez no demuestra por sí solo que el resultado sea cierto. Para aplicaciones delicadas hacen falta comprobaciones y supervisión.

### Mini cuestionario con respuestas

1. **¿7B significa siete mil millones de palabras?** No: se refiere aproximadamente a parámetros.
2. **¿Un modelo 70B siempre gana a uno menor?** No, depende de tarea y evaluación.
3. **¿Puede un LLM funcionar sin Internet?** Sí, si sus pesos y un motor compatible están disponibles localmente.
4. **¿Puede un LLM abrir aplicaciones por sí solo?** El modelo genera señales o texto; una aplicación con permisos y herramientas realiza acciones.
5. **¿Cambiar el prompt reentrena el modelo?** No, normalmente cambia el contexto de inferencia.

**Siguiente:** [cómo se genera una respuesta token a token](20-glosario.md).
