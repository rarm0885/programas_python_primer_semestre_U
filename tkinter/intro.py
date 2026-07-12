import tkinter as tk

ventana = tk.Tk () 

ventana.title("Mi primera ventana ")
ventana.geometry("600x400+500+250")
ventana.minsize(600,400 )
ventana.maxsize(600,400)
ventana.iconbitmap("tkinter/imagen.jpg")

ventana.attributes("-alpha", 0.9)

ventana.configure(bg="gray26")

ventana.mainloop()