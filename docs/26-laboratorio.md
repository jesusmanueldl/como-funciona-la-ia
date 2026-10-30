# 26. Laboratorio práctico y conclusiones

## Ya conocemos las piezas: ahora vamos a conectarlas

Recorrimos una cadena completa: datos → representaciones numéricas → parámetros → entrenamiento → modelo ajustado → inferencia → aplicación → agente con herramientas. Cada paso explica una parte diferente; decir simplemente «la IA piensa» oculta ese funcionamiento.

### Ruta de experimentos

1. **Neurona:** calcula $z=wx+b$ y comprueba cómo cambia la salida al cambiar un peso.
2. **Red neuronal:** cuenta parámetros de capas densas y comprueba dimensiones.
3. **Descenso de gradiente:** observa cómo $w$ se aproxima a 2 durante varias actualizaciones.
4. **Entrenamiento desde cero:** ajusta $w$ y $b$ para $y=2x+1$, evalúa y guarda el resultado.
5. **Bigramas:** calcula probabilidades de transiciones y genera caracteres.
6. **Inferencia:** cambia temperatura y observa cómo varían probabilidades.
7. **Agente simulado:** selecciona herramientas, valida y maneja errores.

Ejecuta los ejemplos desde la raíz del proyecto, con Python instalado. Los ejemplos suministrados con esta entrega incluyen uno de entrenamiento y otro de bigramas que no requieren dependencias adicionales.

### Preguntas frecuentes con respuestas

1. **¿Un parámetro es una neurona?** No: una neurona puede utilizar varios parámetros.
2. **¿Un parámetro es una palabra?** No: es un número utilizado en operaciones.
3. **¿7B son siete mil millones de respuestas?** No: es una cantidad aproximada de parámetros.
4. **¿De dónde salen los pesos?** Se inicializan y se ajustan durante entrenamiento.
5. **¿La arquitectura aprende por sí misma?** No: requiere un procedimiento y datos adecuados.
6. **¿Qué es la pérdida?** Una medida numérica del error según una función elegida.
7. **¿Qué es el gradiente?** Información sobre cómo cambia la pérdida respecto a parámetros.
8. **¿Qué es una época?** Un recorrido general por los datos de entrenamiento.
9. **¿Qué es inferencia?** Usar un modelo ajustado para obtener salidas nuevas.
10. **¿Conversar entrena el modelo?** Normalmente no cambia los pesos.
11. **¿Qué es preentrenado?** Un modelo con una fase previa de aprendizaje.
12. **¿Qué es parcialmente entrenado?** Un estado intermedio respecto a un plan de entrenamiento.
13. **¿Qué es semisupervisado?** Aprender con datos etiquetados y no etiquetados.
14. **¿Qué es fine-tuning?** Adaptar pesos de un modelo previamente entrenado.
15. **¿Qué es LoRA?** Una técnica de adaptación de bajo rango.
16. **¿Un checkpoint guarda solo pesos?** Puede guardar también optimizador y configuración.
17. **¿Un token es una palabra?** No necesariamente; puede representar otras unidades.
18. **¿Qué es un ID de token?** Un identificador entero del vocabulario.
19. **¿Qué es un embedding?** Una representación vectorial aprendida.
20. **¿Qué es atención?** Un mecanismo de combinación ponderada entre representaciones.
21. **¿Transformer es igual a LLM?** No: es una arquitectura utilizada por muchos modelos.
22. **¿Todos los LLM usan exactamente la misma estructura?** No.
23. **¿Qué es softmax?** Una transformación de puntuaciones a probabilidades normalizadas.
24. **¿Qué es temperatura?** Un control de distribución de probabilidades al generar.
25. **¿Más parámetros garantizan calidad?** No.
26. **¿Cuantizar elimina necesariamente parámetros?** No: suele reducir la precisión de almacenamiento.
27. **¿El tamaño de archivo es toda la RAM necesaria?** No.
28. **¿Un LLM consulta Internet solo?** No, requiere integración con herramientas.
29. **¿Un chatbot es un agente?** No necesariamente.
30. **¿Todo agente utiliza LLM?** No.
31. **¿La memoria externa modifica los pesos?** No por sí misma.
32. **¿Qué es RAG?** Recuperar información externa para complementar generación.
33. **¿Por qué puede alucinar?** La generación plausible no asegura verdad.
34. **¿Puede entrenarse un modelo sin GPU?** Sí, uno pequeño; grandes modelos pueden exigir recursos enormes.
35. **¿Se puede probar un agente sin ejecutar acciones reales?** Sí, con herramientas simuladas.

### Un glosario breve

**Activación:** transformación de la salida intermedia de una neurona. **Batch/lote:** grupo de ejemplos en un paso. **Contexto:** datos disponibles al modelo durante inferencia. **Dataset:** colección de datos. **Embedding:** vector aprendido. **Gradiente:** conjunto de derivadas de pérdida. **Hiperparámetro:** configuración del entrenamiento. **Inferencia:** producción de salidas con un modelo. **Logit:** puntuación antes de softmax. **Parámetro:** valor ajustable del modelo. **Token:** unidad de texto procesada por un tokenizador. **Transformer:** familia de arquitecturas con mecanismos de atención.

### Cierre

El valor de comprender la IA no consiste en memorizar siglas. Consiste en saber que detrás de una respuesta hay datos, funciones matemáticas, pesos, aprendizaje, cálculo, aplicaciones y límites verificables. Con esa base puedes comenzar a evaluar modelos, entrenar pequeños sistemas o desarrollar agentes de manera más responsable.

**Pregunta final:** elige una respuesta generada por una IA y explica, con tus palabras, qué parte pertenece al modelo y qué parte dependería de una aplicación externa.
