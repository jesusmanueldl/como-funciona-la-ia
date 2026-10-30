import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
from ejemplos.neurona import neurona
from ejemplos.contar_parametros import parametros_densa, parametros_red
from ejemplos.descenso_gradiente import paso
from ejemplos.probabilidades import softmax
from ejemplos.agente_simulado import ejecutar


class EjemplosTest(unittest.TestCase):
    def test_neurona(self):
        z, salida = neurona([2, 3], [0.5, -0.2], 0.1)
        self.assertAlmostEqual(z, 0.5)
        self.assertAlmostEqual(salida, 0.5)

    def test_parametros(self):
        self.assertEqual(parametros_densa(3, 4), 16)
        self.assertEqual(parametros_red([3, 4, 2]), 26)

    def test_descenso_reduce_error(self):
        nuevo, _, perdida = paso(1.0, 2.0, 4.0, 0.1)
        _, _, perdida_siguiente = paso(nuevo, 2.0, 4.0, 0.1)
        self.assertLess(perdida_siguiente, perdida)

    def test_softmax(self):
        valores = softmax([2.0, 1.0])
        self.assertAlmostEqual(sum(valores), 1.0)
        self.assertGreater(valores[0], valores[1])

    def test_agente_valida_herramienta(self):
        dato = ejecutar({"herramienta": "pronostico", "argumentos": {"ciudad": "X"}})
        self.assertEqual(dato["ciudad"], "X")


if __name__ == "__main__":
    unittest.main()
