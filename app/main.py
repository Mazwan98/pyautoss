from tkinter.constants import CENTER
import tkinter.messagebox as tm
import tkinter as tki
# from typing_extensions import IntVar
# from tki.constants import GROOVE
import pyautogui as pag
import time


def main():
    app = tki.Tk()
    app.title('Auto Screenshot  |   PYT-3C ( Kel. T )')
    # app.geometry('650x250')

    var = tki.IntVar()
    var.set(1)

    var2 = tki.IntVar()
    var2.set(2)

    var3 = tki.IntVar()
    var3.set(1)

    def kosong():
        var.set('')
        var2.set('')
        var3.set('')

    def mulai():

        time.sleep(var.get())

        for i in range(var2.get()):
            # tm.showinfo('Info Bro !', var.get())
            filename = 'screenshot ' + str(i) + '.png'

            # tampil = tki.Label(app, text='File ' + filename +' sedang dibuat . . .')
            # tm.showinfo('Info Bro !', 'tes')
            info = tki.Label(app, text='File ' + filename +
                             ' sedang dibuat . . .', bg='black', fg='yellow')
            info.grid(row=3, column=0, padx=3, pady=3)

            shot = pag.screenshot()
            shot.save(filename)

            time.sleep(var3.get())

    l = tki.Label(app, text='Durasi antar SS (Detik) ?')
    l.grid(row=0, column=0, sticky=tki.E, padx=3, pady=3)

    e = tki.Entry(app, textvariable=var)
    e.grid(row=0, column=1, columnspan=2, padx=3, pady=3)

    l2 = tki.Label(app, text='Berapa Kali SS dalam sekali Jalan ?')
    l2.grid(row=1, column=0, sticky=tki.E, padx=3, pady=3)

    e2 = tki.Entry(app, textvariable=var2)
    e2.grid(row=1, column=1, columnspan=2, padx=3, pady=3)

    l3 = tki.Label(app, text='Refreshing setelah script berjalan (Detik) ?')
    l3.grid(row=2, column=0, sticky=tki.E, padx=3, pady=3)

    e3 = tki.Entry(app, textvariable=var3)
    e3.grid(row=2, column=1, columnspan=2, padx=3, pady=3)

    b1 = tki.Button(app, text='Reset', command=kosong, activebackground='red')
    b1.grid(row=3, column=1, padx=3, pady=3, sticky=tki.N+tki.S+tki.E+tki.W)

    b2 = tki.Button(app, text='Mulai', command=mulai,
                    activebackground='black', activeforeground='white')
    b2.grid(row=3, column=2, padx=3, pady=3, sticky=tki.N+tki.S+tki.E+tki.W)

    # def mulai():
    #     # tm.showinfo('Info', 'Halo Mas Bro !')

    #     time.sleep(int(input('Jeda antar screenshot (Detik) ?\t')))

    #     for i in range(int(input('Berapa Kali Screenshot ?\t'))):
    #         filename = 'screenshot ' + str(i) + '.png'

    #         tampil = print('File ' + filename +' sedang dibuat . . .')

    #         tm.showinfo('Info Mas Bro !', tampil)

    #         shot = pag.screenshot()
    #         shot.save(filename)

    #         time.sleep(1)

    # btn = tki.Button(app, text='Start', state=tki.NORMAL, command=mulai)
    # btn.grid(sticky=tki.E+tki.S, padx=90, pady=120)

    app.mainloop()


if __name__ == "__main__":
    main()
