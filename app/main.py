'''

Desktop App Screenshot Otomatis
By : Sulistiawan
Github : Mazwan98

www.Binarybay.site

'''

import datetime
import tkinter.messagebox as tm
import tkinter as tki
import pyautogui as pag
import time
from datetime import date
import os


def main():
    app = tki.Tk()
    app.title('Auto Screenshot - Aptika')

    def about():
        tm.showinfo(
            'About', 'Author\t: Sulistiawan A P\nIG\t: @wawan.sulisstia\nGithub\t: github.com/Mazwan98')

    menubar = tki.Menu(app, tearoff=0, selectcolor='black')
    menubar.add_command(label='About App', command=about)

    var = tki.IntVar()
    var.set(2)

    var2 = tki.IntVar()
    var2.set(5)
    
    var3 = tki.StringVar()
    var3.set('Nama Kegiatan')

    def reset():
        var.set('0')
        var2.set('0')
        var3.set('')

    def mulai():

        time.sleep(var.get())

        for i in range(var2.get()):

            sesi = str(var3.get())
            today = str(date.today())
            namaSesi = sesi + ' ' + today
            filename = 'Shot' + ' ' + str(i) + '.png'
            folder = r'Screenshot' + '\\' + namaSesi + '\\' + filename

            try:

                info = tki.Label(app, text='Selesai  . . .', bg='black', fg='green')
                info.grid(row=3, column=0, padx=3, pady=3)
                
                
                shot = pag.screenshot()
                shot.save(folder)

            except:

                os.chdir('Screenshot')
                os.mkdir(namaSesi)
                os.chdir(namaSesi)
                # os.mkdir(sesi)
                # os.chdir(sesi)
                
                
                info = tki.Label(app, text='Path terbuat, Mohon tutup Aplikasi dan diulangi lagi .. ', bg='black', fg='green')
                info.grid(row=3, column=0, padx=3, pady=3)
                
                
                shot = pag.screenshot()
                shot.save(folder)
                
            # except FileNotFoundError():
            #     info = tki.Label(app, text='Mohon diulangi .. ', bg='black', fg='green')
            #     info.grid(row=3, column=0, padx=3, pady=3)
                
                

                # info = tki.Label(app, text='Folder ' + today +
                #                  ' terbuat . . .', bg='black', fg='green')
                # info.grid(row=3, column=0, padx=3, pady=3)

                # info = tki.Label(app, text='Mohon diulangi ..', bg='black', fg='green')
                # info.grid(row=3, column=0, padx=3, pady=3)

                # shot = pag.screenshot()
                # shot.save(folder)

            # finally:
            #     info = tki.Label(app, text='Ups .. Ada yang salah ( Error ) saat menyimpan ' +
            #                      filename + ' atau membuat folder ' + today, bg='black', fg='green')
            #     info.grid(row=3, column=0, padx=3, pady=3)
           
            time.sleep(5)

    l = tki.Label(app, text='Sesi\t:')
    l.grid(row=0, column=0, sticky=tki.E, padx=3, pady=3)

    e = tki.Entry(app, textvariable=var3)
    e.grid(row=0, column=1, columnspan=2, padx=3, pady=3)

    l2 = tki.Label(app, text='Durasi antar SS (Detik) ?')
    l2.grid(row=1, column=0, sticky=tki.E, padx=3, pady=3)

    e2 = tki.Entry(app, textvariable=var)
    e2.grid(row=1, column=1, columnspan=2, padx=3, pady=3)

    l3 = tki.Label(app, text='Berapa Kali SS dalam sekali Jalan ?')
    l3.grid(row=2, column=0, sticky=tki.E, padx=3, pady=3)

    e3 = tki.Entry(app, textvariable=var2)
    e3.grid(row=2, column=1, columnspan=2, padx=3, pady=3)

    b1 = tki.Button(app, text='Reset', command=reset, activebackground='red')
    b1.grid(row=3, column=1, padx=3, pady=3, sticky=tki.N+tki.S+tki.E+tki.W)

    b2 = tki.Button(app, text='Mulai', command=mulai,
                    activebackground='black', activeforeground='white')
    b2.grid(row=3, column=2, padx=3, pady=3, sticky=tki.N+tki.S+tki.E+tki.W)

    app.config(menu=menubar)
    app.mainloop()


if __name__ == "__main__":
    main()
