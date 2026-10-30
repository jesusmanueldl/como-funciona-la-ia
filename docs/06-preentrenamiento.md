# 6. ¿Cómo se calcula el número de parámetros?

Una neurona con tres entradas tiene $3+1=4$ parámetros. Una capa con 3 entradas y 4 neuronas tiene $3\times4$ pesos y 4 sesgos, por lo que $P=(3\times4)+4=16$. En una red $3\rightarrow4\rightarrow2$, el total es $16+10=26$.

Las dimensiones explican el conteo: una matriz $W\in\mathbb{R}^{3\times4}$ contiene 12 pesos y un vector de sesgos contiene 4. Un embedding de vocabulario $V$ y dimensión $d$ contiene $V\times d$ valores. Parámetros, operaciones y memoria no son lo mismo.

## Datos, preentrenamiento y ajuste fino

Un conjunto de entrenamiento sirve para ajustar parámetros; validación y prueba estiman generalización. Una época es un recorrido; un lote es una parte. Los optimizadores combinan gradientes con reglas como momento o Adam.

En preentrenamiento, un modelo aprende regularidades generales de grandes colecciones de datos. En ajuste fino se continúa el entrenamiento con un objetivo más específico. LoRA actualiza matrices pequeñas o de bajo rango mientras conserva la mayor parte de los pesos base. El aprendizaje supervisado usa etiquetas; el autosupervisado obtiene objetivos del propio dato, como predecir el siguiente token.

El ajuste mediante preferencias humanas puede comparar respuestas y optimizar una señal de preferencia, pero no elimina sesgos ni errores. Un modelo recién inicializado produce salidas sin utilidad garantizada; uno preentrenado capturó patrones; uno ajustado para instrucciones fue optimizado para seguir formatos y solicitudes.

**No confundir:** conversar no suele actualizar parámetros. Puede existir una memoria externa que cambie el contexto, pero eso no equivale a reentrenar.

**Autoevaluación:** ¿qué separa prueba de entrenamiento?, ¿qué problema combate el sobreajuste?, ¿qué ventaja tiene un ajuste eficiente? Actividad: dibuja el ciclo datos → pérdida → gradientes → actualización.

[Siguiente →](07-modelos-de-lenguaje.md)
