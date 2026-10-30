# 5. ¿Qué son realmente los parámetros?

## El número que una máquina no conoce al empezar

Imagina una pequeña calculadora que debe aprender un descuento del 20 %. Le damos precios antes y después del descuento. No queremos programar a mano todas las respuestas posibles: queremos que encuentre el factor $0.8$.

Podemos representar la operación como $\hat y=wx+b$. El sombrerito en $\hat y$ indica **predicción**, no resultado correcto. Si utilizamos $b=0$ y $w=1$, al introducir $100$ la máquina responde $100$, pero debería responder $80$. Debemos cambiar $w$.

### Parámetros frente a datos

En este ejemplo $x=100$ es un **dato de entrada**, $y=80$ es la **respuesta objetivo**, y $w$ es un **parámetro**. Un parámetro es un número propio del modelo que el procedimiento de entrenamiento puede ajustar. Si hay un sesgo entrenable $b$, también es un parámetro.

Los valores pueden inicializarse con ceros o valores aleatorios cuidadosamente elegidos, según la arquitectura. Inicializar todos los pesos igual puede crear problemas de simetría en redes multicapa: distintas neuronas aprenderían comportamientos idénticos. Los métodos de inicialización buscan mantener señales y gradientes en escalas útiles.

### ¿Qué significa «entrenable»?

Un parámetro *entrenable* participa en las actualizaciones del optimizador. Otro puede quedar *congelado*: existe en el modelo y participa en los cálculos de salida, pero no cambia durante cierto entrenamiento. Esto se utiliza, por ejemplo, al adaptar solo una parte de un modelo previamente entrenado.

| Elemento | ¿Se ajusta con el entrenamiento? | Ejemplo |
|---|---|---|
| Peso entrenable | Sí | $w=0.2\rightarrow0.4$ |
| Sesgo entrenable | Sí | $b=-0.1\rightarrow0$ |
| Peso congelado | No durante esa fase | $w=0.7$ |
| Entrada | No es parámetro | $x=100$ |
| Hiperparámetro | Se configura por otro procedimiento | Tasa de aprendizaje $\eta=0.1$ |
| Activación | Se recalcula para cada entrada | Salida intermedia de una capa |
| Gradiente | Se calcula a partir de la pérdida | $\partial L/\partial w$ |

### Error y ajuste

Con $\hat y=wx$, una pérdida posible es $L=(\hat y-y)^2$. Si $x=1$, $y=2$ y $w=0$, $\hat y=0$ y $L=4$. Tras un paso de entrenamiento, el optimizador puede actualizar $w$ para reducir esa pérdida. El capítulo 7 muestra todas las operaciones numéricas.

### Entonces, ¿un parámetro guarda una respuesta?

No. En un modelo grande, cantidades inmensas de pesos contribuyen a las representaciones y transformaciones. Un peso individual no suele corresponder a «la capital de un país» o «la palabra perro». Por eso tampoco podemos contar los conocimientos de un modelo contando parámetros como si fueran fichas enciclopédicas.

### Parámetros, estado y memoria no son lo mismo

Si cierras una aplicación con IA, sus **pesos** pueden conservarse en archivos. Pero el historial de conversación podría estar en una base de datos externa. Además, durante el entrenamiento pueden guardarse gradientes o estados del optimizador en checkpoints. Cada cosa cumple una función distinta.

**Ejercicio.** En una red con 20 pesos, 5 sesgos y 3 valores de entrada, ¿cuántos parámetros existen si todos los pesos y sesgos son entrenables? **Solución:** $20+5=25$; las entradas no cuentan.

**Para reflexionar.** ¿Cambiar la temperatura de generación modifica los pesos del modelo? **Respuesta:** normalmente no; cambia cómo se seleccionan los tokens a partir de las predicciones.

**Siguiente:** [contaremos millones de parámetros](06-preentrenamiento.md).
