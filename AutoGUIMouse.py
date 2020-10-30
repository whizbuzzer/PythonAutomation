########################################################################################################################
# Automating GUI with Python by Al Sweigart: Mouse Automation ##########################################################
# made by Aniket N Prabhu                                     ##########################################################
########################################################################################################################

########################################################################################################################

# In computer coordinates, top-left is considered (0, 0); we are operating in Quadrant IV.
import pyautogui  # GUI automation package: https://pyautogui.readthedocs.org/

########################################################################################################################

########################################################################################################################

w, h = pyautogui.size()  # Stores the current size (width and height)
print(w, h)
x, y = pyautogui.position()  # Returns the current cursor coordinates (x and y), magnitude-wise, from top-left
print(x, y)
# In case you wanna find out the real-time position:
# 1. Open terminal/commandline/powershell. Executing it in IDLE creates a giant mess unfortunately.
# 2. run "python"
# 3. run "import pyautogui"
# 4. run "pyautogui.DisplayMousePosition()"

# print(type(x))

# Function for controlling the cursor:
xn, yn = input("Enter the x and y coordinates that you wanna move your cursor to: ").split()
pyautogui.moveTo(int(xn), int(yn))

# We can even move the cursor gradually instead of instantly:
xn2, yn2 = input("Enter the x and y coordinates that you wanna move your cursor to: ").split()
dur = input('Enter the duration (seconds): ')  # In seconds
pyautogui.moveTo(int(xn2), int(yn2), int(dur))

# We can also click with it:
pyautogui.moveTo(1749, 6)
pyautogui.click()  # Other options are '.rightClick()' and '.middleClick'

# If you wanna relocate the cursor with your current position as the origin then we can use:
print("Sike. :-P")
xn3, yn3 = input("Enter the x and y coordinates that you wanna move your cursor to: ").split()
pyautogui.moveRel(int(xn3), int(yn3))  # Even this accepts a third duration parameter

# Here's a loop to draw an aztec spiral:
# Open and snap paint to the right, keep the cursor on the paint program, and then execute this program:
input("Here's a loop to draw an aztec spiral"
      "\nOpen and snap paint to the right, keep the cursor on the paint program, and then press enter in pycharm")
pyautogui.click()
distance = 420
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1)  # Drag relatively. Holds the cursor and drags it horizontally,
    # to the right
    distance -= 4.2
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1)  # Drag vertically downwards
    distance -= 4.2
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1)  # Drag horizontally, to the left
    distance -= 4.2
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1)  # Drag vertically, upwards
    distance -= 4.2

# pyautogui has a failsafe function that is, whenever you wanna force-stop the program, just drag the cursor to
# top-left corner


########################################################################################################################
########################################################################################################################
