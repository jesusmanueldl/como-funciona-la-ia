# 11. ¿Qué es un modelo parcialmente entrenado?

## Guardar la partida mientras aprendemos

Cuando juegas un videojuego, puedes guardar tu avance y continuar mañana. El entrenamiento de una red neuronal también puede conservar estados intermedios. Un **checkpoint** es una instantánea que permite guardar y, en ciertas condiciones, reanudar un entrenamiento.

### Un entrenamiento incompleto

Supongamos que planeamos 100 pasos de ajuste, pero nos detenemos en el 30. Tenemos un modelo entrenado parcialmente respecto al plan establecido. Puede que ya funcione algo; también puede que todavía prediga muy mal. «Parcialmente entrenado» no describe una arquitectura oficial ni garantiza calidad.

### ¿Qué guarda un checkpoint?

Depende de la implementación. Para **hacer inferencia** puede bastar con los pesos, la arquitectura y la información necesaria para preparar entradas. Para **reanudar fielmente** el entrenamiento también conviene guardar el estado del optimizador, el paso o época, el estado del generador aleatorio y cualquier configuración relevante.

```text
checkpoint ilustrativo
  pesos: {"w": 0.976}
  paso: 3
  optimizador: {...}
  configuración: {"tasa_aprendizaje": 0.1}
```

Este bloque solo muestra la idea: un checkpoint real puede contener muchos tensores binarios y metadatos.

### Cargar pesos no equivale a continuar exactamente

Si restauras solo $w=0.976$ en una regresión simple, puedes seguir calculando predicciones. Pero con optimizadores que mantienen momentos internos, como Adam, olvidar su estado puede cambiar la trayectoria de entrenamiento. Tampoco debes usar una copia de checkpoint como si estuviera evaluada en un conjunto de prueba independiente.

### Pasos, épocas y versiones

Un paso es una actualización del optimizador; una época representa, en términos generales, pasar una vez por el conjunto de entrenamiento. Para ciertos entrenamientos, como el de grandes modelos con datos de flujo, se describe progreso también mediante tokens procesados.

**Práctica:** ejecuta `ejemplos/entrenar_modelo.py` del repositorio y comprueba cómo guarda y restaura sus pesos. Si la salida restaurada difiere de la previa, investiga el formato o el redondeo.

**Ejercicio resuelto.** Un modelo empezó en $w=0$, tras tres pasos tiene $w=0.976$ y se detuvo. ¿Es preentrenado por esa razón? **No necesariamente:** solo sabemos que recibió tres actualizaciones. «Preentrenado» se refiere a una fase previa de aprendizaje, normalmente antes de la tarea final.

**Siguiente:** [entender qué significa preentrenamiento](12-memoria-y-contexto.md).
