import pyperclip
import keyboard

keyboard.add_hotkey('ctrl+shift+alt+v', lambda: keyboard.write(pyperclip.paste()))

keyboard.wait('ctrl+esc')
