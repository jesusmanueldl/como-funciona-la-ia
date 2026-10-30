# 3. ¿Cómo funciona una neurona artificial?

## Una pequeña máquina que transforma números

Piensa en una báscula que calcula cuánto pagarás por fruta. Introduces los kilos, la máquina los multiplica por el precio y entrega el importe. Una neurona artificial es también una función que recibe números y produce números. Su diferencia no es que tenga deseos o pensamientos: **sus factores de multiplicación pueden ajustarse a partir de ejemplos**.

### De una entrada a una salida

Usamos la expresión $z=wx+b$. Si $x$ es la entrada, $w$ es un peso y $b$ un sesgo. La letra $z$ designa el resultado antes de una posible función de activación. Si $x=3$, $w=2$ y $b=1$, entonces:

$$
\begin{aligned}
z&=wx+b\\
 &=3(2)+1\\
 &=7.
\end{aligned}
$$

El peso controla cuánto influye la entrada; el sesgo desplaza el resultado. **Un peso negativo no es un error:** indica que al aumentar esa entrada, la contribución disminuye. Si usamos $w=-2$, $b=1$ y $x=3$, obtenemos $z=-5$.

### Varias entradas: una decisión basada en más de un dato

Imagina que un detector de mensajes usa dos características numéricas: $x_1$ = cantidad de enlaces y $x_2$ = cantidad de expresiones sospechosas. En lugar de una entrada:

$$z=w_1x_1+w_2x_2+b.$$

Si $x_1=2$, $x_2=3$, $w_1=0.5$, $w_2=-0.2$ y $b=0.1$:

$$
\begin{aligned}
z&=(0.5\times2)+(-0.2\times3)+0.1\\
 &=1-0.6+0.1\\
 &=0.5.
\end{aligned}
$$

**Atención:** los números no expresan un detector real; solo muestran la operación. En un sistema de clasificación no bastaría sumar: necesitamos interpretar o transformar la salida.

### Activaciones: por qué no basta con multiplicar y sumar

Una función de activación transforma $z$ en una salida $a=f(z)$. Un ejemplo es ReLU, cuyo nombre significa unidad lineal rectificada:

$$a=\operatorname{ReLU}(z)=\max(0,z).$$

Si $z=0.5$, la salida es $0.5$. Si $z=-5$, es $0$. Este cambio es importante: sin activaciones no lineales, apilar muchas capas densas lineales equivaldría a una sola transformación lineal, incluso si la red tuviera muchas capas.

Otros ejemplos son la función sigmoide, que transforma números en valores entre 0 y 1, y `tanh`, cuyo resultado está entre -1 y 1. El significado de una salida depende del objetivo de la red; no basta con interpretar cualquier número entre 0 y 1 como una probabilidad bien calibrada.

### ¿Cuántos parámetros contiene nuestra neurona?

Con dos entradas hay dos pesos y un sesgo: **tres parámetros entrenables**, si decidimos entrenarlos. Los valores de entrada no son parámetros. En el capítulo de entrenamiento veremos cómo cambian los pesos; aquí solo calculamos con los valores dados.

### Comprobación con Python

```python
entradas = [2.0, 3.0]
pesos = [0.5, -0.2]
sesgo = 0.1
z = sum(x*w for x,w in zip(entradas,pesos)) + sesgo
a = max(0.0,z)
print(z, a)  # 0.5 0.5
```

**Ejercicio 1.** Cambia $w_2$ a $0.2$. ¿Cuánto valen $z$ y $a$? **Solución:** $z=1+0.6+0.1=1.7$ y ReLU devuelve $1.7$.

**Ejercicio 2.** Para $x=4$, $w=-1$, $b=2$, calcula ReLU. **Solución:** $z=-4+2=-2$, luego $a=0$.

**Error habitual:** llamar «conocimiento» a cada peso individual. Las representaciones útiles surgen de relaciones entre muchos valores, no de un diccionario escondido en cada número.

**Lo siguiente:** conectaremos muchas neuronas y veremos cómo sus cálculos forman una red.
