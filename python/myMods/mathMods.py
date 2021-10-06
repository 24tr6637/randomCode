from myMods import qR
def quadratic(a,b,c):
    import cmath
    """Runs the quadratic formula on three numbers in the form ax^2+bx+c=0 and returns
solution

    Args:
        a (int): A value in the form ax^2+bx+c=0
        b (int): B value in the form ax^2+bx+c=0
        c (int): C value in the form ax^2+bx+c=0
    Returns:
        int: solutions. Values one and two can be called with sol1 and sol2
    """


    a = int(1)
    b = int(b)
    c = int(c)
    d = (b ** 2) - (4 * a * c)
    sol1 = float((-b - cmath.sqrt(d)) / (2 * a))
    sol2 = float((-b + cmath.sqrt(d)) / (2 * a))
    return (sol1, sol2)


def prime(n):
    """Tests if a number is prime

    Args:
        n (int): Number to test if is prime

    Returns:
        bool: True or False is prime
    """
    from math import sqrt
    from itertools import count, islice
    if n < 2:
        return False
    return all(n % number != 0 for number in islice(count(2), int(sqrt(n) - 1)))


def factorial(n):
    """Finds the factorial of a number

    Args:
        n (int): number to find the factorial of

    Returns:
        int: answer to factorial
    """
    n=int(n)
    if n < 0:
        return("Sorry, factorial does not exist for negative numbers")
    elif n in {0, 1}:
        return int((1))
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return int(fact)



def add(x, y):
    """Adds X to Y and returns sum

    Args:
        x (float): Augend
        y (float): Addend

    Returns:
        float: Sum
    """
    try:
        x = float(x)
        y = float(y)
        a = float(x + y)
    except:
        return("Error, not float or int")
    return float(a)


def subtract(x, y):
    """subtracts Y from X and returns difference

    Args:
        x (float): Minuend
        y (float): Subtrahend

    Returns:
        float: Difference
    """
    try:
        x = float(x)
        y = float(y)
        a = float(x - y)
    except:
        return("Error, not float or int")
    return float(a)


def multiply(x, y):
    """Multiples X by Y and returns product

    Args:
        x (float): First Multiplicand
        y (float): Second Multiplicand

    Returns:
        float: Product
    """
    try:
        x = float(x)
        y = float(y)
        a = float(x * y)
    except:
        return("Error, not float or int")
    return float(a)


def divide(x, y):
    """Divides X by Y and returns quotient

    Args:
        x (int): [dividend]
        y (int): [divisor]

    Returns:
        float: [quotient]
    """
    try:
        x = float(x)
        y = float(y)
        a = float(x / y)
    except:
        return("Error, not float or int")
    return float(a)


def triangle():
    """Calculates the area of a triangle given three sides.

    Args:
        a (int): First side of a triangle
        b (int): Second side of a triangle
        c (int): Third side of a triangle
    Returns:
        float: the area of the triangle

    """
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    s = float((a + b + c) / 2)

    return float((s * (s - a) * (s - b) * (s - c)) ** 0.5)





def factor(n):
    """lists factors of a number.

    Args:
        n (int, optional): Number to factor.
    """
    from functools import reduce


    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def basicFunctions():
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choice(1/2/3/4): ")
    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")


def calculator():
    print("Select operation.")
    print("1.Basic Functions")
    print("2.Factorial")
    print("3.Prime Checker")
    print("4.quadratic Equation")
    print("5.Triangle Area Solver")
    print("6.Factor")
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice == "1":
        basicFunctions()
        qR(calculator)
    elif choice == "2":
        num1 = float(input("Enter Number: "))
        print("Factorial of ", num1, "=", factorial(num1))
        qR(calculator)
    elif choice == "3":
        num1 = float(input("Enter Number: "))
        print(prime(num1))
        qR(calculator)
    elif choice == "4":
        print(quadratic())
        qR(calculator)
    elif choice in ["exit", "", "e"]:
        exit
    elif choice == "5":
        print(triangle())
        qR(calculator)
    elif choice == "6":
        factor()
        qR(calculator)
    else:
        print("Invalid input")
        qR(calculator)
from myHelp import helpMe
helpMe()
