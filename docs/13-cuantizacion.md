# 13. Ajuste fino, transferencia de aprendizaje y LoRA

## ¿Es necesario reentrenar todos los números?

Imagina un modelo que ya aprendió a procesar textos generales. Ahora queremos que clasifique reseñas de productos. Podríamos entrenar una red nueva desde cero, pero también podemos **ajustar** el modelo existente con ejemplos apropiados para la nueva tarea.

### Ajuste fino completo

En el **fine-tuning completo** se permiten actualizaciones en todos o en gran parte de los parámetros del modelo. Esto ofrece flexibilidad, pero puede exigir bastante memoria y cómputo. También existe el riesgo de degradar capacidades útiles si los datos o el procedimiento son deficientes.

### Congelar componentes

Otra posibilidad es conservar fijos los pesos de una parte del modelo y entrenar solo una capa de salida. Si el modelo tiene $1\,000\,000$ parámetros y solo $10\,000$ son entrenables, el optimizador actualiza esos $10\,000$; los otros siguen participando en el cálculo de la salida.

### LoRA con una matriz pequeña

LoRA (*Low-Rank Adaptation*) agrega una corrección entrenable a determinadas matrices existentes. En una configuración simplificada:

$$W'=W+BA,$$

con $W$ congelada, $A$ de forma $r\times d_{\text{in}}$ y $B$ de forma $d_{\text{out}}\times r$. En lugar de entrenar todos los $d_{\text{out}}d_{\text{in}}$ elementos de $W$, se entrenan:

$$P_{\text{LoRA}}=r(d_{\text{in}}+d_{\text{out}}).$$

Ejemplo: si $W$ mide $1000\times1000$, tiene un millón de valores. Con rango $r=8$, las dos matrices LoRA tienen $8(1000+1000)=16\,000$ parámetros. Es una reducción grande **para esta matriz y configuración**, sin afirmar que todo el sistema tenga únicamente 16 000 parámetros.

### ¿Qué es QLoRA?

Es una estrategia que combina adaptadores de rango bajo con almacenamiento cuantizado de pesos base para reducir necesidades de memoria durante ciertos ajustes. No significa que los parámetros aprendidos se conviertan mágicamente en un modelo mejor ni que siempre resulte apropiada.

### ¿Cuál opción elegir?

| Estrategia | Qué se modifica | Uso habitual |
|---|---|---|
| Desde cero | Pesos inicializados para la tarea | Modelos educativos o necesidades especiales |
| Capa de salida | Solo una pequeña parte | Clasificación con representación previa |
| Fine-tuning completo | Muchos o todos los pesos | Adaptación con suficientes recursos |
| LoRA | Adaptadores seleccionados | Adaptación eficiente |

**Práctica numérica.** Para una matriz $512\times256$ y rango LoRA $r=4$: matriz original $131\,072$ pesos; adaptadores $4(512+256)=3\,072$ parámetros. Calcula el porcentaje y explica que este conteo excluye otros componentes.

**Error frecuente:** fine-tuning no es lo mismo que agregar documentos a un buscador RAG. El primero cambia parámetros; el segundo recupera información externa durante la consulta.

**Siguiente:** [entrenar un modelo propio](14-ejecucion-de-modelos.md).
