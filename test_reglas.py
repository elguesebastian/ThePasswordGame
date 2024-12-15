import unittest
from reglas.mas_8_y_mayuscula import tiene_ocho_y_mayuscula
from reglas.simbolo_y_numero import tiene_simbolo_y_numero
from reglas.colores import contiene_color
from reglas.suma_numeros import suma_mayor_20
from reglas.jugador_campeon import contiene_jugador_campeon
from reglas.mes_año import contiene_mes
from reglas.tres_repetidos import tiene_tres_caracteres_repetidos
from reglas.acertijo_numero import contiene_numero_acertijo
from reglas.color_hex import contiene_color_hex
from reglas.numero_romano import contiene_numero_romano
from reglas.principio_y_fin import tiene_principio_y_fin


class TestReglas(unittest.TestCase):

    # Regla 1
    def test_regla1_valida(self):
        self.assertTrue(tiene_ocho_y_mayuscula("Password1"))

    def test_regla1_invalida_menos_caracteres(self):
        self.assertFalse(tiene_ocho_y_mayuscula("Pass1"))

    def test_regla1_invalida_sin_mayusculas(self):
        self.assertFalse(tiene_ocho_y_mayuscula("password1"))

    # Regla 2

    def test_regla2_valida(self):
        self.assertTrue(tiene_simbolo_y_numero("Password@1"))

    def test_regla2_invalida_sin_simbolo(self):
        self.assertFalse(tiene_simbolo_y_numero("Password1"))

    def test_regla2_invalida_sin_numero(self):
        self.assertFalse(tiene_simbolo_y_numero("Password@"))

    # Regla 3

    def test_regla3_valida(self):
        self.assertTrue(contiene_color("Passwordrojo"))

    def test_regla3_invalida_color_no_permitido(self):
        self.assertFalse(contiene_color("PasswordMarron"))

    def test_regla3_invalida_sin_color(self):
        self.assertFalse(contiene_color("PasswordNegro"))

    # Regla 4

    def test_regla4_valida(self):
        self.assertTrue(suma_mayor_20("Password999"))

    def test_regla4_invalida_suma_menor_20(self):
        self.assertFalse(suma_mayor_20("Password5555"))

    def test_regla4_invalida_suma_exactamente_20(self):
        self.assertFalse(suma_mayor_20("Password95"))

    # Regla 5

    def test_regla5_valida(self):
        self.assertTrue(contiene_jugador_campeon("PasswordMessi"))

    def test_regla5_invalida(self):
        self.assertFalse(contiene_jugador_campeon("PasswordLanzini"))

    # Regla 6

    def test_regla6_valida(self):
        self.assertTrue(contiene_mes("PasswordMayo"))

    def test_regla6_invalida(self):
        self.assertFalse(contiene_mes("Password"))

    # Regla 7

    def test_regla7_valida(self):
        self.assertTrue(tiene_tres_caracteres_repetidos("PasswordAAA"))

    def test_regla7_invalida(self):
        self.assertFalse(tiene_tres_caracteres_repetidos("PasswordAA"))

    # Regla 8

    def test_regla8_valida(self):
        self.assertTrue(contiene_numero_acertijo("Password5"))

    def test_regla8_invalida(self):
        self.assertFalse(contiene_numero_acertijo("Password3"))

    # Regla 9

    def test_regla9_valida(self):
        self.assertTrue(contiene_color_hex("Password#000000"))

    def test_regla9_invalida_formato_incorrecto(self):
        self.assertFalse(contiene_color_hex("Password#00f0ff"))

    def test_regla9_invalida_sin_color_hex(self):
        self.assertFalse(contiene_color_hex("PasswordTexto"))

    # Regla 10

    def test_regla10_valida(self):
        self.assertTrue(contiene_numero_romano("PasswordXXVI"))

    def test_regla10_invalida_numero_romano_incorrecto(self):
        self.assertFalse(contiene_numero_romano("PasswordMXV"))

    def test_regla10_invalida_sin_numero_romano(self):
        self.assertFalse(contiene_numero_romano("Password"))

    # Regla 11

    def test_regla11_valida(self):
        self.assertTrue(tiene_principio_y_fin("1PasswordF"))

    def test_regla11_invalida_solo_numero_inicio(self):
        self.assertFalse(tiene_principio_y_fin("Password1"))

    def test_regla11_invalida_sin_caracteres_inicio_fin(self):
        self.assertFalse(tiene_principio_y_fin("Password"))

if __name__ == "__main__":
    unittest.main()