from Operators.Operator import ArithmeticOperator

class Operations(ArithmeticOperator):
    def __init__(self):
        super().__init__()
        var = self.operators
        self.number1 = 0
        self.number2 = 0


    def GetInputs(self):
        number1 = eval(input('Number1: '))
        self.number2 = eval(input('Number2: '))

    def GetOperator(self):
        self.operator = input('Enter operator: ')


    def Operate(self):
        if self.operator in self.operators:
            if self.operator == '+':
                result = self.number1 + self.number2
                print('\nThe sum  of {:2d}  and  {:2d} = {:2d} '.format(self.number1,self.number2,result))
                return result

            elif self.operator == '*':
                result = self.number1 * self.number2
                print('The product = ', result)
                return result

            elif self.operator == '-':
                if self.number1 > self.number2:
                    result = self.number1 - self.number2
                    print('The difference = ', result)
                    return result

                else:
                    result = self.number2 - self.number1
                    print('The difference = ', result)
                    return result

            elif self.operator == '/':
                if self.number1 > self.number2 != 0:
                    result = self.number2 / self.number1
                    return result
                else:
                    try:
                        pass
                    except ZeroDivisionError:
                        print('zero division error')

            elif self.operator == '%':
                result = self.number1 % self.number2
                print('The remainder = ',result)
                return result


        else:
            print('Error!!!')

Operator1 = Operations()
Operator1.GetInputs()
Operator1.GetOperator()
Operator1.Operate()
