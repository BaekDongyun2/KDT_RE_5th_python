// 아두이노 I2C 통신 표준 라이브러리 사용
 #include <Wire.h>

// MPU-6050dml I2C 주소 저장
const int MPU = 0x68;

/*
- int16_6: 16비트 정수형 변수를 선언하기 위한 자료형
  16비트 정수형 자료형을 변수로 선언하는 이유: 자이로 센서가 데이터를 16비트(2바이트)로 보내기 때문
- AcX, AcY, AcZ
- GyX, GyY, GyZ
- Temp
*/

int16_t AcX, AcY, AcZ, Temp, GyX, GyY, GyZ;


void setup() {
  Serial.begin(9600);

  Wire.begin(); // 아두이노 I2C 통신 기능 활성화
  Wire.beginTransmission(MPU); // I2C 통신 시작 + 어떤 센서와 통신할지 주소로 지어
  Wire.write(0x6B); // 0x6B라는 레지스터로 내부 포인터 이동
  Wire.write(0); // 해당 레지스터 값을 0으로 쓰기
  Wire.endTransmission(true); // 명령 전송 완료 시 I2C 통신 종료
}

void loop() {
  Wire.beginTransmission(MPU);
  Wire.write(0x3B); // 0x3B라는 레지스터에 센서 데이터 저장 시작
  Wire.endTransmission(false); // 0x3B 레지스터 연결 유지 (Stop 조건)

  Wire.requestFrom(MPU, 14, true); // 실제 데이터 읽기 시작
  // 파라미터: (0x68 주소 장치에게, 14 바이트 읽어오기, 모두 읽었으면 Stop 조건 전송)

  /*
  자이로센서는 하나의 센서 값을 2바이트(16비트)로 전송
  하지만 아두이노 I2C 통신을 한 번에 1바이트만 통신이 가능
  그래서 1바이트씩 두 번 값을 읽어와서 두 바이트를 합쳐서 저장

  <<: 비트를 왼쪽으로 이동시키는 연산자
    x << n
    x의 비트를 왼쪽으로 n칸 이동시키고, 오른쪽 빈 비트에는 0을 채움
      00010010 << 2 =< 01001000 이렇게 바뀜

  |: 비트를 합치는 연산자 (or 연산자이면서 비트를 조립할 때 이렇게 사용하기도 함) 
  */
  AcX = Wire.read() << 8 | Wire.read(); // 먼저 받아온 8비트를 왼쪽으로 여덟칸 옮기고, 다음 받아온 8비트를 합침
  AcY = Wire.read() << 8 | Wire.read();
  AcZ = Wire.read() << 8 | Wire.read();
  Temp = Wire.read() << 8 | Wire.read();
  GyX = Wire.read() << 8 | Wire.read();
  GyY = Wire.read() << 8 | Wire.read();
  GyZ = Wire.read() << 8 | Wire.read();

  /*
  이렇게 값을 그냥 지정할 수 있는 이유는 데이터를 읽어오는 지점을 지정했고, 
  해당 지점부터 XYZ 축 가속도, 센서온도, 자이로스코프 값이 순서대로 오기 때문
  시작 주소와 바이트 수를 정확하게 맞춰서 오기 때문에
  데이터를 읽어왔을 때  순서가 바뀌거가 무작위로 저장될 일 없이 사용 가능
  */

  Serial.print("AcX: ");
  Serial.print(AcX);
  Serial.print(" | ");
  Serial.print("AcY: ");
  Serial.print(AcY);
  Serial.print(" | ");
  Serial.print("AcZ: ");
  Serial.print(AcZ);
  Serial.print(" | ");
  Serial.print("Temp: ");
  Serial.print(Temp);
  Serial.print(" | ");
  Serial.print("GyX: ");
  Serial.print(GyX);
  Serial.print(" | ");
  Serial.print("GyY: ");
  Serial.print(GyY);
  Serial.print(" | ");
  Serial.print("GyZ: ");
  Serial.print(GyZ);
  Serial.println("");

  delay(2000);
}
