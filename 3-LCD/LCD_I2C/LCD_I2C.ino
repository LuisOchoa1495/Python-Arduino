#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3F,16,2);

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.begin(16,2); 
}

void loop() {
  if(Serial.available()){
    lcd.clear();
    String c = Serial.readString();    
    //LINEA 1 
    lcd.setCursor(0,0);
    lcd.print(">>MENSAJE:");     
    //LINEA 2
    lcd.setCursor(0,1);
    lcd.print(c);
    }
}
