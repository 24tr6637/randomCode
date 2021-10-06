"""A system of functions to ease the repetivity. helpMe() in code for more info.
Functions return answer. to print, print(functionName(functionValueA,functionValueB))
    """
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # # warnings.filterwarnings("ignore", category=ModuleNotFoundError)
    import time, keyboard, mouse, string, random, os, sys, json, matplotlib, google, pygsheets, calendar, base64, pandas, time, datetime, dbm, email, cmd, random_word, functools, gspread, gzip, hashlib, joblib, keyword, kiwisolver, numbers, numpy, oauth2client, oauthlib, parser, pickle, parser, pathlib, pickletools, pstats, pydoc, queue, requests, regcheck, secrets, symbol, turtle, tkinter, typing, uuid, urllib3, venv, warnings, wave, xml, zipfile



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
