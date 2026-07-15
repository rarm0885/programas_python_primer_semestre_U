import tkinter as tk

ventana = tk.Tk () 

#El titulo de la ventana
ventana.title("Mi primera ventana ")

#el aspecto y coordenadas
ventana.geometry("600x400+500+250")

#Lo max que se puede agrandar o minimizar
ventana.minsize(600,400 )
ventana.maxsize(600,400)

#Una imagen para la ventana 
ventana.iconbitmap("tkinter/imagen.jpg")

#Esto es la transparencia
ventana.attributes("-alpha", 0.9)

#El color
ventana.configure(bg="gray26")

#Que la ventana siempre este activa
ventana.mainloop()