import unittest
from reglas.mas_8_y_mayuscula import tiene_ocho_y_mayuscula
from reglas.simbolo_y_numero import tiene_simbolo_y_numero
from reglas.suma_numeros import suma_mayor_20
from reglas.jugador_campeon import contiene_jugador_campeon
from reglas.mes_año import contiene_mes
from reglas.tres_repetidos import tiene_tres_caracteres_repetidos
from reglas.acertijo_numero import contiene_numero_acertijo
from reglas.color_hex import contiene_color_hex
from reglas.numero_romano import contiene_numero_romano


class TestReglas(unittest.TestCase):

    def test_regla1(self):
        self.assertTrue(tiene_ocho_y_mayuscula("Password1"))
        self.assertFalse(tiene_ocho_y_mayuscula("Pass1"))
        self.assertFalse(tiene_ocho_y_mayuscula("password1"))

    def test_regla2(self):
        self.assertTrue(tiene_simbolo_y_numero("Password@1"))
        self.assertFalse(tiene_simbolo_y_numero("Password1"))
        self.assertFalse(tiene_simbolo_y_numero("Password@"))

    def test_regla3(self):
        self.assertTrue(suma_mayor_20("Password999"))
        self.assertFalse(suma_mayor_20("Password5555"))
        self.assertFalse(suma_mayor_20("Password95"))

    def test_regla4(self):
        self.assertTrue(contiene_jugador_campeon("PasswordMessi"))
        self.assertFalse(contiene_jugador_campeon("PasswordLanzini"))

    def test_regla5(self):
        self.assertTrue(contiene_mes("PasswordMayo"))
        self.assertFalse(contiene_mes("Password"))

    def test_regla6(self):
        self.assertTrue(tiene_tres_caracteres_repetidos("PasswordAAA"))
        self.assertFalse(tiene_tres_caracteres_repetidos("PasswordAA"))

    def test_regla7(self):
        self.assertTrue(contiene_numero_acertijo("Password5"))
        self.assertFalse(contiene_numero_acertijo("Password3"))

    def test_regla8(self):
        self.assertTrue(contiene_color_hex("Password#000000"))
        self.assertFalse(contiene_color_hex("Password#00f0ff"))

    def test_regla9(self):
        self.assertTrue(contiene_numero_romano("PasswordXXVI"))
        self.assertFalse(contiene_numero_romano("PasswordMXV"))


if __name__ == "__main__":
    unittest.main()
