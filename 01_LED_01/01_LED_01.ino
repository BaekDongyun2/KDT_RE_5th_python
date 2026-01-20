int LED_Pin = 3; // 사용할 핀 번호를 변수화 (A를 붙이면 아날로그, 없으면 디지털)

void setup() {
  pinMode(LED_Pin, OUTPUT); // 디지털 3번 핀을 출력으로 사용한다고 정의
}

void loop() {
  digitalWrite(LED_Pin, HIGH);  // 3번 핀을 HIGH로 출력 => LED 켜짐
  delay(1000);                      // LED가 켜진 상태로 1초 중지
  digitalWrite(LED_Pin, LOW);   // 3번 핀을 LOW로 출력 => LED 꺼짐
  delay(1000);                      // LED가 꺼진 상태로 1초 중지
}