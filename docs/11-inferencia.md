# 11. ¿Cómo genera una respuesta un LLM?

El flujo general es: prompt → tokenización → embeddings → capas → logits → probabilidades → selección → nuevo token → repetición.

Los logits `z_i` se convierten con softmax:

\[
P_i=\frac{e^{z_i}}{\sum_j e^{z_j}}.
\]

Con logits `[2,1]`, las probabilidades son aproximadamente `[0.73,0.27]`. La temperatura `T` modifica `z_i/T`: una temperatura menor concentra la distribución; una mayor la aplana. Greedy elige el máximo; top-k conserva k candidatos; top-p conserva el conjunto cuya masa acumulada alcanza p.

```mermaid
sequenceDiagram
  participant U as Usuario
  participant M as Modelo
  U->>M: Prompt
  M->>M: Tokens y capas
  M->>M: Probabilidades
  M-->>U: Un token
  M->>M: Repetir hasta detenerse
```

La variación puede provenir del muestreo, temperatura, contexto o estado del sistema. Predicción no es recuperación literal de respuestas almacenadas.

**Práctica:** ejecuta `ejemplos/probabilidades.py`. Preguntas: ¿qué ocurre con `T=0.5`?, ¿por qué un token probable puede ser falso?, ¿qué señal detiene la generación?

[Siguiente →](12-memoria-y-contexto.md)
