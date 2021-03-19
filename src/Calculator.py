from CsvReader import CsvReader

def addition(a,b):
     return (int)a+(int)b

class Calculator:


    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
