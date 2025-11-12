"""
Pruebas unitarias para las operaciones de la calculadora.
"""
import unittest
import sys
import os

# Agregar el directorio padre al path para importar el módulo calculadora
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from calculadora.operaciones import Calculadora

class TestCalculadora(unittest.TestCase):
    """Caso de prueba para la clase Calculadora."""
    
    def test_suma_numeros_positivos(self):
        """Prueba la suma con números positivos."""
        self.assertEqual(Calculadora.suma(5, 3), 8)
        self.assertEqual(Calculadora.suma(2.5, 3.5), 6.0)
    
    def test_suma_numeros_negativos(self):
        """Prueba la suma con números negativos."""
        self.assertEqual(Calculadora.suma(-5, -3), -8)
        self.assertEqual(Calculadora.suma(-2.5, 3.5), 1.0)
    
    def test_suma_cadenas_validas(self):
        """Prueba la suma con cadenas que representan números."""
        self.assertEqual(Calculadora.suma("5", "3"), 8)
        self.assertEqual(Calculadora.suma("2.5", "3.5"), 6.0)
    
    def test_suma_cadenas_invalidas(self):
        """Prueba que la suma lance error con cadenas inválidas."""
        with self.assertRaises(ValueError):
            Calculadora.suma("abc", 3)
        with self.assertRaises(ValueError):
            Calculadora.suma(5, "xyz")
    
    def test_resta_numeros_positivos(self):
        """Prueba la resta con números positivos."""
        self.assertEqual(Calculadora.resta(5, 3), 2)
        self.assertEqual(Calculadora.resta(3, 5), -2)
    
    def test_resta_numeros_negativos(self):
        """Prueba la resta con números negativos."""
        self.assertEqual(Calculadora.resta(-5, -3), -2)
        self.assertEqual(Calculadora.resta(-2.5, 3.5), -6.0)
    
    def test_resta_cadenas_invalidas(self):
        """Prueba que la resta lance error con cadenas inválidas."""
        with self.assertRaises(ValueError):
            Calculadora.resta("abc", 3)
    
    def test_multiplicacion_numeros_positivos(self):
        """Prueba la multiplicación con números positivos."""
        self.assertEqual(Calculadora.multiplicacion(5, 3), 15)
        self.assertEqual(Calculadora.multiplicacion(2.5, 4), 10.0)
    
    def test_multiplicacion_por_cero(self):
        """Prueba la multiplicación por cero."""
        self.assertEqual(Calculadora.multiplicacion(5, 0), 0)
        self.assertEqual(Calculadora.multiplicacion(0, 3.5), 0)
    
    def test_multiplicacion_cadenas_invalidas(self):
        """Prueba que la multiplicación lance error con cadenas inválidas."""
        with self.assertRaises(ValueError):
            Calculadora.multiplicacion("abc", 3)
    
    def test_division_numeros_positivos(self):
        """Prueba la división con números positivos."""
        self.assertEqual(Calculadora.division(6, 3), 2)
        self.assertEqual(Calculadora.division(5, 2), 2.5)
    
    def test_division_por_cero(self):
        """Prueba que la división por cero lance error."""
        with self.assertRaises(ValueError) as contexto:
            Calculadora.division(5, 0)
        self.assertEqual(str(contexto.exception), "No se puede dividir entre cero")
    
    def test_division_cadenas_invalidas(self):
        """Prueba que la división lance error con cadenas inválidas."""
        with self.assertRaises(ValueError):
            Calculadora.division("abc", 3)
    
    def test_potencia_numeros_positivos(self):
        """Prueba la potencia con números positivos."""
        self.assertEqual(Calculadora.potencia(2, 3), 8)
        self.assertEqual(Calculadora.potencia(5, 2), 25)
    
    def test_potencia_exponente_cero(self):
        """Prueba la potencia con exponente cero."""
        self.assertEqual(Calculadora.potencia(5, 0), 1)
    
    def test_potencia_cadenas_invalidas(self):
        """Prueba que la potencia lance error con cadenas inválidas."""
        with self.assertRaises(ValueError):
            Calculadora.potencia("abc", 3)
    
    def test_raiz_cuadrada_numeros_positivos(self):
        """Prueba la raíz cuadrada con números positivos."""
        self.assertEqual(Calculadora.raiz_cuadrada(9), 3)
        self.assertEqual(Calculadora.raiz_cuadrada(16), 4)
    
    def test_raiz_cuadrada_numero_negativo(self):
        """Prueba que la raíz cuadrada de número negativo lance error."""
        with self.assertRaises(ValueError) as contexto:
            Calculadora.raiz_cuadrada(-9)
        self.assertEqual(str(contexto.exception), "No se puede calcular la raíz cuadrada de un número negativo")
    
    def test_raiz_cuadrada_cadena_invalida(self):
        """Prueba que la raíz cuadrada lance error con cadena inválida."""
        with self.assertRaises(ValueError):
            Calculadora.raiz_cuadrada("abc")
    
    def test_porcentaje_numeros_positivos(self):
        """Prueba el cálculo de porcentaje con números positivos."""
        self.assertEqual(Calculadora.porcentaje(50, 200), 25)
        self.assertEqual(Calculadora.porcentaje(25, 100), 25)
    
    def test_porcentaje_divisor_cero(self):
        """Prueba que el porcentaje con divisor cero lance error."""
        with self.assertRaises(ValueError) as contexto:
            Calculadora.porcentaje(50, 0)
        self.assertEqual(str(contexto.exception), "El divisor no puede ser cero para calcular porcentaje")
    
    def test_porcentaje_cadenas_invalidas(self):
        """Prueba que el porcentaje lance error con cadenas inválidas."""
        with self.assertRaises(ValueError):
            Calculadora.porcentaje("abc", 100)
    
    def test_evaluar_expresion_valida(self):
        """Prueba la evaluación de expresiones válidas."""
        self.assertEqual(Calculadora.evaluar_expresion("2 + 3 * 4"), 14)
        self.assertEqual(Calculadora.evaluar_expresion("(2 + 3) * 4"), 20)
        self.assertEqual(Calculadora.evaluar_expresion("10 / 2"), 5)
    
    def test_evaluar_expresion_caracteres_invalidos(self):
        """Prueba que la evaluación lance error con caracteres inválidos."""
        with self.assertRaises(ValueError) as contexto:
            Calculadora.evaluar_expresion("2 + abc")
        self.assertEqual(str(contexto.exception), "La expresión contiene caracteres no permitidos")
    
    def test_evaluar_expresion_palabras_prohibidas(self):
        """Prueba que la evaluación lance error con palabras prohibidas."""
        with self.assertRaises(ValueError) as contexto:
            Calculadora.evaluar_expresion("__import__('os')")
        self.assertEqual(str(contexto.exception), "Expresión no permitida")
    
    def test_evaluar_expresion_sintaxis_invalida(self):
        """Prueba que la evaluación lance error con sintaxis inválida."""
        with self.assertRaises(ValueError) as contexto:
            Calculadora.evaluar_expresion("2 + * 3")
        self.assertEqual(str(contexto.exception), "Expresión matemática inválida")

if __name__ == '__main__':
    unittest.main()
