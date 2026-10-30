# 7. ¿Cómo aprende una máquina? Entrenamiento paso a paso

## Una calculadora que se equivoca y mejora

Queremos que una pequeña máquina aprenda a duplicar un número. Le enseñamos que $x=1$ debe producir $y=2$. Nuestro modelo elemental es $\hat y=wx$, donde $w$ es un peso inicialmente desconocido y $\hat y$ es lo que el modelo predice.

Si empezamos con $w=0$, el modelo predice $0$: todavía no sabe duplicar. ¿Cómo podemos orientarlo para acercarse a la respuesta correcta sin decirle directamente que $w=2$?

### Medir el error

Elegimos una pérdida cuadrática:

$$L=(\hat y-y)^2=(wx-y)^2.$$

Al principio, con $w=0$, $x=1$ y $y=2$:

$$L=(0\times1-2)^2=4.$$

La pérdida es un número que resume lo mal que salió la predicción **según la regla que elegimos**. No existe una única función de pérdida correcta para todos los problemas.

### Descubrir hacia dónde mover el peso

Necesitamos saber cómo cambia la pérdida si movemos ligeramente $w$. Una **derivada** mide esta sensibilidad. Para esta función:

$$\frac{\partial L}{\partial w}=2(wx-y)x.$$

La expresión $\partial L/\partial w$ significa «cómo cambia $L$ cuando cambia $w$». Con nuestros datos:

$$2(0\times1-2)(1)=-4.$$

El gradiente es negativo: aumentar $w$ un poco reduce inicialmente la pérdida. Utilizamos una **tasa de aprendizaje** $\eta=0.1$ para controlar el tamaño del cambio:

$$w_{\text{nuevo}}=w_{\text{anterior}}-\eta\frac{\partial L}{\partial w}.$$

Primer cambio: $w_1=0-0.1(-4)=0.4$.

### Tres iteraciones completas

| Paso | Peso inicial | Predicción | Pérdida | Gradiente | Peso nuevo |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.000 | 0.000 | 4.0000 | -4.000 | 0.400 |
| 2 | 0.400 | 0.400 | 2.5600 | -3.200 | 0.720 |
| 3 | 0.720 | 0.720 | 1.6384 | -2.560 | 0.976 |

En el segundo paso: $L=(0.4-2)^2=2.56$, gradiente $2(0.4-2)=-3.2$, nuevo peso $0.4-0.1(-3.2)=0.72$.

En el tercero: $L=(0.72-2)^2=1.6384$, gradiente $-2.56$, peso $0.976$. El peso sigue sin ser 2, pero se acerca.

### Del ejemplo pequeño al entrenamiento real

Las redes modernas reciben muchos ejemplos organizados en **lotes**. En cada paso calculan predicciones, pérdidas y gradientes para muchos parámetros. La **retropropagación** usa la regla de la cadena para obtener derivadas de las capas anteriores; un **optimizador** actualiza los pesos. Una **época** es un recorrido completo por el conjunto de entrenamiento, aunque no todos los sistemas de gran escala describen su progreso solo mediante épocas.

### ¿Aprendió de verdad?

El ejemplo ajusta un solo parámetro con una sola muestra; no prueba generalización. Un modelo útil debe evaluarse con ejemplos no utilizados para entrenar. Entrenamiento, validación y prueba cumplen objetivos diferentes. Veremos cómo separar los datos en el siguiente capítulo.

```python
w, x, y, eta = 0.0, 1.0, 2.0, 0.1
for paso in range(1, 4):
    pred = w*x
    perdida = (pred-y)**2
    grad = 2*(pred-y)*x
    nuevo = w-eta*grad
    print(paso, round(w,3), round(pred,3), round(perdida,4), round(grad,3), round(nuevo,3))
    w = nuevo
```

**Autoevaluación.** ¿Qué ocurriría si $\eta$ fuera demasiado grande? El entrenamiento podría oscilar o divergir. ¿Se modifican los pesos al ejecutar una predicción sin entrenamiento? Normalmente no.

**Siguiente:** [datos y conjuntos de evaluación](08-embeddings.md).
