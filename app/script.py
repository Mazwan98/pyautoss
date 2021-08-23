import pyautogui  # mengimpor Library pyautogui
import time  # mengimpor Library Time utk menerapkan Timing (Jeda, durasi, dll)

# memberi waktu antar screnshot (akan Screenshot per 5 Detik). Disini sy Sett per 5 detik
time.sleep(5)

# mulai screenshot secara berkala
# saya Sett Screenshot sebanyak 5x. pakai range(5) artinya akan dihitung mulai dari 0 = 1, 1=2, 2=3, dst.
for i in range(5):

    # membuat nama file hasil screenshot. contoh : screenshot 0.png, screenshot 1.png, screenshot 2.png, dst
    filename = 'screenshot ' + str(i) + '.png'
    
    # Menampilkan laporan bahwa File sedang dibuat (Proses)
    print('File ' + filename + ' sedang dibuat')
    
    shot = pyautogui.screenshot()  # membuat sebuah Variabel shot
    shot.save(filename)  # Fungsinya untuk menyimpan Hasil File SS


    # =====================================================================
    # Kalo emang perlu melakukan refresh, Nyalakan perintah di bawah ini
    # pyautogui.hotkey('command', 'r')
    # =====================================================================


    # menentukan Durasi waktu untuk melakukan Jeda utk Refleksi usai Running Script.

    time.sleep(10)

'''
To Do List :

1. Kawinkan Script ke Gui
2. Mengganti Icon App
3. Membuat Frame khusus Laporan Hasil Screenshot ke GUI (Bukan di CLI / CMD) dan Membuat Loading
4. Memastikan Script berjalan dgn Baik (Gk ada Error)
5. Modifikasi Script biar lebih Clean Code saat Presentasi Tgl 26 Agustus nnti.

NB : Jgn Lupa Pelajari Script demi Script. Kalo gk tau silahkan bertanya di Grup kelompok kita diskusi Bareng. 

Regard's,
Sulistiawan | PYT-3C

=========================================
Kelompok L :
1. sulistiawan A P (Palu | Sulteng)
2. Yusuf Bagaskoro (Jakarta)
3. Bernad Wahyu
'''
