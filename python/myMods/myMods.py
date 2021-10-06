"""A system of functions to ease the repetivity. helpMe() in code for more info
    """
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # warnings.filterwarnings("ignore", category=ModuleNotFoundError)
    import time, keyboard, mouse, string, random, os, sys, json, matplotlib, google, pygsheets, calendar, base64, pandas, time, datetime, dbm, email, cmd, random_word, functools, gspread, gzip, hashlib, joblib, keyword, kiwisolver, numbers, numpy, oauth2client, oauthlib, parser, pickle, parser, pathlib, pickletools, pstats, pydoc, queue, requests, regcheck, secrets, symbol, turtle, tkinter, typing, uuid, urllib3, venv, warnings, wave, xml, zipfile
import cmath


def quadratic():
    """Runs the quadratic formula on three numbers int the form ax^2+bx+c=0 and returns
solution

    Returns:
        int: solutions. Values one and two can be called with sol1 and sol2
    """

    a = int(input("Ax^2+Bx+C\nA? "))
    b = int(input("B? "))
    c = int(input("C? "))
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
        print("Sorry, factorial does not exist for negative numbers")
    elif n in {0, 1}:
        print("The factorial of 0 or 1 is 1")
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return ("the factorial of ",n," is: ",fact)



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
        print("Error, not float or int")
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
        print("Error, not float or int")
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
        print("Error, not float or int")
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
        print("Error, not float or int")
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


def redo(programToRerun, timeBeforeReRunAsk=0, yesWaitTime=0, noWaitTime=0):
    """Redoes a function, aka runs a function with a query and time to wait after input.
    Equivalent to r

    Args:
        programToRerun (str): function you want to run with no brackets.
        timeBeforeReRunAsk (int, optional): Time before the program asks to rerun . Defaults to 0.
        yesWaitTime (int, optional): Time after yes is inputted befre running again. Defaults to 0.
        noWaitTime (int, optional): Time after no is inputted before ending function. Defaults to 0.
    """

    def yes():
        sleep(yesWaitTime)
        programToRerun()

    def no():
        print("Closing..")
        sleep(noWaitTime)
        print("Closed")
        exit

    from sys import exit
    from time import sleep

    sleep(timeBeforeReRunAsk)
    startOVer = input("Re Run, Yes or No: ")
    startOver = startOVer.upper()
    if (
        startOver == "Y"
        or startOver == "YES"
        or startOver == "YS"
        or startOver == "YE"
        or startOver == "ES"
        or startOver == ""
    ):
        yes()
    elif startOver == "N" or startOver == "NO" or startOver == "O":
        no()
    else:
        no()


def r(programToRerun, timeBeforeReRunAsk=0, yesWaitTime=0, noWaitTime=0):
    """Redoes a function, aka runs a function with a query and time to wait after input.
    Equivalent to redo

    Args:
        programToRerun (str): function you want to run with no brackets.
        timeBeforeReRunAsk (int, optional): Time before the program asks to rerun . Defaults to 0.
        yesWaitTime (int, optional): Time after yes is inputted befre running again. Defaults to 0.
        noWaitTime (int, optional): Time after no is inputted before ending function. Defaults to 0.
    """

    def yes():
        sleep(yesWaitTime)
        programToRerun()

    def no():
        print("Closing..")
        sleep(noWaitTime)
        print("Closed")
        exit

    from sys import exit
    from time import sleep

    sleep(timeBeforeReRunAsk)
    startOVer = input("Re Run, Yes or No: ")
    startOver = startOVer.upper()
    if (
        startOver == "Y"
        or startOver == "YES"
        or startOver == "YS"
        or startOver == ""
        or startOver == "YE"
    ):
        yes()
    elif startOver == "N" or startOver == "NO" or startOver == "":
        no()
    else:
        no()


def quickRedo(programToRerun, timeBeforeReRunAsk=0):
    """Runs a function again with a wait time. No asking about redoing. Equivalent to qR

    Args:
        programToRerun (str): Name of the function to run without the brackets
        timeBeforeReRunAsk (int, optional): Time before running again. Defaults to 0.
    """
    from sys import exit
    from time import sleep

    sleep(timeBeforeReRunAsk)
    programToRerun()


