import unittest
from reglas.numero_romano import contiene_numero_romano


class TestReglas(unittest.TestCase):

    def test_regla10_valida(self):
        self.assertTrue(contiene_numero_romano("PasswordXXVI"))

    def test_regla10_invalida_numero_romano_incorrecto(self):
        self.assertFalse(contiene_numero_romano("PasswordMXV"))

    def test_regla10_invalida_sin_numero_romano(self):
        self.assertFalse(contiene_numero_romano("Password"))


if __name__ == "__main__":
    unittest.main()
