import pyautogui

print(pyautogui.size())
width, height = pyautogui.size()  # get the resolution of the screen

print(pyautogui.position())  # get the current position of the mouse
# the bottommost and rightmost coordinates will be the width -1 and height - 1

pyautogui.moveTo(10, 10)  # move the mouse to the 10, 10 coordinate
pyautogui.moveTo(10, 10, duration=1.5)  # same as above but move there in 1.5s
pyautogui.moveRel(200, 0)  # move the mouse in X-axis by 200 pixels
pyautogui.moveRel(0, -100)  # move Y-axis up by 100 pixels

pyautogui.click(200, 300)  # doing the click at 200, 300 coordinate
pyautogui.rightClick(200, 300)  # same but doing right click

# sometimes the GUI automation may have bug and keep running
# to stop the automation we can keep moving the mouse to the top left corner
# it is a safer point that sets by the library to break the program

# in terminal we can execute the following line
# pyautogui.displayMousePosition()
# it will constantly return the position of the mouse, easier for you to look at the coordinate
# and also we can know the RGB value

distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1)  # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1)  # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1)  # move up

pyautogui.click(100, 100)
pyautogui.typewrite('Hello world!', interval=0.2)  # send virtual key presses to the computer
# interval is similar to duration, putting pause between each character
pyautogui.typewrite('a', 'b', 'left', 'left', 'X', 'Y', interval=0.2)   # pressing left arrow twice
print(pyautogui.KEYBOARD_KEYS)          # different keyboard keys
pyautogui.press('f1')                   # pressing once
pyautogui.hotkey('ctrl', 'o')           # pressing shortcut


pyautogui.screenshot('c:\\screenshot_example.png')        # taking screenshot
pyautogui.locateOnScreen('c:\\calc7key.png')              # to locate the position of the image in the screenshot
pyautogui.locateCenterOnScreen('c:\\calc7key.png')        # return the centre of the image in the screenshot
pyautogui.moveTo((932, 336), duration=1)
pyautogui.click((932, 336))
# this way to locate needs to be pixel perfect and therefore kinda slow
