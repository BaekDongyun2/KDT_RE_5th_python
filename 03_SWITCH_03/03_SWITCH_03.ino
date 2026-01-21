int switch1 = 11;
int switch2 = 12;
int led1 = 3;
int led2 = 4;


void setup() {
  Serial.begin(9600);
  pinMode(switch1, INPUT_PULLUP); // 기본 상태가 1(HIGH, 5V), 스위치가 눌렸을 대 0(LOW, 0V)
  pinMode(switch2, INPUT_PULLUP);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  int pb1 = digitalRead(switch1);
  int pb2 = digitalRead(switch2);
  
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);

  if(pb1 == LOW) {
    Serial.print("Switch: Red");
    digitalWrite(led1, HIGH);
  }

  if(pb2 == LOW) {
  Serial.print("Switch: Blue");
  digitalWrite(led2, HIGH);
  }
  delay(100);

}
