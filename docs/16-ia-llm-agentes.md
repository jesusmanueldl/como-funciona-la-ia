# 16. ¿Qué es un modelo de lenguaje?

## Completa una frase: tú ya has hecho algo parecido

Si alguien escribe «Mañana llevaré paraguas porque va a...», seguramente piensas en «llover». Para elegir esa continuación utilizas asociaciones aprendidas y el contexto. Un modelo de lenguaje realiza una tarea relacionada, pero mediante cálculos: estima qué unidades de texto podrían seguir después de una secuencia.

### Primero, una probabilidad cotidiana

Ante «El cielo está...», supongamos que el modelo asigna, en un ejemplo **inventado**, 60 % a «azul», 25 % a «nublado», 10 % a «despejado» y 5 % a otras opciones. Si añadimos «durante la tormenta», esas probabilidades pueden cambiar. La información anterior se llama **contexto**.

### Del ejemplo a la notación

Los modelos modernos de lenguaje trabajan con **tokens**, que pueden ser palabras, fragmentos u otras unidades. Para una secuencia $x_1,x_2,\dots,x_{t-1}$ el modelo estima una distribución para la siguiente unidad $x_t$:

$$P(x_t\mid x_1,x_2,\ldots,x_{t-1}).$$

Aquí $P$ significa probabilidad; la barra vertical significa «dado el contexto»; $t$ es la posición que queremos predecir. La expresión **no afirma que el modelo consulte una lista completa de preguntas y respuestas**.

### ¿De dónde aprende las probabilidades?

Durante el entrenamiento ajusta parámetros usando ejemplos de texto y una tarea de predicción. En inferencia, utiliza esos parámetros ya aprendidos junto con los tokens actuales para calcular nuevas probabilidades.

### ¿Por qué puede redactar respuestas largas?

Selecciona un token, lo agrega al contexto y vuelve a calcular qué token puede seguir. El procedimiento se repite. De ese mecanismo, junto con los patrones aprendidos y el contexto de entrada, pueden emerger textos complejos. No garantiza verdad, coherencia permanente ni razonamiento correcto.

### ¿Todos los modelos de lenguaje predicen el siguiente token?

No exactamente. Existen modelos autoregresivos que lo hacen y modelos con otros objetivos, como predecir tokens ocultos. La idea general es aprender regularidades estadísticas del lenguaje; los detalles varían según la arquitectura y el entrenamiento.

### ¿Puede conocer el clima de este momento?

Un modelo aislado no consulta automáticamente información nueva. Si una aplicación le proporciona herramientas de búsqueda o datos actualizados, puede incorporar esas fuentes. Sin una herramienta externa, su respuesta puede ser desactualizada o inventada.

**Ejercicio.** Compara «El niño dejó el vaso sobre la...» con «El médico examinó la...»; piensa en tres continuaciones probables y explica por qué cambian. No es necesario que todos propongan exactamente las mismas palabras.

**Siguiente:** [convertir texto en números](17-agentes.md).
