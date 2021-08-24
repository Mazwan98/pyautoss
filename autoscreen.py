import pyautogui as pag
import time
time.sleep(5)


for i in range(5):
   filename = 'ss' + str(i) + '.png'
   print(filename)
   im = pag.screenshot()
   im.save(filename)

   #pag.hotkey('command', 'r') #untuk refresh
   time.sleep(10)