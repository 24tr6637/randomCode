def helpMe():
    """Help function."""
    from time import sleep
    from sys import exit
    from myMods import qR

    print("Help Page Here")
    print("Current Modules:\nTkSetup\nRedo")
    sleep(1)
    print("QuickRedo\nTkClose")
    sleep(1)
    print("Triangle Area-Triangle\nQuadratic Roots")
    sleep(1)
    #TODO add all descriptions to the menu. NOTE:   factor, factorial, prime checker.

    print("Calculator Menu\nBasic Arithmetic Menu\nAddition\nSubtraction\nMultiplacation\nDivision")
    sleep(1)
    print("factorial\nfactors\nPrime Checker")
    helpWith = input("What module do you need help with? ")
    helpWith = helpWith.upper()
    if helpWith in ["REDO", "R", "RESTART", "REDO()", "RESTART()"]:
        print("Usage of Redo:")
        sleep(1)
        print("To use, type:\nfrom myMods import redo")
        sleep(1)
        print(
            "Then, type redo(function you want to run with no brackets, Time before asking to re-run, yes wait time, no wait time)"
        )
        sleep(1)
        print("The last 3 arguments are optional...")
        sleep(1)
        print("You can also use: from myMods import r, and r(...) for the same result")
        qR(helpMe)
    elif helpWith in ["FACTORIAL"]:
        print("Usage of factorial")
        sleep(1)
        print("To use, type:\nfrom myMods import factorial")
        sleep(1)
        print("""Then, type factorial(number to factorial)\nTo print this
result, simply type print(factorial(number to factorial)) """)
        qR(helpMe)
    elif helpWith in ["FACTOR"]:
        print("Usage of factor")
        sleep(1)
        print("To use, type:\nfrom myMods import factor")
        sleep(1)
        print("""Then, type factor(number to factor)\nTo print this
result, simply type print(factor(number to factor)) """)
        qR(helpMe)
    elif helpWith in ["ADDITION", "ADD"]:
        print("Usage of add")
        sleep(1)
        print("To use, type:\nfrom myMods import add")
        sleep(1)
        print("""Then, type add(first number to add, second number to add)\nTo print this
result, simply type print(add(first number to add, add second number to add)) """)
        qR(helpMe)
    elif helpWith in ["DIVISION", "DIVIDE"]:
        print("Usage of divide")
        sleep(1)
        print("To use, type:\nfrom myMods import divide")
        sleep(1)
        print("""Then, type divide(number to be divided, number to be divided by)\nTo print this
result, simply type print(divide(number to be divided, number to be divided by)) """)
        qR(helpMe)
    elif helpWith in ["MULTIPLICATION", "MULTIPLY"]:
        print("Usage of multiply")
        sleep(1)
        print("To use, type:\nfrom myMods import multiply")
        sleep(1)
        print("""Then, type multiply(first number to multiply, second number to add)
To print this result, simply type print(multiply(first number to multiply, second number
to multiply)) """)
        qR(helpMe)
    elif helpWith in ["SUBTRACTION", "SUBTRACT"]:
            print("Usage of subtract")
            sleep(1)
            print("To use, type:\nfrom myMods import subtract")
            sleep(1)
            print(
                """Then, type subtract(first number to subtract, number to be subtracted from first number)\nTo print this
result, simply type print(subtract(first number to subtract, number to be subtracted from first number)) """)
            qR(helpMe)
    elif helpWith in [ "BASIC FUNCTIONS","BASIC MENU"]:
        print("Usage of Basic Menu")
        sleep(1)
        print("To use, type:\nfrom myMods import basicFunctions")
        sleep(1)
        print("Then, type basicFunctions()","""This will open the calculator menu the next time the code is run
Make sure to also install all of the other nesscary functions as well, i.e "add\"""")
        qR(helpMe)

    elif helpWith in ["CALCULATOR", "CALCULATOR MENU"]:
        print("To use, type:\nfrom myMods import calculator")
        sleep(1)
        print("Then, type calculator()")
        sleep(1)
        print(
            """This will open the calculator menu the next time the code is run
Make sure to also install all of the other nesscary functions as well""")
    elif helpWith in [
        "QUICKREDO",
        "QUICKRESTART",
        "QUICKRERUN",
        "QUICKREDO()",
        "QUICKRESTART()",
        "QR",
    ]:
        print("Usage of quickRedo:")
        sleep(1)
        print("To use, type:\nfrom myMods import quickRedo")
        sleep(1)
        print(
            "Then, type quickRedo(function you want to run with no brackets, time before re-runing)"
        )
        sleep(1)
        print("The last argument is optional... Default is zero.")
        sleep(1)
        print(
            "You can also use: from myMods import qR, and qR(...) for the same result"
        )
    elif helpWith in ["TkKTEMPLATE", "TKSETUP", "TS"]:
        print("Usage of TkSetup:")
        sleep(1)
        print("To use, type:\nfrom myMods import tkSetup")
        sleep(1)
        print(
            """Then, type tkSetup('WindowTitle','Label1','Label2',ButtonFunction, 'WindowSize', 'ButtonName'::Ex. '300x600')"""
        )
        sleep(1)
        print("This has a built in close function.")
        sleep(1)
        print(
            "You can also use: from myMods import tS, and tS(....) for the same result"
        )
        sleep(1)
        print("""Make sure button function has 'event' as an argument""")
        qR(helpMe)
    elif helpWith == "ABSV":
        print("Absv has been removed....")
        sleep(1)
        print("Please use abs() for absolute value functions ")
        sleep(1)
        qR(helpMe)
    elif helpWith == "PASS":
        pass
    elif helpWith == "ALL":

        print("Usage of TkSetup:")
        sleep(1)
        print("To use, type:\nfrom myMods import tkSetup")
        sleep(1)
        print(
            """Then, type tkSetup('WindowTitle','Label1','Label2','ButtonFunction',ButtonName,'WindowSize'::Ex. '300x100')"""
        )
        sleep(1)
        print("This has a built in close function.")
        sleep(1)
        print("""Make sure button function has 'event' as an argument""")
        sleep(1)
        print("""For a blank label, use ' ' as label 1 or 2 """)
        sleep(1)
        print(
            "You can also use: from myMods import tS, and tS(....) for the same result"
        )
        sleep(1)
        print("Usage of quickRedo:")
        sleep(1)
        print("To use, type:\nfrom myMods import quickRedo")
        sleep(1)
        print(
            "Then, type quickRedo(function you want to run with no brackets, time before re-runing)"
        )
        sleep(1)
        print("The last argument is optional... Default is zero.")
        sleep(1)
        print(
            "You can also use: from myMods import qR, and qR(...) for the same result"
        )
        sleep(1)
        print("Usage of Redo:")
        sleep(1)
        print("To use, type:\nfrom myMods import redo")
        sleep(1)
        print(
            "Then, type redo(function you want to run with no brackets, Time before asking to re-run, yes wait time, no wait time)"
        )
        sleep(1)
        print("The last 3 arguments are optional...")
        sleep(1)
        print("You can also use: from myMods import r, and r(...) for the same result")
        sleep(1)
        print("Usage of tkClose:")
        sleep(1)
        print("To use, type:\nfrom myMods import tkClose")
        sleep(1)
        print("Then, type tkClose(windowName to close)")
        sleep(1)
        print(
            """The purpose of this function is to destroy a window and call a message box to check closing, or by using 'esc' or 'e' key and file>exit"""
        )
        sleep(1)
        print(
            """You will have to mainloop the window after tkClosing the window name. """
        )
        qR(helpMe)
    elif helpWith in ["TKDESTROY", "TKCLOSE"]:
        print("Usage of tkClose:")
        sleep(1)
        print("To use, type:\nfrom myMods import tkClose")
        sleep(1)
        print("Then, type tkClose(windowName to close)")
        sleep(1)
        print(
            """The purpose of this function is to destroy a window and call a message box to check closing, or by using 'esc' or 'e' key or file>>exit"""
        )
        qR(helpMe)
    elif helpWith in ["TRIANGLE", "TRIANGLE AREA"]:
        print("Usage of triangle:")
        sleep(1)
        print("To use, type:\nfrom myMods import triangle")
        sleep(1)
        print("Then, type print(triangle(first side, second side, third side)).\nAlternatively, do not print.")
        sleep(1)
        qR(helpMe)
    elif helpWith in [
        "QUADRADIC FOURMULA",
        "QUADRADIC",
        "QUADRATIC FOURMULA",
        "QUADRATIC",
    ]:
        print("Usage of quadratic:")
        sleep(1)
        print("To use, type:\nfrom myMods import quadratic")
        sleep(1)
        print("Then, type print(quadratic(a, b , c))\nIn the format Ax^2+Bx+C=0 to print.\nAlternatively, do not print. ")
        sleep(1)
        qR(helpMe)
    else:
        print("Please enter a valid function...")
        sleep(1)
        qR(helpMe)