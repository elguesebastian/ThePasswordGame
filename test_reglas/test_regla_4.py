import unittest
from reglas.suma_numeros import suma_mayor_20


class TestReglas(unittest.TestCase):

    def test_regla4_valida(self):
        self.assertTrue(suma_mayor_20("Password999"))

    def test_regla4_invalida_suma_menor_20(self):
        self.assertFalse(suma_mayor_20("Password5555"))

    def test_regla4_invalida_suma_exactamente_20(self):
        self.assertFalse(suma_mayor_20("Password95"))


if __name__ == "__main__":
    unittest.main()
