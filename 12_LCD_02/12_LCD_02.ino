#include <LiquidCrystal_I2C.h> // 외부 라이브러리 불러오기
#include <Servo.h>

LiquidCrystal_I2C myLCD(0x27, 16, 2);
Servo myServo;
int angle = 0;

void setup() {
  myLCD.init();
  myLCD.backlight();

  Serial.begin(9600);
  myServo.attach(10);
}

void loop() {
  int val = analogRead(A0);
  angle = map(val, 0, 1023, 0, 180);

  myServo.write(angle);
  
  myLCD.setCursor(0, 0); 
  myLCD.print("angle: ");
  myLCD.print(angle);
  delay(100);

  myLCD.clear();
}
