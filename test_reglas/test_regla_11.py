import unittest
from reglas.principio_y_fin import tiene_principio_y_fin


class TestReglas(unittest.TestCase):

    def test_regla11_valida(self):
        self.assertTrue(tiene_principio_y_fin("1PasswordF"))

    def test_regla11_invalida_solo_numero_inicio(self):
        self.assertFalse(tiene_principio_y_fin("Password1"))

    def test_regla11_invalida_sin_caracteres_inicio_fin(self):
        self.assertFalse(tiene_principio_y_fin("Password"))


if __name__ == "__main__":
    unittest.main()
