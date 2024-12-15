import unittest
from reglas.mes_año import contiene_mes


class TestReglas(unittest.TestCase):

    def test_regla6_valida(self):
        self.assertTrue(contiene_mes("PasswordMayo"))

    def test_regla6_invalida(self):
        self.assertFalse(contiene_mes("Password"))


if __name__ == "__main__":
    unittest.main()
