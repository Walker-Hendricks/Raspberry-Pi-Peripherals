# Imports
from tkinter import *           # For GUI
from RPLCD.i2c import CharLCD   # For LCD interfacing
import time                     # For scrolling control

# Global variables


# Functions
def button_press():
    '''
    Defines the function that occurs when the button is pressed.

    On button press, the text in the Entry widget is read and becomes the new loop text on the LCD.

    '''
    pass

# Initializing the window
window = Tk()
window.title("Text Loop Widget--Fun!")

# Initializing components
label = Label(window, text='Enter the text to loop on the LCD').grid(row=0)
entry = Entry(window).grid(row=1)
button = Button(window, text='Send to LCD!', command=button_press).grid(row=2)

# Launching widget
window.mainloop()
