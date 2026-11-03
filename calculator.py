class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        is_negative = False
        result = 0
        if b < 0:
            b = self.subtract(0, b)
            is_negative = True
        for i in range(b):
            result = self.add(result, a)
        if is_negative:
                result = self.subtract(0, result)
        return result
    def divide(self, a, b):
        if b == 0:
            return 0 
        is_negative = False

        if a < 0 and b > 0:
            a = self.subtract(0, a)
            is_negative = True
        elif a > 0 and b < 0:
            b = self.subtract(0, b)
            is_negative = True
        elif a < 0 and b < 0:
            a = self.subtract(0, a)
            b = self.subtract(0, b)

        result = 0
        while a >= b:
            a = a-b
            result = self.add(result, 1)
        
        if is_negative:
            result = self.subtract(0, result)

        return result
    
    def modulo(self, a, b):
        if b == 0:
            return 0 
        if a < 0:
            a = self.subtract(0, a)
        if b < 0:
            b = self.subtract(0, b)
        while a >= b:
            a = a-b
            
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))