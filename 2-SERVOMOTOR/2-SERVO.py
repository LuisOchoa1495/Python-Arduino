import tkinter as tk
from PIL import ImageTk, Image

ventana=tk.Tk()
ventana.geometry("300x410")
ventana.resizable(0,0)
ventana.title("PYTHON + ARDUINO")

#Texto
texto = tk.Label(ventana,text="CONTROL DE SERVOMOTOR",font=("Arial", 12,"bold"))
texto.place(x=35,y=15)

#Imagen
imagen_led=Image.open("D:/EIGHTA/PYTHON+ARDUINO/2-SERVOMOTOR/servo.jpg")
nueva_imagen=imagen_led.resize((150,150))
render=ImageTk.PhotoImage(nueva_imagen)
label_imagen= tk.Label(ventana, image= render)
label_imagen.image=render
label_imagen.place(x=75,y=50)

label = tk.Label(font=("Arial", 9,"bold"))  
#funcion enviar
def Enviar():  
   angulo = "Angulo Servomotor = " + str(valor_servo.get())  
   label.config(text = angulo)
   label.place(x=80,y=310) 

#Valor a enviar - arduino     
valor_servo = tk.IntVar()

#Crear slider 0-180
scale = tk.Scale(variable = valor_servo, from_ = 0, to = 180, orient = "horizontal",length=220)
scale.place(x=40,y=200)

#Boton enviar
boton_enviar = tk.Button(text="Enviar", command=Enviar,height=2,width=10,bg="green",fg="white",font=("Arial", 9,"bold"))  
boton_enviar.place(x=110,y=250) 

#boton cerrar
boton_cerrar=tk.Button(text="Cerrar",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Arial", 9,"bold"))
boton_cerrar.place(x=110,y=350)

ventana.mainloop()
#arduino.close()