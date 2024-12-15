import unittest
from reglas.colores import contiene_color


class TestReglas(unittest.TestCase):

    def test_regla3_valida(self):
        self.assertTrue(contiene_color("Passwordrojo"))

    def test_regla3_invalida_color_no_permitido(self):
        self.assertFalse(contiene_color("PasswordMarron"))

    def test_regla3_invalida_sin_color(self):
        self.assertFalse(contiene_color("PasswordNegro"))


if __name__ == "__main__":
    unittest.main()
