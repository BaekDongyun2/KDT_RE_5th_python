void setup() {
  Serial.begin(9600);
  pinMode(7, OUTPUT);
}

void loop() {
  int resistor = analogRead(A0);
  digitalWrite(7, LOW);

  if(resistor < 700) {
    Serial.println("Light Off");
    digitalWrite(7, HIGH);
  }
  else {
    Serial.println("Light On");
  }
}
