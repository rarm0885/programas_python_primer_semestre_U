import tkinter as tk
ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("600x400")

frame1 = tk.Frame(ventana)
frame1.configure(width=400, height=200, bg="red", bd=5 )
frame1.pack()

#siempre se pone el .pack
boton = tk.Button(frame1,text=("HOLA DORMILONCITAAAA"))
boton.pack()


ventana.mainloop()
 