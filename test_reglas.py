import unittest
from reglas import regla1, regla2, regla3, regla4, regla5, regla6

class TestReglas(unittest.TestCase):

    def test_regla1(self):
        # Contraseña válida: más de 8 caracteres y al menos una mayúscula
        self.assertTrue(regla1("Password1"))
        # Contraseña inválida: menos de 8 caracteres
        self.assertFalse(regla1("Pass1"))
        # Contraseña inválida: no tiene mayúsculas
        self.assertFalse(regla1("password1"))

    def test_regla2(self):
        # Contraseña válida: tiene un símbolo y un número
        self.assertTrue(regla2("Password@1"))
        # Contraseña inválida: no tiene símbolos
        self.assertFalse(regla2("Password1"))
        # Contraseña inválida: no tiene números
        self.assertFalse(regla2("Password@"))

    def test_regla3(self):
        # Contraseña válida: la suma de los números es mayor a 20
        self.assertTrue(regla3("Password999"))
        # Contraseña inválida: la suma de los números es igual a 20
        self.assertFalse(regla3("Password5555"))
        # Contraseña inválida: la suma de los números es menor a 20
        self.assertFalse(regla3("Password95"))

    def test_regla4(self):
        # Contraseña válida: contiene el apellido de un campeón
        self.assertTrue(regla4("PasswordMessi"))
        # Contraseña inválida: no contiene apellidos de campeones
        self.assertFalse(regla4("PasswordLanzini"))

    def test_regla5(self):
        # Contraseña válida: contiene tres letras iguales seguidas
        self.assertTrue(regla5("PasswordAAA"))
        # Contraseña inválida: no tiene tres letras iguales seguidas
        self.assertFalse(regla5("PasswordAA"))

    def test_regla6(self):
        # Contraseña válida: contiene el número '5'
        self.assertTrue(regla6("Password5"))
        # Contraseña inválida: no contiene el número '5'
        self.assertFalse(regla6("Password3"))

if __name__ == "__main__":
    unittest.main()
