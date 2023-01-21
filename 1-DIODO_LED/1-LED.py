import tkinter as tk
from PIL import ImageTk, Image
import serial
#pip install pyserial

arduino=serial.Serial('COM5',9600,timeout=1)
ventana=tk.Tk()
ventana.geometry("300x200")
ventana.resizable(0,0)
ventana.title("PYTHON + ARDUINO")

#imagen led
def imagen_led_encendido():
    imagen_led=Image.open("D:/EIGHTA/PYTHON+ARDUINO/1-DIODO_LED/led_encendido.png")
    nueva_imagen=imagen_led.resize((120,120))
    render=ImageTk.PhotoImage(nueva_imagen)

    label_imagen= tk.Label(ventana, image= render)
    label_imagen.image=render
    label_imagen.place(x=40,y=40)
    
def imagen_led_apagado():
    imagen_led=Image.open("D:/EIGHTA/PYTHON+ARDUINO/1-DIODO_LED/led_apagado.png")
    nueva_imagen=imagen_led.resize((120,120))
    render=ImageTk.PhotoImage(nueva_imagen)

    label_imagen= tk.Label(ventana, image= render)
    label_imagen.image=render
    label_imagen.place(x=40,y=40)

def encender():
    print("ENCENDER")
    arduino.write(b'e')

def apagar():
    print("APAGAR")
    arduino.write(b'a')    
    

#texto
texto = tk.Label(ventana,text="DIODO LED",font=("Arial", 12))
texto.place(x=60,y=15)

#boton encender
boton_encender=tk.Button(text="Encender",command= lambda:[imagen_led_encendido(),encender()],height=2,width=10)
boton_encender.place(x=200,y=40)
#boton apagar
boton_apagar=tk.Button(text="Apagar",command=lambda:[imagen_led_apagado(),apagar()] ,height=2,width=10)
boton_apagar.place(x=200,y=100)


ventana.mainloop()
arduino.close()