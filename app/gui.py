import tkinter as tki  # Import Library tkinter


class Frame(tki.Frame):  # membuat class dengan nama Frame
    def __init__(self, master=None):
        tki.Frame.__init__(self, master)
        self.grid()
        self.kontrol()

    def kontrol(self):  # Melakukan Defining (Pendefinisian Fungsi). Nama Fungsinya "Kontrol"
        
        self.lbl = tki.Label(self)  # Buat Label dari Kolom Input
        self.lbl['text'] = "Durasi Jeda antar SS (Detik)"
        self.lbl.grid(row=0, column=0, sticky=tki.E+tki.N+tki.W+tki.S)

        self.lbl2 = tki.Label(self)  # Buat Label dari Kolom Input
        self.lbl2['text'] = "Berapa kali SS\t?"
        self.lbl2.grid(row=1, column=0, sticky=tki.E+tki.N+tki.W+tki.S)

        self.txt = tki.Entry(self)  # Buat Kolom Input (Form)
        self.txt['width'] = 40
        self.txt.grid(row=0, column=1, columnspan=2)

        self.txt2 = tki.Entry(self)  # Buat Kolom Input (Form)
        self.txt2['width'] = 40
        self.txt2.grid(row=1, column=1, columnspan=2)

        self.btn = tki.Button(self)  # Buat Tombol untuk menjalankan Script
        self.btn['text'] = 'Mulai'
        self.btn.grid(row=2, column=2)


def main():  # Melakukan Defining App dengan nama Fungsi "Main"
    app = Frame()  # Buat Frame App
    # Nambah Title App
    app.master.title('Auto Screenshot  |   PYT-3C (Kel. T)')
    app.mainloop()  # Menampilkan App nya


# untuk script dibawah ini sy lupa buat apaan. tapi sama instruktur sangat dianjurkan utk mengikut-sertakan script ini. Teman2 bisa bantu Googling nanti yah
if __name__ == '__main__':
    main()


# Selanjutnya, tinggal bagaimana meng-kawinkan Script yg ada di File script.py ke Gui ini

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
