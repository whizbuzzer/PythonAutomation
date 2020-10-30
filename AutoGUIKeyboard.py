########################################################################################################################
# Automating GUI with Python by Al Sweigart: Keyboard Automation #######################################################
# made by aniket N Prabhu                                        #######################################################
########################################################################################################################

########################################################################################################################

# In computer coordinates, top-left is considered (0, 0); we are operating in Quadrant IV.
import pyautogui  # GUI automation package: https://pyautogui.readthedocs.org/

########################################################################################################################

print("In order to type,\n1. snap MS word to the right and pycharm to the left."
      "\n2. Press enter.")
input()
pyautogui.click(983, 420, duration=0.3)
pyautogui.typewrite('Hello World.', interval=0.1)  # Sends virtual key-presses to the computer. Duration is optional.
input('There are keywords for non-character keys like shift, escape, etc. example (Press enter):\n')
print(pyautogui.KEYBOARD_KEYS)
pyautogui.leftClick(1018, 420)
pyautogui.typewrite(['t'], interval=0.1)
input()
# We can also press single keys:
pyautogui.leftClick(1018, 420)
pyautogui.press('tab')
# Or use hotkeys:
pyautogui.leftClick(1018, 420)
pyautogui.hotkey('alt', 'f4')
pyautogui.click(1549, 731, duration=0.3)

########################################################################################################################
########################################################################################################################
