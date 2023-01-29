#Defining the operators to be used
class ArithmeticOperator:

    def __init__(self):
        self.operators = ['+', '-', '*', '/', '%']

    @staticmethod
    def Addition():
        summator = '+'
        return summator

    @staticmethod
    def Subtraction():
        subtractor = '-'
        return subtractor

    @staticmethod
    def Multiplication():
        product = '*'
        return product

    @staticmethod
    def Division():
        divider = '/'
        return divider

    @staticmethod
    def Modulus():
        modulo = '%'
        return modulo
