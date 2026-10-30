# 26. Laboratorio práctico, preguntas frecuentes y conclusiones

## Recorrido del laboratorio

Ejecuta los ejemplos en este orden:

1. `neurona.py`: entrada, peso, sesgo y ReLU.
2. `contar_parametros.py`: dimensiones y parámetros.
3. `descenso_gradiente.py`: tres iteraciones de $\hat{y}=wx$ con $x=1$, $y=2$.
4. `entrenar_modelo.py`: pesos propios, checkpoint y restauración.
5. `clasificador.py`: clasificación sencilla y separación de datos.
6. `tokenizacion.py` y `modelo_lenguaje_pequeno.py`: tokens y bigramas.
7. `probabilidades.py`: softmax y temperatura.
8. `agente_simulado.py`: herramienta, validación y permisos.

Todos son modelos didácticos. Memorizar el conjunto de entrenamiento no demuestra generalización: prueba siempre con ejemplos no vistos.

## Preguntas frecuentes

1. **¿IA significa aprendizaje profundo?** No; también hay reglas, búsqueda y métodos estadísticos.
2. **¿Un parámetro es una palabra?** No, es un valor numérico.
3. **¿Más parámetros siempre es mejor?** No; importan datos, arquitectura, entrenamiento y evaluación.
4. **¿Preentrenado significa a medias?** No; significa que ya pasó una etapa previa.
5. **¿Un checkpoint garantiza calidad?** No; solo guarda un estado.
6. **¿LoRA actualiza todo el modelo?** Normalmente actualiza adaptadores, no todos los pesos.
7. **¿Un token es una palabra?** No necesariamente.
8. **¿Un LLM busca frases guardadas?** Produce distribuciones a partir de parámetros y contexto.
9. **¿La temperatura añade conocimiento?** No, cambia el muestreo.
10. **¿RAG reentrena?** No, añade información al contexto.
11. **¿La atención es conciencia?** No; es una operación matemática.
12. **¿Cuantizar elimina parámetros?** No, cambia su representación.
13. **¿Una respuesta fluida es verdadera?** No necesariamente.
14. **¿Un chatbot es un agente?** Solo si tiene objetivo, acciones y observación.
15. **¿Una herramienta da permisos?** No; los permisos deben validarse aparte.
16. **¿Un modelo local es automáticamente privado?** No; importan registros y aplicaciones.
17. **¿Entrenar y ejecutar son lo mismo?** No; entrenar actualiza pesos, inferir los usa.
18. **¿Validación y prueba son iguales?** No; la prueba final debe reservarse para evaluar.
19. **¿Una cifra 7B es exacta?** Suele ser una aproximación comercial.
20. **¿Un sistema puede equivocarse en aritmética?** Sí; hay que verificar operaciones.
21. **¿Los datos sintéticos son siempre seguros?** No; pueden heredar errores o sesgos.
22. **¿Semisupervisado significa entrenamiento incompleto?** No; usa datos etiquetados y sin etiquetar.
23. **¿Un modelo sin entrenar no tiene arquitectura?** Sí la tiene, pero sus pesos aún no son útiles.
24. **¿Un gradiente es una predicción?** No; indica cómo cambiar parámetros.
25. **¿Una fuente externa garantiza verdad?** No; debe evaluarse.
26. **¿La memoria externa cambia el modelo?** No, salvo que después se use para entrenarlo.
27. **¿Un agente debe actuar sin preguntar?** Solo dentro de límites explícitos.
28. **¿La analogía del cerebro es literal?** No; una neurona artificial es una función.
29. **¿La generación token a token implica una llamada de red por token?** No necesariamente.
30. **¿Puedo entrenar un LLM grande en este laboratorio?** No; los recursos son muy superiores.

## Conclusión

Una IA es un sistema construido de capas: datos, representaciones, funciones, parámetros, entrenamiento, inferencia y, en algunos casos, herramientas y permisos. Comprender esas capas permite admirar sus capacidades sin atribuirle propiedades que no se han demostrado.
