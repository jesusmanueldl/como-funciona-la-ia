# 12. Memoria, contexto y conocimiento

Hay varias cosas llamadas “memoria”:

- pesos: patrones incorporados durante entrenamiento;
- contexto: texto temporal enviado en una solicitud;
- historial: contexto acumulado por una aplicación;
- base de datos: información externa persistente;
- RAG: recuperar documentos y añadirlos al contexto.

Un sistema RAG puede indexar documentos, buscar fragmentos relevantes y dárselos al modelo. Eso puede mejorar actualidad y trazabilidad sin modificar pesos. También introduce problemas: documentos incompletos, permisos, inyección de instrucciones y recuperación equivocada.

Recordar una conversación no demuestra que el modelo haya aprendido mediante actualización de parámetros. La ventana de contexto limita cuánto texto puede procesarse en una solicitud.

Actividad: diseña un flujo que almacene preferencias en una tabla, recupere solo las autorizadas y las incluya con una marca de fuente.

[Siguiente →](13-cuantizacion.md)
