# 8. ¿De dónde obtiene los datos una IA?

## Aprender con ejemplos: la importancia del cuaderno de ejercicios

Si quieres enseñar a un sistema a distinguir mensajes legítimos de spam, necesitas ejemplos representativos. Una **observación** podría ser un mensaje; su **etiqueta** podría ser «spam» o «no spam». Pero los datos no garantizan aprendizaje útil: pueden contener errores, repeticiones o prejuicios.

### Construimos un conjunto diminuto

| Texto | Etiqueta |
|---|---|
| «Gana un premio ahora» | spam |
| «Nos vemos a las 5» | no spam |
| «Haz clic para cobrar» | spam |
| «Adjunto las notas de clase» | no spam |

Un modelo entrenado solamente con cuatro mensajes puede memorizar coincidencias y fallar con expresiones nuevas. Por ejemplo, «La clase recibió un premio» contiene «premio» pero no tiene que ser spam. **Generalizar** es responder bien ante casos nuevos, no repetir ejemplos vistos.

### Entrenar, validar y probar no es lo mismo

- **Entrenamiento:** ejemplos que se usan para ajustar los parámetros.
- **Validación:** ejemplos que ayudan a elegir configuraciones, controlar el progreso y comparar alternativas.
- **Prueba:** ejemplos reservados para estimar rendimiento al final, sin usarlos para decidir ajustes.

Si tienes 100 ejemplos, una partición ilustrativa podría ser 70/15/15. No es una ley universal. El reparto depende del problema y del tamaño de los datos; en series temporales hay que respetar el tiempo, y en datos de personas conviene impedir que el mismo individuo aparezca indebidamente en entrenamiento y prueba.

### Contaminación y fugas

Supongamos que copias el mismo mensaje, con pequeñas variaciones, a entrenamiento y prueba. El modelo puede parecer excelente sin haber aprendido patrones generalizables. Esto es una **fuga de datos**. También ocurre si usamos información que en el momento real de hacer una predicción todavía no estaría disponible.

### Datos sin etiquetas

No todas las tareas requieren que una persona escriba la respuesta correcta para cada ejemplo. El aprendizaje **autosupervisado** construye objetivos desde los propios datos; por ejemplo, predecir un token oculto o el siguiente token de un texto. Esto permite aprovechar grandes cantidades de material, pero también exige calidad, derechos de uso y precauciones de privacidad.

### ¿De dónde pueden venir los datos?

De mediciones, registros propios, colecciones públicas, textos con permiso, simulaciones o datos creados artificialmente. Que una página esté disponible en Internet no significa automáticamente que podamos usarla sin revisar licencias, restricciones, privacidad y condiciones aplicables.

**Práctica guiada.** Construye 12 mensajes ficticios, etiqueta los mensajes y separa al menos 3 para prueba. Escribe por qué no debes cambiar tus reglas de clasificación después de mirar los resultados de prueba.

**Ejercicio resuelto.** Si 12 ejemplos se dividen en 8 de entrenamiento, 2 de validación y 2 de prueba, ¿cuántos sirven para ajustar directamente parámetros? **Ocho.** Los otros cuatro cumplen funciones distintas.

**Error frecuente:** confundir cantidad con calidad. Un conjunto enorme y sesgado puede producir un sistema que falla sistemáticamente para algunos grupos o situaciones.

**Siguiente:** [diferentes formas de aprender](09-transformers.md).
