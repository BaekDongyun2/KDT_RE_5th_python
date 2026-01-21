int pb = 12;

void setup() {
  Serial.begin(9600);
  pinMode(pb, INPUT_PULLUP); // 기본 상태가 1(HIGH, 5V), 스위치가 눌렸을 대 0(LOW, 0V)
}

void loop() {
  int pbState = digitalRead(pb);
  Serial.println(pbState);
  delay(500);
}
