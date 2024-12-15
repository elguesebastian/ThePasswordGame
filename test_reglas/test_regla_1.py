import unittest
from reglas.mas_8_y_mayuscula import tiene_ocho_y_mayuscula


class TestReglas(unittest.TestCase):

    def test_valida(self):
        self.assertTrue(tiene_ocho_y_mayuscula("Password1"))

    def test_invalida_menos_caracteres(self):
        self.assertFalse(tiene_ocho_y_mayuscula("Pass1"))

    def test_invalida_sin_mayusculas(self):
        self.assertFalse(tiene_ocho_y_mayuscula("password1"))


if __name__ == "__main__":
    unittest.main()
