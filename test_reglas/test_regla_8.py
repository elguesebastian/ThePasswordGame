import unittest
from reglas.acertijo_numero import contiene_numero_acertijo


class TestReglas(unittest.TestCase):

    def test_regla8_valida(self):
        self.assertTrue(contiene_numero_acertijo("Password5"))

    def test_regla8_invalida(self):
        self.assertFalse(contiene_numero_acertijo("Password3"))


if __name__ == "__main__":
    unittest.main()
