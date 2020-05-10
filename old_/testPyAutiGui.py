import pyautogui

button7location = pyautogui.locateOnScreen('sevenBtn.jpeg')
# button7location
# Box(left=1416, top=562, width=50, height=41)
# button7location[0]

# button7location.left

# button7point = pyautogui.center(button7location)
# button7point
# Point(x=1441, y=582)
# button7point[0]

# button7point.x

# button7x, button7y = button7point
# pyautogui.click(button7x, button7y)  # clicks the center of where the 7 button was found
# pyautogui.click('calc7key.png') # a shortcut version to click on the center of where the 7 button was found
