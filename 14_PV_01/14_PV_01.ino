const int PANEL_PIN = A0;
const int SW_PIN = 2;

// 가상 에너지 저장소
long energy = 0;

const long SELL_UNIT = 100; // 판매 단위

// 충전 스케일 조정
const int MAX_CHARGE_RATE = 50; // 전압이 5V일 때 +50씩 저장

void setup() {
  Serial.begin(9600);
  pinMode(SW_PIN, INPUT_PULLUP);
}

void loop() {
  // 태양광 패널 전압 읽어오기
  int raw = analogRead(PANEL_PIN);
  float voltage = (raw * 5.0) / 1023.0;

  // 전압 기반 충전 공식
  // gain = (전압비율)* 최대충전량
  int gain = (voltage / 5.0) * MAX_CHARGE_RATE;

  // 햇빛이 없어서 충전이 되지 않을 때의 예외처리
  if(gain > 0){
    energy += gain;
  }

  // 판매 버튼 눌림 감지
  bool prev = HIGH;
  bool curr = digitalRead(SW_PIN);

  if (prev == HIGH && curr == LOW) {
    Serial.println("판매요청 발생");

    if(energy >= SELL_UNIT) {
      energy -= SELL_UNIT;
      Serial.print("판매 성공 | 판매량: ");
      Serial.print(SELL_UNIT);
      Serial.print(" | 남은 에너지: ");
      Serial.println(energy);
    }
    else {
      Serial.print("판매 실패 | 저장된 에너지가 부족합니다. | 현재 에너지: ");
      Serial.print(energy);
    }
  }
  prev = curr;

  // 현재 상태 출력
  Serial.print("전압: ");
  Serial.print(voltage);
  Serial.print("V | 적립량: ");
  Serial.print(gain);
  Serial.print(" | 현재 저장된 에너지: ");
  Serial.print(energy);

  delay(1000);
}
