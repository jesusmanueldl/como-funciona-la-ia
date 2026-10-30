# 13. Precisión numérica, cuantización y memoria

Bits codifican valores. FP32 usa 32 bits, FP16 16, BF16 conserva más rango con menos precisión, INT8 usa enteros de 8 bits y Q4 suele referirse a pesos de aproximadamente 4 bits con escalas auxiliares.

El tamaño teórico de pesos es:

$$
\text{bytes}
 = \frac{\text{parámetros} \times \text{bits por parámetro}}{8}.
$$

Para 1,000 millones a 16 bits:

$$
\begin{aligned}
1{,}000{,}000{,}000 \times \frac{16}{8}
  &= 2{,}000{,}000{,}000\ \text{bytes}.
\end{aligned}
$$

es decir, 2 GB decimales o aproximadamente 1.86 GiB antes de sobrecargas.

En la práctica se suman escalas, metadatos, activaciones, buffers y caché KV. Entrenar requiere gradientes y estados del optimizador; inferir requiere pesos, activaciones y caché. Cuantizar reduce memoria, pero puede degradar algunas salidas y el efecto depende del método y datos.

Preguntas: ¿por qué GB y GiB difieren?, ¿qué memoria se reutiliza entre tokens?, ¿por qué Q4 no significa exactamente cuatro bits para cada byte del archivo?

[Siguiente →](14-ejecucion-de-modelos.md)
