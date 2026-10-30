import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
from ejemplos.neurona import neurona
from ejemplos.contar_parametros import parametros_densa, parametros_red
from ejemplos.descenso_gradiente import paso
from ejemplos.entrenar_modelo import cargar, entrenar, guardar, predecir
from ejemplos.clasificador import clasificar
from ejemplos.modelo_lenguaje_pequeno import entrenar as entrenar_lenguaje, generar
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
        nuevo, _, _, perdida, _ = paso(1.0, 2.0, 4.0, 0.1)
        _, _, _, perdida_siguiente, _ = paso(nuevo, 2.0, 4.0, 0.1)
        self.assertLess(perdida_siguiente, perdida)

    def test_entrenamiento_checkpoint(self):
        modelo = entrenar([(0, 1), (1, 3), (2, 5)], epocas=30)
        ruta = Path(self._testMethodName + ".json")
        try:
            guardar(modelo, ruta)
            restaurado = cargar(ruta)
            self.assertAlmostEqual(predecir(modelo, 3), predecir(restaurado, 3))
        finally:
            ruta.unlink(missing_ok=True)

    def test_clasificador(self):
        self.assertEqual(clasificar(5), "corto")
        self.assertEqual(clasificar(30), "largo")

    def test_modelo_lenguaje(self):
        modelo = entrenar_lenguaje("abcabc")
        self.assertEqual(generar(modelo, "a", pasos=2), "abc")

    def test_softmax(self):
        valores = softmax([2.0, 1.0])
        self.assertAlmostEqual(sum(valores), 1.0)
        self.assertGreater(valores[0], valores[1])

    def test_agente_valida_herramienta(self):
        dato = ejecutar({"herramienta": "pronostico", "argumentos": {"ciudad": "X"}})
        self.assertEqual(dato["ciudad"], "X")


if __name__ == "__main__":
    unittest.main()
