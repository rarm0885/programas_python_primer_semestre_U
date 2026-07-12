import tkinter as tk
ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("600x400")

labelframe = tk.LabelFrame(ventana, text="EYY MUY BUENAS A TODOSS GUAPISIMOS AQUI VEGETTA 777", bg="purple", padx=10, pady=10)
labelframe.configure(width=400, height=200)
labelframe.pack()

ventana.mainloop()