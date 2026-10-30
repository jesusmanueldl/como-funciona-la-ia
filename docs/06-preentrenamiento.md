# 6. Datos, preentrenamiento y ajuste fino

Un conjunto de entrenamiento sirve para ajustar parámetros; validación y prueba estiman generalización. Una época es un recorrido; un lote es una parte. Los optimizadores combinan gradientes con reglas como momento o Adam.

En preentrenamiento, un modelo aprende regularidades generales de grandes colecciones de datos. En ajuste fino se continúa el entrenamiento con un objetivo más específico. LoRA actualiza matrices pequeñas o de bajo rango mientras conserva la mayor parte de los pesos base. El aprendizaje supervisado usa etiquetas; el autosupervisado obtiene objetivos del propio dato, como predecir el siguiente token.

El ajuste mediante preferencias humanas puede comparar respuestas y optimizar una señal de preferencia, pero no elimina sesgos ni errores. Un modelo recién inicializado produce salidas sin utilidad garantizada; uno preentrenado capturó patrones; uno ajustado para instrucciones fue optimizado para seguir formatos y solicitudes.

**No confundir:** conversar no suele actualizar parámetros. Puede existir una memoria externa que cambie el contexto, pero eso no equivale a reentrenar.

**Autoevaluación:** ¿qué separa prueba de entrenamiento?, ¿qué problema combate el sobreajuste?, ¿qué ventaja tiene un ajuste eficiente? Actividad: dibuja el ciclo datos → pérdida → gradientes → actualización.

[Siguiente →](07-modelos-de-lenguaje.md)
