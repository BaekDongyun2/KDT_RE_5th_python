int pb = 2;

void setup() {
  Serial.begin(9600);
  pinMode(pb, INPUT);
}

void loop() {
  int pbState = digitalRead(pb);
  Serial.println(pbState);
  delay(10);
}
