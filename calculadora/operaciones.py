"""
Módulo que contiene las operaciones básicas de la calculadora.
"""

class Calculadora:
    @staticmethod
    def suma(a, b):
        """Realiza la suma de dos números."""
        try:
            return float(a) + float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def resta(a, b):
        """Realiza la resta de dos números."""
        try:
            return float(a) - float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def multiplicacion(a, b):
        """Realiza la multiplicación de dos números."""
        try:
            return float(a) * float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def division(a, b):
        """Realiza la división de dos números."""
        try:
            a_float = float(a)
            b_float = float(b)
            if b_float == 0:
                raise ValueError("No se puede dividir entre cero")
            return a_float / b_float
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def potencia(a, b):
        """Calcula la potencia de a elevado a b."""
        try:
            return float(a) ** float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def raiz_cuadrada(a):
        """Calcula la raíz cuadrada de un número."""
        try:
            a_float = float(a)
            if a_float < 0:
                raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
            return a_float ** 0.5
        except (ValueError, TypeError):
            raise ValueError("El operando debe ser un número válido")

    @staticmethod
    def porcentaje(a, b):
        """Calcula el porcentaje de a respecto a b."""
        try:
            a_float = float(a)
            b_float = float(b)
            if b_float == 0:
                raise ValueError("El divisor no puede ser cero para calcular porcentaje")
            return (a_float / b_float) * 100
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def evaluar_expresion(expresion):
        """
        Evalúa una expresión matemática simple.
        Solo permite operaciones básicas y números.
        """
        # Validar caracteres seguros
        caracteres_permitidos = set('0123456789.+-*/() ')
        if not all(c in caracteres_permitidos for c in expresion):
            raise ValueError("La expresión contiene caracteres no permitidos")
        
        # Validar que no sea una expresión peligrosa
        palabras_prohibidas = ['import', 'exec', 'eval', 'open', 'file', '__']
        for palabra in palabras_prohibidas:
            if palabra in expresion.lower():
                raise ValueError("Expresión no permitida")
        
        try:
            # Usar eval con precaución (en un entorno controlado)
            resultado = eval(expresion, {'__builtins__': None}, {})
            return float(resultado)
        except:
            raise ValueError("Expresión matemática inválida")
