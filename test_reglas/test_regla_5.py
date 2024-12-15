import unittest
from reglas.jugador_campeon import contiene_jugador_campeon


class TestReglas(unittest.TestCase):

    def test_regla5_valida(self):
        self.assertTrue(contiene_jugador_campeon("PasswordMessi"))

    def test_regla5_invalida(self):
        self.assertFalse(contiene_jugador_campeon("PasswordLanzini"))


if __name__ == "__main__":
    unittest.main()
