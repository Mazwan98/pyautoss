import tkinter.messagebox as tm
import tkinter as tki
import pyautogui as pag
import time
from datetime import date

def main():
    app = tki.Tk()
    app.title('Auto Screenshot  |   ( Kel. T )')
        
    
    def about():
        tm.showinfo('Tentang Aplikasi', 'Tugas Project Kelas PYT - 3C DTS Kemenkominfo at Cisco (Kelompok T) :\n1. Sulistiawan A P\n2. Yusuf Bagaskoro\n3. Bernad Wayu')
    
    menubar = tki.Menu(app, tearoff=0, selectcolor='black')
    menubar.add_command(label='Tentang', command=about)
    

    var = tki.IntVar()
    var.set(1)

    var2 = tki.IntVar()
    var2.set(2)

    var3 = tki.IntVar()
    var3.set(1)

    def reset():
        var.set('')
        var2.set('')
        var3.set('')

    def mulai():

        time.sleep(var.get())

        for i in range(var2.get()):
            
            today = date.today()

            filename = 'screenshot ' + str(today) + ' ' + str(i) + '.png'
            folder = r'D:\Project Python\pyautoss\app\hasil' + '\\' + filename
            
            try:
                info = tki.Label(app, text='File ' + filename +
                                ' dibuat . . .', bg='black', fg='green')
                info.grid(row=3, column=0, padx=3, pady=3)
                
                shot = pag.screenshot()
                shot.save(folder)

                time.sleep(var3.get())
                
                
            except:
                info = tki.Label(app, text='Ups .. Ada yang salah ( Error ) saat menyimpan ' + filename , bg='black', fg='green')
                info.grid(row=3, column=0, padx=3, pady=3)


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

    b1 = tki.Button(app, text='Reset', command=reset, activebackground='red')
    b1.grid(row=3, column=1, padx=3, pady=3, sticky=tki.N+tki.S+tki.E+tki.W)

    b2 = tki.Button(app, text='Mulai', command=mulai,
                    activebackground='black', activeforeground='white')
    b2.grid(row=3, column=2, padx=3, pady=3, sticky=tki.N+tki.S+tki.E+tki.W)

    app.config(menu=menubar)
    app.mainloop()

if __name__ == "__main__":
    main()
