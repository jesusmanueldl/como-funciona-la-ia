# 14. Cómo entrenar un modelo propio: tutorial completo

## Construiremos una máquina que aprende una regla sencilla

Para aprender de manera comprobable no necesitas empezar entrenando un LLM. Un modelo lineal con dos parámetros permite ver casi todo el ciclo: datos, predicción, error, entrenamiento, evaluación y guardado.

### Paso 1: definir el problema

Queremos predecir $y=2x+1$ a partir de ejemplos. El modelo tendrá dos parámetros:

$$\hat y=wx+b.$$

No programaremos esos valores como solución; los ajustaremos con datos. Elegimos ejemplos de entrenamiento y reservamos entradas nuevas para prueba.

### Paso 2: preparar datos

Para entrenamiento: $(0,1)$, $(1,3)$, $(2,5)$, $(3,7)$. Para prueba: $(4,9)$ y $(5,11)$. En un conjunto real necesitaríamos más diversidad y una separación adecuada; aquí buscamos entender el procedimiento, no evaluar una aplicación comercial.

### Paso 3: inicializar y calcular pérdidas

Empezamos con $w=0$ y $b=0$. El modelo predice cero para todos. Definimos el error medio cuadrático sobre $n$ ejemplos:

$$L=\frac1n\sum_{i=1}^{n}(wx_i+b-y_i)^2.$$

En cada paso los gradientes son:

$$
\frac{\partial L}{\partial w}=\frac2n\sum_i(wx_i+b-y_i)x_i,
\qquad
\frac{\partial L}{\partial b}=\frac2n\sum_i(wx_i+b-y_i).
$$

Estas derivadas dicen cómo mover $w$ y $b$ para reducir localmente la pérdida. Usaremos una tasa de aprendizaje pequeña y varias iteraciones.

### Paso 4: entrenar, guardar y reutilizar

El archivo didáctico `ejemplos/tutorial_entrenar_desde_cero.py` incluido en esta entrega implementa la regresión sin dependencias externas, imprime pesos y pérdida, prueba entradas nuevas y guarda los parámetros en JSON. También recarga el JSON y compara las predicciones antes y después de restaurar.

No confundas guardar un par de números en JSON con el formato de un LLM: en los modelos grandes existen numerosos tensores, metadatos y, durante entrenamiento, estados adicionales.

### Paso 5: evaluar sin hacer trampas

Los datos de prueba no se utilizan para decidir cuándo detener el entrenamiento ni para cambiar hiperparámetros. Un buen resultado con un conjunto minúsculo y perfectamente lineal es solo una demostración didáctica. Modelos reales requieren mediciones reproducibles, pruebas con datos apropiados y análisis de errores.

### Paso 6: ¿qué sucede si usamos un modelo preentrenado?

La secuencia general sigue siendo semejante: preparar datos, definir objetivo, entrenar los parámetros elegidos, validar, evaluar y guardar. La diferencia está en que los pesos **no comienzan todos desde su inicialización original**: aprovechamos el entrenamiento previo y ajustamos solo lo necesario.

### Lista de verificación para entrenar de forma responsable

1. ¿La tarea y la métrica están definidas?
2. ¿Los datos tienen calidad, permisos y privacidad apropiados?
3. ¿Separaste entrenamiento, validación y prueba sin fugas?
4. ¿Elegiste arquitectura, pérdida y optimizador adecuados?
5. ¿Registraste semilla, versiones e hiperparámetros?
6. ¿Guardaste un checkpoint reproducible?
7. ¿Evaluaste en ejemplos no utilizados para entrenar?
8. ¿Documentaste los límites de uso?

**Ejercicio:** cambia los ejemplos para representar $y=3x+2$ y vuelve a entrenar. ¿Qué pesos aprendió la máquina? **Resultado esperado:** próximos a 3 y 2, si la optimización converge.

**Siguiente:** [un modelo de lenguaje diminuto](15-razonamiento.md).
