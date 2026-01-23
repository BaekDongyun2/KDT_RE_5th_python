#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT

DHT myDHT(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  myDHT.begin();
}

void loop() {
  delay(2000);
  float h = myDHT.readHumidity(); // 습도값 읽어옴
  float c = myDHT.readTemperature(); // 섭씨 온도값 읽어옴
  float f = myDHT.readTemperature(true); // 화씨 온도값 읽어옴
  
  // 측정 실패 시 예외처리
  if (isnan(h) || isnan(c) || isnan(f)) {
    Serial.println("값을 읽어오지 못했습니다.");
    return; // 아래 코드를 실행시키지 않기 위해 loop 함수 자체를 나감
  }

  // 정상 측정이 되었을 때 실행되는 코드
  Serial.println("습도: ");  
  Serial.println(h);  
  Serial.println("섭씨온도: ");  
  Serial.println(c);  
  Serial.println("화씨온도: ");  
  Serial.println(f);  

}
