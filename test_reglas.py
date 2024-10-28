import unittest
from reglas import regla1, regla2, regla3, regla4, regla5, regla6


class TestReglas(unittest.TestCase):

    def test_regla1(self):
        self.assertTrue(regla1("Password1"))
        self.assertFalse(regla1("Pass1"))
        self.assertFalse(regla1("password1"))

    def test_regla2(self):
        self.assertTrue(regla2("Password@1"))
        self.assertFalse(regla2("Password1"))
        self.assertFalse(regla2("Password@"))

    def test_regla3(self):
        self.assertTrue(regla3("Password999"))
        self.assertFalse(regla3("Password5555"))
        self.assertFalse(regla3("Password95"))

    def test_regla4(self):
        self.assertTrue(regla4("PasswordMessi"))
        self.assertFalse(regla4("PasswordLanzini"))

    def test_regla5(self):
        self.assertTrue(regla5("PasswordAAA"))
        self.assertFalse(regla5("PasswordAA"))

    def test_regla6(self):
        self.assertTrue(regla6("Password5"))
        self.assertFalse(regla6("Password3"))


if __name__ == "__main__":
    unittest.main()
