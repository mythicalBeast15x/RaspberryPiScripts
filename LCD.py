from RPLCD import CharLCD

# Define LCD pins
lcd = CharLCD(cols=16, rows=3, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

# Write to the LCD screen
lcd.clear()
lcd.write_string('Hello, World!\nThis is line 2\nAnd this is line 3')

# You can also set the cursor position
lcd.cursor_pos = (0, 0)  # Set cursor to first row, first column
lcd.write_string('New text')

# Close the LCD connection
lcd.close()