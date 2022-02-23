from sympy import *
import matplotlib as plt

def nth_derivative(num):
    x = Symbol('x')
    y = (1-2*x+(2*x)**2)**0.5
    for i in range(num):
        y = y.diff(x)
    derivative = lambdify(x, y, 'numpy')
    return derivative(0)


def rfactorial(number):
    if number == 1:
        return 1
    else:
        return number*rfactorial(number - 1)


def expansion(func_argument, amount_of_members):
    value = 0
    for i in range(1, amount_of_members):
        value += (nth_derivative(i)/rfactorial(i))*(func_argument**i)
    return value


if __name__ == '__main__':
    func_argument = float(input("Enter the function argument: "))
    amount_of_members = int(
        input("Enter the amount of members in Taylor's expansion: "))
    x = 0
    func_in_zero = eval('(1-2*x+(2*x)**2)**0.5')
    print(func_in_zero + expansion(func_argument, amount_of_members))
