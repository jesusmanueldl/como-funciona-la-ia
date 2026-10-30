# 12. ¿Qué es un modelo preentrenado?

## Aprender a leer antes de estudiar medicina

Una persona que ya sabe leer, escribir y comprender textos puede aprender después vocabulario médico más rápidamente que alguien que empieza desde cero. Esta analogía ayuda a entender el **preentrenamiento**: un modelo aprende patrones generales en una fase anterior y luego sus pesos pueden reutilizarse para una tarea o dominio.

### Lo que ocurre en el preentrenamiento

En un modelo de lenguaje, una tarea frecuente es predecir tokens a partir de otros tokens. El proceso ajusta parámetros mediante muchísimos ejemplos de texto. Un modelo preentrenado puede aprender regularidades del lenguaje, relaciones estadísticas y ciertas habilidades generales. No implica que sea infalible ni que todas sus respuestas sean ciertas.

```mermaid
flowchart LR
  A[Arquitectura + inicialización] --> B[Preentrenamiento]
  B --> C[Modelo base preentrenado]
  C --> D[Ajuste especializado o de instrucciones]
  D --> E[Modelo adaptado]
```

### ¿Preentrenado significa incompleto?

No. El prefijo «pre-» indica una fase anterior a otra posible etapa, no que se haya detenido accidentalmente a mitad de un proceso. Un modelo base preentrenado puede estar plenamente terminado según su objetivo de preentrenamiento, aunque no sea especialmente adecuado para mantener conversaciones obedeciendo instrucciones.

### Modelo base, modelo instruct y especialización

Un modelo **base** se ha entrenado para tareas generales de modelado. Un modelo **ajustado para instrucciones** recibe entrenamiento adicional para responder a solicitudes humanas siguiendo formatos y comportamientos deseados. Un modelo **especializado** puede adaptarse a documentos legales, lenguaje técnico u otra tarea, siempre con validación adecuada.

### Transferencia de aprendizaje

Si los pesos ya capturan patrones útiles, podemos reutilizarlos en lugar de aprender absolutamente todo desde cero. A esto se le llama **transferencia de aprendizaje**. Algunas capas pueden congelarse y otras entrenarse; también es posible ajustar todos los pesos.

**Ejercicio:** imagina que tienes 100 ejemplos etiquetados para clasificar mensajes y dispones de un modelo que ya procesa lenguaje. ¿Qué ventaja potencial tiene reutilizarlo? **Respuesta:** puede aportar representaciones previas útiles, reduciendo la cantidad de datos o cómputo necesarios, aunque no garantiza buen rendimiento.

**No confundir:** la memoria de una conversación con el preentrenamiento. Guardar «me llamo Ana» en una base de datos y recuperarlo después no modifica por sí mismo los pesos.

**Siguiente:** [cómo adaptar un modelo existente](13-cuantizacion.md).
