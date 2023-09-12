import time
import pyautogui
"""
pyautogui.click(122,1060,1)
time.sleep(1)
pyautogui.typewrite("Edge", 0.3)
time.sleep(1)
pyautogui.click(240,104,1,0.2)
time.sleep(1)
pyautogui.click(352,53,1,0.2)
time.sleep(1)
pyautogui.typewrite("https://www.instagram.com/casadosanjos/", 0.1)
time.sleep(1)
pyautogui.press("enter")

time.sleep(9)

pyautogui.click(717,855,1)
time.sleep(1)
"""

for i in range(1):
    if pyautogui.locateCenterOnScreen('heart.png'):
        
        pyautogui.click(1828, 556)
        time.sleep(2)
        print("Loop concluído! Loop:", i)
    else:
        
        img = pyautogui.locateCenterOnScreen('like.png')
        pyautogui.click(img)
        time.sleep(2)

        img2 = pyautogui.locateCenterOnScreen('coment.png')
        pyautogui.click(img2)
        pyautogui.typewrite("Mensagem de engajamento: O justo cuida dos seus animais, mas o coracao dos impios e cruel (Proverbios 12:10)", 0.1)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.click(1828, 556)
        time.sleep(2)

        print("Loop concluído! Loop:", i)


