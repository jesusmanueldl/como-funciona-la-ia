# 18. ¿Cómo funciona un Transformer?

Antes de la ecuación, la pregunta es qué información de otras posiciones necesita cada token. Self-attention calcula consultas, claves y valores; una máscara causal impide mirar tokens futuros. Después aparecen atención multicabeza, capas feed-forward, normalización y conexiones residuales. Existen variantes y no todos los Transformers se usan igual.

La atención escalada es:

$$
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^{\mathsf{T}}}{\sqrt{d_k}}\right)V.
$$

La raíz estabiliza la escala de los productos; softmax convierte puntuaciones en pesos. Un cálculo pequeño con dos puntuaciones puede verificarse mediante `ejemplos/probabilidades.py`.

## Experimentos prácticos

Todos los ejemplos funcionan con Python estándar:

1. `neurona.py`: pesos, sesgo y ReLU.
2. `contar_parametros.py`: capas densas y red multicapa.
3. `descenso_gradiente.py`: tres iteraciones reproducibles y tabla de campos.
4. `entrenar_modelo.py`: entrenamiento, checkpoint y restauración.
5. `clasificador.py`: clasificación de una característica.
6. `tokenizacion.py`: tokenización pedagógica, no universal.
7. `modelo_lenguaje_pequeno.py`: corpus de caracteres y generación.
8. `probabilidades.py`: softmax y temperatura.
9. `agente_simulado.py`: herramientas ficticias, validación y permisos.
10. `entrenar_pytorch.py`: versión opcional con PyTorch.

Ejecuta:

```bash
python -m unittest discover -s tests -v
```

Los experimentos son modelos didácticos: no entrenan un LLM real ni sustituyen un motor de producción.

[Siguiente →](19-preguntas-frecuentes.md)
