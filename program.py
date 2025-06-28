# import pyautogui
# import time
# import pyperclip

# # Step 1: Click on the icon at coordinates (1018, 1067)
# pyautogui.click(1018, 1067)
# time.sleep(1)  # Wait for 1 second to ensure the click is registered

# # Step 2: Drag the mouse from (546, 138) to (1898, 944) to select the text
# pyautogui.moveTo(546, 138)
# pyautogui.dragTo(1898, 944, duration=1.0, button='left')  # Drag for 1 second

# # Step 3: Copy the selected text to the clipboard
# pyautogui.hotkey('ctrl', 'c')
# time.sleep(1)  # Wait for 1 second to ensure the copy command is complete

# # Step 4: Retrieve the text from the clipboard and store it in a variable
# text = pyperclip.paste()

# # Print the copied text to verify
# print(text)


import pyautogui
import time
import pyperclip

# Safety settings
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

# Step 1: Click on the icon at coordinates (1018, 1067)
print("Clicking icon...")
pyautogui.click(1018, 1067)
time.sleep(2)  # Wait for app/window to open

# Step 2: Drag the mouse from (546, 138) to (1898, 944) to select the text
print("Selecting text...")
pyautogui.moveTo(676, 197)
pyautogui.mouseDown()
pyautogui.moveTo(1874, 925, duration=1.0)
pyautogui.mouseUp()

# Step 3: Copy the selected text to the clipboard
print("Copying to clipboard...")
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# Step 4: Retrieve text
text = pyperclip.paste()

# Step 5: Print result
print("Copied text:")
print(text if text.strip() else "[Clipboard is empty]")


