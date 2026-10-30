# 21. Cómo se almacena y ejecuta un modelo de IA

## Un archivo lleno de números puede convertirse en respuestas

Cuando se termina el entrenamiento, normalmente no guardamos un libro de todas las respuestas posibles: se conservan los **pesos** y la información necesaria para reconstruir sus operaciones. Un **motor de inferencia** interpreta esos datos y realiza cálculos para una entrada nueva.

### ¿Qué se almacena?

Según el sistema, pueden guardarse tensores de pesos, configuración de arquitectura, vocabulario, reglas de tokenización y metadatos. Un **checkpoint de entrenamiento** puede incluir además estados del optimizador para reanudar ajustes. No todos los archivos de pesos son intercambiables entre motores o arquitecturas.

### ¿Qué sucede al ejecutar?

1. La aplicación recibe una entrada.
2. El tokenizador o procesador la convierte a números.
3. Un motor compatible carga pesos y prepara memoria.
4. El procesador realiza multiplicaciones de matrices y otras operaciones.
5. Se calculan salidas y se devuelven a la aplicación.

Una CPU puede ejecutar esas operaciones de manera general. Una GPU dispone de gran paralelismo útil para muchos cálculos matriciales. Algunas NPU ofrecen aceleración especializada. La elección depende del dispositivo, la compatibilidad y las características del modelo.

### ¿Por qué importa la RAM?

Los pesos ocupan memoria, pero también hay activaciones temporales, buffers y a veces una **caché KV**. En modelos autoregresivos Transformer, esa caché permite reutilizar ciertas representaciones de claves y valores de tokens anteriores, evitando recalcular completamente todo en cada paso. Su tamaño crece con el contexto y depende de la arquitectura y precisión.

### Tamaño del archivo frente a memoria real

Si un modelo hipotético tiene $N=1\,000\,000$ pesos guardados en FP32, cada uno ocupa 4 bytes: aproximadamente 4 millones de bytes. Si se guarda a 16 bits, el tamaño básico de pesos baja a la mitad. Pero la memoria total de ejecución puede ser superior a ese cálculo y varía con el motor.

### ¿Qué mide «tokens por segundo»?

La cantidad de tokens generados por unidad de tiempo durante una fase de generación. No equivale necesariamente al tiempo de procesar un prompt largo, ni a la latencia de la primera respuesta. Es importante indicar hardware, configuración y condiciones si comparamos resultados.

**Ejercicio resuelto:** pesos hipotéticos de $500\,000$ elementos en FP32: $500\,000\times4=2\,000\,000$ bytes decimales. En FP16: $500\,000\times2=1\,000\,000$ bytes. Esto ignora otros requisitos.

**Siguiente:** [cuantización y precisión](22-cuantizacion.md).
