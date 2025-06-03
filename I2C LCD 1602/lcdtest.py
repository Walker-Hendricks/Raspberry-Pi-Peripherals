from RPLCD.i2c import CharLCD

# --- Configuration ---
# Replace with the actual I2C address you found (e.g., 0x3F)
LCD_I2C_ADDRESS = 0x27
# I2C bus number (usually 1 for Raspberry Pi)
I2C_BUS = 1
# LCD dimensions
LCD_WIDTH = 16
LCD_LINES = 2

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
print(f"LCD Initialized (Address: {hex(LCD_I2C_ADDRESS)}, Bus: {I2C_BUS})")


# --- Basic Display Operations ---

# 1. Clear the display
lcd.clear()
print("LCD Cleared.")

# 2. Write a single line
lcd.write_string('Hello, RPLCD!')
print("Displayed 'Hello, RPLCD!'")

# lcd.backlight_enabled = False