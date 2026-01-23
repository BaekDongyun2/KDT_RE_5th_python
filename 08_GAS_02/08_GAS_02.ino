#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
#define GAS_AO A0
#define GAS_DO 8
#define LED 13
#define PIEZO 12

DHT myDHT(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  myDHT.begin();
  pinMode(GAS_AO, INPUT);
  pinMode(GAS_DO, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(PIEZO, OUTPUT);
  Serial.println("히터 가열 시작");
  delay(1000);
  Serial.println("히터 가열 종료 동작 시작");
}

void loop() {
  delay(2000);
  float h = myDHT.readHumidity(); // 습도값 읽어옴
  float c = myDHT.readTemperature(); // 섭씨 온도값 읽어옴
  float f = myDHT.readTemperature(true); // 화씨 온도값 읽어옴

  digitalWrite(PIEZO, LOW);
  digitalWrite(LED, LOW);

  float sensorValue = analogRead(GAS_AO);
  int sensorDValue = digitalRead(GAS_DO);

  Serial.print("아날로그 센서 입력: ");
  Serial.println(sensorValue);

  Serial.println("디지털 센서 입력: ");
  Serial.print(sensorDValue);

  // 측정 실패 시 예외처리
  if (isnan(h) || isnan(c) || isnan(f)) {
    Serial.println("값을 읽어오지 못했습니다.");
    return; // 아래 코드를 실행시키지 않기 위해 loop 함수 자체를 나감
  }

  if(sensorValue > 450) {
    Serial.println("!! 연기 감지 !!");
    digitalWrite(PIEZO, HIGH);
    digitalWrite(LED, HIGH);
  }

  // 정상 측정이 되었을 때 실행되는 코드
  Serial.println("습도: ");  
  Serial.println(h);  
  Serial.println("섭씨온도: ");  
  Serial.println(c);  
  Serial.println("화씨온도: ");  
  Serial.println(f);  

  delay(1000);




}
