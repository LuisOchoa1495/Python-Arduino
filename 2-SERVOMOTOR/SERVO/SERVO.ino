#include<Servo.h>
Servo servo_motor;

String dataString = "";
bool dataComplete= false;
int data=0;

void setup() {
  servo_motor.attach(7);
  Serial.begin(9600);
}

void loop() {
  //Lectura 
  if(dataComplete){
    data = dataString.toInt();
  //Angulo servomotor
    servo_motor.write(data);
    dataString = "";
    dataComplete= false;
  }                  
}

//Recepción de datos Seriales
void serialEvent(){
  while(Serial.available()){ //Si existen datos seriales, leer a todos
    char inChar = (char)Serial.read();
    dataString += inChar;
    if(inChar == '\n'){
      dataComplete = true;
    }
  }
}