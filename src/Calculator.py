

def addition(a,b):
     return float(a)+float(b)

def subtraction(a, b):
    return float(a) - float(b)

def multiplication(a, b):
    return float(a) * float(b)

def dividing(a, b):
    return float(a) / float(b)

def squaring(a):
        return float(a) ** 2

def square_rooting(a):
    return float(a) ** 0.5

class Calculator:
    result = 0
    data = []
    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
       self.result=subtraction(a, b)
       return self.result

    def multiply(self, a, b):
        self.result=multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result=round(dividing(a, b), 9)
        return self.result

    def square(self, a):
        self.result=squaring(a)
        return self.result

    def square_root(self, a):
        self.result=square_rooting(a)
        return self.result



