# Imports
from tkinter import *           # For GUI
from RPLCD.i2c import CharLCD   # For LCD interfacing
import time                     # For scrolling control

# Global variables
TEXT = ''           # The text displayed on the LCD
TIME_STEP = 1       # How quickly the text scrolls


# Functions
def button_press():
    '''
    Defines the function that occurs when the button is pressed.

    On button press, the text in the Entry widget is read and becomes the new loop text on the LCD.
    '''
    TEXT = entry.get()



def scroll():
    '''
    Logic for scrolling the text on the LCD.
    '''
    # Checking if the text doesn't fill the screen
    if len(TEXT) < MAX_CHAR:
        TEXT += ' '*(MAX_CHAR-len(TEXT))
        lcd.write_string(TEXT)
        time.sleep(TIME_STEP)
        for i in range(len(TEXT)):
            new_text = TEXT[i:] + TEXT[:i]
            lcd.write_string(new_text)
            time.sleep(TIME_STEP)

    # When the text doesn't fill the screen
    else:
        TEXT += ' '*(int(MAX_CHAR/2))
        new_text = TEXT[:MAX_CHAR]
        lcd.write_string(new_text)
        time.sleep(TIME_STEP)
        for i in range(len(TEXT)):
            low = i
            high = i + MAX_CHAR
            if i + MAX_CHAR > len(TEXT):
                new_high = i + MAX_CHAR - len(TEXT)
                new_text = TEXT[i:] + TEXT[:new_high]
            else:
                new_text = TEXT[low:high]

            lcd.write_string(new_text)
            time.sleep(TIME_STEP)



# LCD Configuration
LCD_I2C_ADDRESS = 0x27
I2C_BUS = 1                             # I2C bus number
LCD_WIDTH = 16
LCD_LINES = 2
MAX_CHAR = LCD_WIDTH * LCD_LINES        # Max number of characters

lcd = CharLCD(
    i2c_expander='PCF8574',             # Specify the I2C expander chip
    address=LCD_I2C_ADDRESS,
    port=I2C_BUS,
    cols=LCD_WIDTH,
    rows=LCD_LINES,
    charmap='A00',
    auto_linebreaks=True,
    backlight_enabled=True              # Set initial backlight state
)

# Initializing the window
window = Tk()
window.title("Text Loop Widget--Fun!")
window.geometry("600x500")
window.after(TIME_STEP*1000-50, scroll)         # Executing the scroll function every TIME_STEP

# Initializing components
label = Label(window, text='Enter the text to loop on the LCD')
entry = Entry(window)
button = Button(window, text='Send to LCD!', command=button_press)

# Assigning widget locations
label.grid(row=0)
entry.grid(row=1)
button.grid(row=2)


# Launching widget
if __name__ == "__main__":
    window.mainloop()
