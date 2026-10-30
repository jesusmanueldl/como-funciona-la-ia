# 15. ¿Cómo entrenar un pequeño modelo de lenguaje?

Un modelo de lenguaje educativo puede aprender caracteres o tokens de un corpus pequeño con licencia adecuada. `ejemplos/modelo_lenguaje_pequeno.py` cuenta qué carácter suele seguir a otro y genera texto por la continuación más frecuente. Tiene vocabulario, secuencias, objetivo y generación, pero no es un Transformer ni un LLM de producción.

Un proyecto más completo separaría corpus, entrenamiento y prueba, guardaría un checkpoint y mediría pérdida. Los resultados limitados son parte del experimento: muestran que memorizar patrones locales no equivale a comprensión general.

## Razonamiento y límites

Un modelo puede producir pasos coherentes, resolver ciertos problemas y planificar secuencias. Eso describe una capacidad observable. No demuestra experiencia subjetiva, conciencia ni pensamiento humano.

El error puede aparecer como cálculo incorrecto, salto lógico o alucinación: una afirmación presentada con fluidez sin evidencia suficiente. Verificar, usar herramientas, pedir fuentes y dividir el problema reduce riesgos, pero no garantiza exactitud.

Conviene evaluar el resultado, no inferir una mente por el estilo del texto. La planificación de un agente es una conducta del sistema completo: modelo, memoria, herramientas, reglas y validadores.

Preguntas: ¿qué diferencia hay entre una explicación plausible y una demostración?, ¿por qué la fluidez no basta?, ¿qué comprobación independiente usarías?

[Siguiente →](16-ia-llm-agentes.md)
