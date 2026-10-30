# 17. Tokens, embeddings y representaciones numéricas

## ¿Cómo entiende una computadora las palabras si calcula con números?

Escribe «Me gusta aprender». Tú ves letras y significado. Una red neuronal necesita transformar ese texto en estructuras numéricas que pueda procesar. El recorrido habitual es: **texto → tokens → identificadores → vectores → transformaciones matemáticas**.

### 1. Separar en tokens

Un tokenizador aplica reglas o un vocabulario aprendido para dividir texto en unidades. Una palabra puede corresponder a un token o a varios. Una segmentación inventada de «Hola, ¿cómo estás?» podría ser `Hola`, `,`, ` ¿`, `cómo`, ` estás`, `?`. **No es la tokenización universal:** diferentes modelos tienen diferentes vocabularios y estrategias.

¿Por qué utilizar fragmentos? Porque sería difícil disponer de un único token para cada palabra, nombre, terminación o expresión imaginable. Las unidades reutilizables ayudan a representar muchos textos.

### 2. Asignar IDs

Imagina un vocabulario hipotético:

| Token | ID |
|---|---:|
| gato | 101 |
| come | 102 |
| pescado | 103 |

«gato come pescado» se convierte en `[101,102,103]`. El ID es una etiqueta, no un significado matemático: 103 no es «más pescado» que 101.

### 3. Obtener embeddings

Cada identificador señala una fila en una tabla de representaciones aprendidas. Por ejemplo, el token `gato` podría tener el vector hipotético $[0.8,0.2,-0.4]$. Un **embedding** es ese conjunto ordenado de números. Las dimensiones son coordenadas en un espacio matemático, pero ningún eje universal tiene por qué significar «animal», «felicidad» o «precio».

Para vocabulario de $V$ tokens y dimensión $d$, una tabla de embeddings aprendidos tiene típicamente $V\times d$ elementos. Si $V=500$ y $d=4$, contiene $2000$ valores. En modelos más grandes, tanto vocabulario como dimensión pueden ser mayores.

### 4. Calcular relaciones entre vectores

El **producto escalar** multiplica componentes correspondientes y suma resultados. Para $\mathbf a=[1,2]$ y $\mathbf b=[2,1]$:

$$\mathbf a\cdot\mathbf b=1(2)+2(1)=4.$$

La **similitud coseno** divide el producto escalar por las longitudes de ambos vectores:

$$\cos\theta=\frac{\mathbf a\cdot\mathbf b}{\|\mathbf a\|\,\|\mathbf b\|}.$$

Como $\|\mathbf a\|=\|\mathbf b\|=\sqrt5$, la similitud es $4/5=0.8$. Dos vectores con orientación parecida tienen coseno cercano a 1. No debe interpretarse esa cercanía automáticamente como un juicio humano sobre el significado.

### 5. El contexto transforma representaciones

La palabra «banco» en «me senté en el banco» y «fui al banco a retirar dinero» puede terminar con representaciones internas diferentes cuando un modelo procesa la oración completa. El embedding inicial de un token es solo el comienzo: las capas posteriores combinan información contextual.

**Práctica.** Ejecuta `ejemplos/tokenizacion.py`, cambia el texto y observa la segmentación. Explica por qué el ejemplo no reproduce necesariamente un tokenizador de un LLM real.

**Ejercicio resuelto.** Para $\mathbf c=[3,0]$ y $\mathbf d=[0,2]$, el producto escalar es $0$, y la similitud coseno es $0$: los vectores son perpendiculares.

**Siguiente:** [cómo usa atención un Transformer](18-experimentos.md).
