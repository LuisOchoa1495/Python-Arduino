import tkinter as tk
from PIL import ImageTk, Image
import serial

arduino=serial.Serial('COM5',9600,timeout=1)
ventana=tk.Tk()
ventana.geometry("300x370")
ventana.resizable(0,0)
ventana.title("PYTHON + ARDUINO")

#Texto
texto = tk.Label(ventana,text="MENSAJE EN PANTALLA LCD",font=("Arial", 12,"bold")).pack(pady=10)

#Imagen
imagen_led=Image.open("D:/EIGHTA/PYTHON+ARDUINO/3-LCD/Pantalla_LCD.png")
nueva_imagen=imagen_led.resize((200,100))
render=ImageTk.PhotoImage(nueva_imagen)
label_imagen= tk.Label(ventana, image= render)
label_imagen.image=render
label_imagen.pack(pady=5)

label = tk.Label(font=("Arial", 9,"bold"))  
#funcion enviar
def Enviar():  
    mensaje_lcd = ">>>Mensaje enviado: " + (mensaje.get())  
    label.config(text = mensaje_lcd)
    label.place(x=40,y=260) 
    
def Mensaje():
    print(f'{mensaje.get()}')
    texto=str(mensaje.get())
    arduino.write(texto.encode())

t=tk.StringVar()

#Caja de texto
mensaje = tk.Entry(textvariable=t,width=30)
mensaje.pack(pady=5)

#Boton enviar
boton_enviar = tk.Button(text="Enviar Mensaje", command=lambda:[Enviar(),Mensaje()],height=2,width=20,bg="green",fg="white",font=("Arial", 9,"bold"))  
boton_enviar.pack(pady=10) 

#boton cerrar
boton_cerrar=tk.Button(text="Cerrar",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Arial", 9,"bold"))
boton_cerrar.place(x=110,y=300)

ventana.mainloop()
arduino.close()