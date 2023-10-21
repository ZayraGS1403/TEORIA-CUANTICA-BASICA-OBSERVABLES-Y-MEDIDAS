import unittest
import matplotlib.pyplot as plot
import numpy as np
import final as fin
import math

class TestSalto_Observables_Medidas(unittest.TestCase):
        def test_prob(self):
                v1 = [2-1j,2j,1-1j,1,-2j,2]
                pos = 3
                expect = 0.05
                real = fin.probabilidad(v1, pos)
                self.assertEqual(expect, real)
        def test_prob1(self):
                v1 = [-3-1j,-2j,1j,2]
                posci = 2
                expect = 0.05263157894736843
                real = fin.probabilidad(v1,posci)
                self.assertEqual(expect, real)

        def test_transicion(self):
                v1 = [1,-1j]
                v2 = [1j,1]
                expect = 0.9999999999999996
                real = fin.prob_transi(v1, v2)
                self.assertEqual(expect, real)
        def test_transicion_1(self):
                v1 = [(2/math.sqrt(2))*1j,-(2/math.sqrt(2))]
                v2 = [(2/math.sqrt(2)),(2/math.sqrt(2))*-1j]
                expect = 0
                real = fin.prob_transi(v1,v2)
                self.assertEqual(expect, real)

        def test_media(self):
                matrix = [[3,1+2j],[1-2j,-1]]
                ket = [math.sqrt(2)/2,(math.sqrt(2)/2)*-1]
                expect = 0
                real = fin.media(matrix, ket)
                self.assertEqual(expect, real)
        def test_media_1(self):
                matrix = [[1,-1j],[1j,2]]
                ket = [math.sqrt(2)/2,(math.sqrt(2)/2)*1j]
                expect = 2.5000000000000004
                real = fin.media(matrix, ket)
                self.assertEqual(expect, real)

        def test_varianza(self):
                matrix = [[3,1+2j],[1-2j,-1]]
                ket = [math.sqrt(2)/2,(math.sqrt(2)/2)*-1]
                expect = 8
                real = fin.varianza(matrix, ket)
                self.assertEqual(expect, real)
        def test_varianza_1(self):
                matrix = [[1,-1j],[1j,2]]
                ket = [math.sqrt(2)/2,(math.sqrt(2)/2)*1j]
                expect = 0.25
                real = fin.varianza(matrix, ket)
                self.assertEqual(expect, real)

        def test_val_prop(self):
                matrix = [[3, 1 + 2j], [1 - 2j, -1]]
                expect = "[ 4.+1.85037171e-17j -2.+9.25185854e-17j]"
                real = str(fin.val_prop(matrix))
                self.assertEqual(expect, real)
        def test_val_prop_1(self):
                matrix = [[1, 0], [0, -1]]
                expect = "[ 1. -1.]"
                real = str(fin.val_prop(matrix))
                self.assertEqual(expect, real)

        def test_transitar_a_vectores_propios(self):
                matrix = [[-1,-1j],[1j,1]]
                ket = [1/2,1/2]
                expect =[0.5, 0.5]
                real = fin.transitar_vect_prop(matrix,ket)
                self.assertEqual(expect, real)
        def test_transitar_a_vectores_propios_1(self):
                matrix = [[0, 1], [1, 0]]
                ket = [0, 1]
                expect =[0.5000000000000001, 0.5000000000000001]
                real = fin.transitar_vect_prop(matrix,ket)
                self.assertEqual(expect, real)

        def test_finalstate_2(self):
                seq = [[[0,1],[1,0]],[[(math.sqrt(2))/2,(math.sqrt(2))/2],[(math.sqrt(2))/2,-1*(math.sqrt(2))/2]]]
                ket = [1+6j,3-2j]
                expect = [(2.8284271247461903+2.8284271247461907j), (1.4142135623730954-5.656854249492381j)]
                real = fin.state(seq,ket)
                self.assertEqual(expect,real)
        def test_finalstate_1(self):
                seq = [[[(1 + 1j)/2, (1 - 1j)/2], [(1 - 1j)/2, (1 + 1j)/2]],[[1, 0], [0, 1j]]]
                ket = [1j, 2j]
                expect = [(0.5+1.5j), (-1.5-0.5j)]
                real = fin.state(seq,ket)
                self.assertEqual(expect, real)

if __name__ == "__main__":
        unittest.main()