def qR(programToRerun, timeBeforeReRunAsk=0):
    """Runs a function again with a wait time. No asking about redoing. Equivalent to quickRedo

    Args:
        programToRerun (str): Name of the function to run without the brackets
        timeBeforeReRunAsk (int, optional): Time before running again. Defaults to 0.
    """
    from sys import exit
    from time import sleep

    sleep(timeBeforeReRunAsk)
    programToRerun()


def tkSetup(title, label1, label2, buttondo, buttonName="Button", windowSize="600x600"):
    """Auto create a tkinter window with several set options and values. This has a built in close function. Equivalent to tS

    Args:
        title (str): Title of the window you wish to display
        label1 (str): first label you wish to display
        label2 (str): second label you wish to display
        buttondo (str): function that you want to run.
        buttonName (str, optional): Name of button. Defaults to "Button".
        windowSize (str, optional): Size of window in str format, . Defaults to "600x600".
    """
    import tkinter
    import tkinter.ttk
    from time import sleep

    namme = tkinter.Tk()
    namme.geometry(windowSize)
    namme.lift()
    namme.bind("<Escape>", lambda e: namme.destroy())
    namme.attributes("-topmost", True)
    namme.after_idle(namme.attributes, "-topmost", False)
    lab = tkinter.StringVar()
    but = tkinter.StringVar()
    but.set(buttonName)
    lab.set(label1)
    lab2 = tkinter.StringVar()
    lab2.set(label2)
    namme.title(title)
    label1 = tkinter.Label(namme, textvariable=lab).pack()
    label2 = tkinter.Label(namme, textvariable=lab2).pack()
    closebutton = tkinter.Button(namme, text="Close", command=namme.destroy).pack()
    button = tkinter.Button(namme, textvariable=but, command=buttondo).pack()
    tkClose(namme)
    namme.mainloop()


def tS(title, label1, label2, buttondo, buttonName="Button", windowSize="600x600"):
    """Auto create a tkinter window with several set options and values. This has a built in close function. Equivalent to tkSetup

    Args:
        title (str): Title of the window you wish to display
        label1 (str): first label you wish to display
        label2 (str): second label you wish to display
        buttondo (str): function that you want to run.
        buttonName (str, optional): Name of button. Defaults to "Button".
        windowSize (str, optional): Size of window in str format, . Defaults to "600x600".
    """
    import tkinter
    import tkinter.ttk
    from time import sleep
    import sys

    namme = tkinter.Tk()
    namme.geometry(windowSize)
    namme.lift()
    namme.attributes("-topmost", True)
    namme.after_idle(namme.attributes, "-topmost", False)
    lab = tkinter.StringVar()
    but = tkinter.StringVar()
    but.set(buttonName)
    lab.set(label1)
    lab2 = tkinter.StringVar()
    lab2.set(label2)
    namme.title(title)
    label1 = tkinter.Label(namme, textvariable=lab).pack()
    label2 = tkinter.Label(namme, textvariable=lab2).pack()
    button = tkinter.Button(namme, textvariable=but, command=buttondo).pack()
    closebutton = tkinter.Button(namme, text="Close", command=namme.destroy).grid(
        row=0, column=3
    )
    namme.bind("<Escape>", lambda e: namme.destroy())
    tkClose(namme)
    namme.mainloop()


def tkClose(closeWindowName):
    """The purpose of this function is to destroy a window and call a message box to check closing, or by using 'esc' key or file>>exit

    Args:
        closeWindowName (str): Window name to close
    """
    import tkinter
    from tkinter import Button, Text
    from tkinter import messagebox
    import tkinter.scrolledtext as scrolledtext

    closeWindowName.bind("<Escape>", lambda e: closeWindowName.destroy())
    menubar = tkinter.Menu(closeWindowName)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=closeWindowName.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    closeWindowName.config(menu=menubar)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            closeWindowName.destroy()

    closeWindowName.protocol("WM_DELETE_WINDOW", on_closing)
    try:
        closer132345 = Button(
            closeWindowName, text="Close", command=closeWindowName.destroy
        ).pack
    except:
        print("")
#######TESTZONE COMMMENT OUT#######
# helpMe()
# quadradic(3,4,5)
welcomeMessage = "Hello From the MyMods Developer!\nFor help, just type 'helpMe()' in your file somewhere!"
print(welcomeMessage)
#######TESTZONE COMMMENT OUT#######
