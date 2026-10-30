"""Versión opcional de la regresión lineal con PyTorch.

Se ejecuta solo si PyTorch está instalado: python ejemplos/entrenar_pytorch.py
"""

try:
    import torch
except ImportError as exc:  # pragma: no cover - dependencia opcional
    raise SystemExit("Instala PyTorch para ejecutar este ejemplo opcional.") from exc

x = torch.tensor([[0.0], [1.0], [2.0]])
y = torch.tensor([[1.0], [3.0], [5.0]])
modelo = torch.nn.Linear(1, 1)
optimizador = torch.optim.SGD(modelo.parameters(), lr=0.1)

for _ in range(200):
    perdida = torch.mean((modelo(x) - y) ** 2)
    optimizador.zero_grad()
    perdida.backward()
    optimizador.step()

ruta = "/tmp/ia-modelo-pytorch.pt"
torch.save(modelo.state_dict(), ruta)
restaurado = torch.nn.Linear(1, 1)
restaurado.load_state_dict(torch.load(ruta, weights_only=True))
print("predicción restaurada:", round(restaurado(torch.tensor([[3.0]])).item(), 3))
