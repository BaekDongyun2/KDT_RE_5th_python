#define TRIG 9
#define ECHO 8
#define PIEZO 12
#define LED 11


void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(PIEZO, OUTPUT);
  pinMode(LED, OUTPUT);
}

void loop() {

  digitalWrite(TRIG, HIGH);
  delay(10);
  digitalWrite(TRIG, LOW);
  
  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/1000000)/2;
  Serial.println(distance);
  Serial.println("cm");
  delay(100);

  if (distance < 100) {
    Serial.println("물체가 가까워짐");
    digitalWrite(PIEZO, HIGH);
    digitalWrite(LED, HIGH);
  }
  else {
    digitalWrite(PIEZO, LOW);
    digitalWrite(LED, LOW);
  }
  delay(100);
}
                                                                 