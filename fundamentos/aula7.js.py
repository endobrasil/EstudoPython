class Calculadora:
    def __init__(self, num1,num2):
        self.a=num1
        self.b=num2

    def soma(self):
        return self.a+self.b

    def sumtracao(self):
        return self.a-self.b

    def divisao(self):
        return self.a/self.b

    def multiplicacao(self):
        return self.a*self.b

calculadora=Calculadora(10,7);
print(calculadora.divisao())
print(calculadora.multiplicacao())
print(calculadora.soma())
print(calculadora.sumtracao())