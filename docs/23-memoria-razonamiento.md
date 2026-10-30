# 23. Memoria, conocimiento y razonamiento

Una respuesta puede usar varias fuentes de información que conviene separar:

- **Pesos:** regularidades ajustadas durante el entrenamiento.
- **Contexto:** texto presente en la solicitud.
- **Historial:** mensajes que una aplicación vuelve a incluir.
- **Memoria externa:** datos guardados fuera del modelo.
- **RAG:** recuperación de documentos para enriquecer el contexto.

Recordar una conversación no demuestra que los pesos hayan cambiado. Reentrenar modifica parámetros; recuperar un documento modifica la entrada disponible. Esa diferencia permite diseñar sistemas más auditables.

## ¿Razonar?

Un modelo puede producir pasos útiles, comparar alternativas o llamar herramientas. Eso es una capacidad observable del sistema, no una prueba de experiencia subjetiva. La planificación de un agente incluye modelo, memoria, reglas, herramientas y validadores.

## Comprobación

Para cada respuesta de un asistente pregunta: ¿estaba en los pesos, en el contexto, en una fuente recuperada o fue inferida? La respuesta no garantiza verdad: una fuente externa también puede estar equivocada y una cadena de pasos puede contener un error.
