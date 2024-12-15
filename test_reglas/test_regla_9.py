import unittest
from reglas.color_hex import contiene_color_hex


class TestReglas(unittest.TestCase):

    def test_regla9_valida(self):
        self.assertTrue(contiene_color_hex("Password#000000"))

    def test_regla9_invalida_formato_incorrecto(self):
        self.assertFalse(contiene_color_hex("Password#00f0ff"))

    def test_regla9_invalida_sin_color_hex(self):
        self.assertFalse(contiene_color_hex("PasswordTexto"))


if __name__ == "__main__":
    unittest.main()
