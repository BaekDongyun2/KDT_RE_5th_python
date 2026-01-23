#include <MFRC522.h>
#include <SPI.h> // 단거리간 통신 방법 중 하나

#define RST_PIN 9
#define SS_PIN 10

MFRC522 myMFRC(SS_PIN, RST_PIN); // MFRC522 라이브러리를 사용해서 나만의 myMFRC객체 생성

int BLUE = 3;
int RED = 2;
int PIEZO = 4;

void setup() {
  Serial.begin(9600);
  SPI.begin(); // SPI 통신 초기화(실행)
               // SPU 통신: 하나의 MASTER(아두이노)와 다수의 SLAVE(종속적인 역할, RFID리터)간의 통신 방식

  pinMode(BLUE, OUTPUT);
  pinMode(RED, OUTPUT);
  pinMode(PIEZO, OUTPUT);
  
  myMFRC.PCD_Init(); // RFID 리더기 초기화(실헹)

  myMFRC.PCD_DumpVersionToSerial(); // 연결 확인용 버전 정보 출력 코드
  Serial.println("RFID 통신 준비 완료");
}

void loop() {
  // 예외처리
  // 1. 근처에 태그가 있는지 확인
  if (!myMFRC.PICC_IsNewCardPresent()) 
    return;

  // 2. 근처 태그의 UID 확인
  if (!myMFRC.PICC_ReadCardSerial()) 
    return;

  if (myMFRC.uid.uidByte[0] == 37 && myMFRC.uid.uidByte[1] == 77 && myMFRC.uid.uidByte[2] == 25 && myMFRC.uid.uidByte[3] == 2) {
    digitalWrite(BLUE, HIGH);
    digitalWrite(RED, LOW);
    digitalWrite(PIEZO, HIGH);
    delay(1000);
    digitalWrite(PIEZO, LOW);
    digitalWrite(BLUE, LOW);
  }
  
  else {
    digitalWrite(RED, HIGH);
    digitalWrite(BLUE, LOW);
    digitalWrite(PIEZO, HIGH);
    delay(300);
    digitalWrite(RED, LOW);
    digitalWrite(PIEZO, LOW);
    delay(100);
    digitalWrite(RED, HIGH);
    digitalWrite(PIEZO, HIGH);
    delay(300);
    digitalWrite(RED, LOW);
    digitalWrite(PIEZO, LOW);
  }

  }
