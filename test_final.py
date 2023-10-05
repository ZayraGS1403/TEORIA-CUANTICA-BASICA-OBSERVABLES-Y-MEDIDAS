import Lib2matrces as lib
import final as fil
import unittest
class TestMatrizOperations(unittest.TestCase):
    def test_prod_interno_dimension(self):
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        resultado = fil.prod_interno(v1, v2)
        self.assertEqual(resultado, 32, "El producto interno debe ser 32")
    def test_prod_interno_dimension(self):
        v1 = [2, 3]
        v2 = [1, 2]
        resultado = fil.prod_interno(v1, v2)
        self.assertEqual(resultado, "Tamaño errado", "'Tamaño errado'")

    def test_prob_transi_probabilidad(self):
        v1 = [1, 0, 0]
        v2 = [0, 1, 0]
        resultado = fil.prob_transi(v1, v2)
        self.assertEqual(resultado, 0.0, "La probabilidad de transición debe ser 0.0")
    def test_prob_transi_probabilidad(self):
        v1 = [1, 1, 0]
        v2 = [0, 1, 1]
        resultado = fil.prob_transi(v1, v2)
        self.assertAlmostEqual(resultado, 0.3333333333333333, places=6, msg="Probabilidad incorrecta")

    def test_media_matriz(self):
        matriz1 = [[1, 2], [2, 1]]
        ket1 = [1, 0]
        resultado = fil.media(matriz1, ket1)
        self.assertEqual(resultado, 2.0, "La media debe ser 2.0")
    def test_media_matriz(self):
        matriz2 = [[1, 2], [3, 4]]
        ket2 = [1, 1]
        resultado = fil.media(matriz2, ket2)
        self.assertEqual(resultado, "NO es hermitiana", "La matriz debe ser no hermitiana")

    def test_varianza_matriz_hermitiana(self):
        matriz3 = [[1, 0], [0, 1]]
        ket3 = [1, 0]
        resultado = fil.varianza(matriz3, ket3)
        self.assertEqual(resultado, 0.0, "La varianza debe ser 0.0")
    def test_varianza_matriz_no_hermitiana(self):
        matriz4 = [[1, 2], [2, 4]]
        ket4 = [1, 0]
        resultado = fil.varianza(matriz4, ket4)
        self.assertEqual(resultado, "NO es hermitiana", "La matriz debe ser no hermitiana")
