'''

Хіленко Марк ШІД-32
markhilenko@gmail.com

'''

from app.calculator import Calculator


def main():
    calculator = Calculator(10, 5)

    print(calculator.add())
    print(calculator.subtract())
    print(calculator.multiply())
    print(calculator.divide())
    print(calculator.power())


if __name__ == "__main__":
    main()
