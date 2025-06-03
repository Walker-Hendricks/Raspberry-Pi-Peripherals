from RPLCD.i2c import CharLCD
import time

# --- Configuration ---
# Replace with the actual I2C address you found (e.g., 0x3F)
LCD_I2C_ADDRESS = 0x27
# I2C bus number (usually 1 for Raspberry Pi)
I2C_BUS = 1
# LCD dimensions
LCD_WIDTH = 16
LCD_LINES = 2
# Max number of characters
MAX_CHAR = 32

lcd = CharLCD(
    i2c_expander='PCF8574', # Specify the I2C expander chip
    address=LCD_I2C_ADDRESS,
    port=I2C_BUS,
    cols=LCD_WIDTH,
    rows=LCD_LINES,
    charmap='A00',
    auto_linebreaks=True,
    backlight_enabled=True # Set initial backlight state
)

def scroll(text, time_step = 1):
    if len(text) < MAX_CHAR:
        text += ' '*(MAX_CHAR-len(text))
        lcd.write_string(text)
        while True:
            time.sleep(time_step)
            for i in range(len(text)):
                new_text = text[i:] + text[:i]
                lcd.write_string(new_text)
                time.sleep(time_step)
    else:
        text += ' '*(int(MAX_CHAR/2))
        new_text = text[:MAX_CHAR]
        lcd.write_string(new_text)
        while True:
            time.sleep(time_step)
            for i in range(len(text)):
                low = i
                high = i + MAX_CHAR
                if i + MAX_CHAR > len(text):
                    new_high = i + MAX_CHAR - len(text)
                    new_text = text[i:] + text[:new_high]
                else:
                    new_text = text[low:high]

                lcd.write_string(new_text)
                time.sleep(time_step)

scroll('This is the story of a bunch of physics students who had to take Dr. Wilcox for E&M1. Strap yourselves in--it is a bumpy ride!', 0.8)