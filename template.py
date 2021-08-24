'''
import tkinter as tki
import time

app = tki.Tk()
app.title('Auto Screenshot | Aptika Sulteng')
app.geometry('600x400')
app.configure(background="black")
  
print(time.sleep(int(input("Durasi SS / detik ?\t"))))

for i in range(int(input('mau SS berapa kali dalam 1x kerja ? '))):

  filename = 'ss-' + str(i) + '.png'
  print(filename)

  import pyautogui as pag
  proses = pag.screenshot()
  proses.save(filename)

  # Fungsi yg dibawah ini => untuk Refreshing Script. Nyalakan jika perlu
  # pag.hotkey('control', 'r')

  # Mengatur Jeda dalam sekali Looping
  # time.sleep(10)
'''
# ==============================================================================
'''
import pyautogui
import time
# beri waktu untuk mengatur layar yang akan disimpan
# 5 detik
time.sleep(5)
# mulai melakukan screenshot secara berkala
for i in range(5):
   filename = 'layar' + str(i) + '.png'
   print(filename)
   im = pyautogui.screenshot()
   im.save(filename)
   # jika perlu dilakukan refresh, gunakan perintah di bawah
   #pyautogui.hotkey('command', 'r')
   time.sleep(10)
'''