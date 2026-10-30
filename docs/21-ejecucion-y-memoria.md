# 21. ¿Cómo se almacena y ejecuta un modelo?

## Del archivo a una respuesta

Un modelo no es un archivo mágico: es una arquitectura acompañada de tensores numéricos, metadatos y un programa que ejecuta operaciones. Al cargarlo, el motor lee los pesos, reserva memoria, prepara el contexto y repite multiplicaciones de matrices para producir tokens.

```mermaid
flowchart LR
  A[Archivo de pesos] --> B[Motor de inferencia]
  B --> C[RAM o VRAM]
  C --> D[Operaciones matriciales]
  D --> E[Logits y tokens]
  E --> F[Respuesta]
```

La memoria necesaria incluye pesos, activaciones temporales, buffers y, en un Transformer autoregresivo, la caché KV. Por eso el tamaño del archivo es una estimación y no siempre coincide con la RAM o VRAM usada.

## Un cálculo pequeño

Una matriz $W$ de $2 \times 3$ contiene seis números. Si se multiplica por un vector de tres entradas, el resultado tiene dos componentes: cada salida combina las tres entradas con su propia fila de pesos. Esta es la operación que se repite en capas grandes, con muchas optimizaciones de hardware.

## Aplicación y comprobación

El experimento `ejemplos/entrenar_modelo.py` guarda pesos en JSON, los carga y verifica que la predicción restaurada coincide. Preguntas: ¿qué diferencia hay entre almacenamiento y ejecución?, ¿por qué dos motores pueden usar distinta memoria con los mismos pesos?
