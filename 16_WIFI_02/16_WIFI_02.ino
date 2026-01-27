#include <SoftwareSerial.h>

SoftwareSerial myESP(2, 3); // D2 = RX(ESP TX), D3 = TX(ESP RX)

// ESP 모듈 속도가 9600으로 바뀌었는지 확인
void setup() {
  Serial.begin(9600);
  myESP.begin(9600);
  Serial.println("================TEST================");
}

void loop() {
  if(myESP.available()) {
    Serial.write(myESP.read());
  }
  if(Serial.available()) {
   myESP.write(Serial.read());
  }
}


/*
AT+CWJAP="spreatics_gusan_cctv","spreatics*"
*/