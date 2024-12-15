import unittest
from reglas.tres_repetidos import tiene_tres_caracteres_repetidos


class TestReglas(unittest.TestCase):

    def test_regla7_valida(self):
        self.assertTrue(tiene_tres_caracteres_repetidos("PasswordAAA"))

    def test_regla7_invalida(self):
        self.assertFalse(tiene_tres_caracteres_repetidos("PasswordAA"))


if __name__ == "__main__":
    unittest.main()
