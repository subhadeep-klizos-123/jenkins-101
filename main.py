from datetime import datetime
print(f"Here is a python script running at {datetime.now()} brother")

class Calc(Object):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a + b

    def mult(self, a, b):
        return a + b

    def div(self, a, b):
        return a + b

if __name__ == '__main__':
    c = Calc()
    print(f"Addition: {c.add(10 + 20)}")
    print(f"Subtraction: {c.sub(10 - 20)}")
    print(f"Multiplication: {c.mult(10 * 20)}")
    print(f"Division: {c.div(10 / 20)}")