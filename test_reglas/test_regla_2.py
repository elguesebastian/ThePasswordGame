import unittest
from reglas.simbolo_y_numero import tiene_simbolo_y_numero


class TestReglas(unittest.TestCase):

    def test_regla2_valida(self):
        self.assertTrue(tiene_simbolo_y_numero("Password@1"))

    def test_regla2_invalida_sin_simbolo(self):
        self.assertFalse(tiene_simbolo_y_numero("Password1"))

    def test_regla2_invalida_sin_numero(self):
        self.assertFalse(tiene_simbolo_y_numero("Password@"))


if __name__ == "__main__":
    unittest.main()
