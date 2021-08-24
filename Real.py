import tkinter as tki
# from tkinter import messagebox
import time

def main():
  app = tki.Tk()
  app.title('Auto Screenshot | PYT-3C (Kel. T)')
  # app.geometry('600x400')
  # app.configure(background="black")
  
  lbl2 = tki.Label(app, text='Input durasi Jeda antar SS dalam satuan Detik :')
  lbl2.grid(row=0, column=0, sticky=tki.E+tki.N+tki.W+tki.S)
  
  def klik():
    
    import pyautogui as pag
    
    durasi = time.sleep(input())
    ss = range(input())

    txt = tki.Entry(app, durasi)
    txt['width']=40
    txt.grid(row=0, column=1, columnspan=2)
      
    for i in ss:
      filename = 'screenshot ' + str(i) + '.png'
      print('File ' + filename + ' sedang dibuat')
      shot = pag.screenshot()
      
      shot.save(filename)
      
      ss
        
  btn = tki.Button(app, text="Mulai !", command=klik)
  btn.grid(row=2, column=2) 






    
  # tki.messagebox.showinfo("Halo",
  #                        "Halo %s, apa kabar ?" % (txt.get()))
    
  # lbl = tki.Label(app)
  # lbl['text'] = 'Sesuaikan terlebih dahulu Script-nya dgn kebutuhan.\nYang perlu anda sesuaikan adalah pada looping dengan Method "Range( )".\nInputkan angka berapa kali akan meng-Screenshoot didalam tanda kurung "Range( )".'
  # lbl.grid(row=0, column=0, sticky=tki.E+tki.N+tki.W+tki.S)
  # lbl.pack(padx=30, pady=20)
  
  # lbl2 = tki.Label(app, text='Input durasi Jeda antar SS dalam satuan Detik :')
  # lbl2.grid(row=0, column=0, sticky=tki.E+tki.N+tki.W+tki.S)
  # lbl2.pack()
  
  # code = time.sleep(input())
  # txt = tki.Entry(app, durasi)
  # txt['width']=40
  # txt.grid(row=0, column=1, columnspan=2)
  # txt.pack()


  btn = tki.Button(app, text="Mulai !", command=klik)
  btn.grid(row=2, column=2)
  # btn.pack(padx=30, pady=20)

  # Menampilkan App
  app.mainloop()

if __name__ == "__main__":
  main()
