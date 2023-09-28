import unittest
import probacilidad as pro
import math
class TestSalto_Observables_Medidas(unittest.TestCase):
    def test_prob_2(self):
        v1 = [2 - 1j, 2j, 1 - 1j, 1, -2j, 2]
        pos = 3
        actual = 0.05
        expect = pro.probabilidad(v1, pos)
        self.assertEqual(actual, expect)

    def test_prob_1(self):
        v1 = [-3 - 1j, -2j, 1j, 2]
        pos = 2
        actual = 0.05263157894736843
        expect = pro.probabilidad(v1, pos)
        self.assertEqual(actual, expect)

    def test_transicion_2(self):
        v1 = [1, -1j]
        v2 = [1j, 1]
        actual = 0.9999999999999996
        expect = pro.prob_transi(v1, v2)
        self.assertEqual(actual, expect)

    def test_transicion_1(self):
        v1 = [(2 / math.sqrt(2)) * 1j, -(2 / math.sqrt(2))]
        v2 = [(2 / math.sqrt(2)), (2 / math.sqrt(2)) * -1j]
        actual = 0
        expect = pro.prob_transi(v1, v2)
        self.assertEqual(actual, expect)

