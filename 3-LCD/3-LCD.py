import tkinter as tk
from PIL import ImageTk, Image

ventana=tk.Tk()
ventana.geometry("300x370")
ventana.resizable(0,0)
ventana.title("PYTHON + ARDUINO")

#Texto
texto = tk.Label(ventana,text="MENSAJE EN PANTALLA LCD",font=("Arial", 12,"bold"))
texto.place(x=35,y=15)

#Imagen
imagen_led=Image.open("D:/EIGHTA/PYTHON+ARDUINO/3-LCD/Pantalla_LCD.png")
nueva_imagen=imagen_led.resize((200,100))
render=ImageTk.PhotoImage(nueva_imagen)
label_imagen= tk.Label(ventana, image= render)
label_imagen.image=render
label_imagen.place(x=50,y=60)

label = tk.Label(font=("Arial", 9,"bold"))  
#funcion enviar
def Enviar():  
    mensaje_lcd = "Mensaje enviado: " + str(mensaje.get())  
    label.config(text = mensaje_lcd)
    label.place(x=80,y=270) 


t=tk.StringVar()
t.set("Mensaje aqui")
#Caja de texto
mensaje = tk.Entry(textvariable=t,width=30)
mensaje.place(x=60,y=180)

#Boton enviar
boton_enviar = tk.Button(text="Enviar Mensaje", command=Enviar,height=2,width=20,bg="green",fg="white",font=("Arial", 9,"bold"))  
boton_enviar.place(x=75,y=210) 

#boton cerrar
boton_cerrar=tk.Button(text="Cerrar",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Arial", 9,"bold"))
boton_cerrar.place(x=110,y=300)

ventana.mainloop()
#arduino.close()