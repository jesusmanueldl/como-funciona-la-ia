"""Softmax y temperatura usando Python estándar."""

import math

def softmax(logits, temperatura=1.0):
    ajustados = [z / temperatura for z in logits]
    m = max(ajustados)
    exp = [math.exp(z - m) for z in ajustados]
    total = sum(exp)
    return [v / total for v in exp]

if __name__ == "__main__":
    print([round(p, 3) for p in softmax([2.0, 1.0])])
    print([round(p, 3) for p in softmax([2.0, 1.0], temperatura=0.5)])
