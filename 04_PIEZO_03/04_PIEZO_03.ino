const int piezo_pin = 8;
const int sw = 2;

void setup() {
  Serial.begin(9600);
  pinMode(piezo_pin, OUTPUT);
  pinMode(sw, INPUT_PULLUP);
}

void loop() {
  int swState = digitalRead(sw);
  digitalWrite(piezo_pin, LOW);

  if(swState == LOW) {
    Serial.println("BUZZ ON");
    digitalWrite(piezo_pin, HIGH);
  }
  else {
    Serial.println("BUZZ OFF");
  }
  delay(100);

}
