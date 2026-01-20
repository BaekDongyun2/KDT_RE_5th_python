/*
Ctrl + N: 아두이노 새 스케치 열기

새로운 스케치를 열면 새로운 창이 열림

아두이노 IDE에서는 탭 방식이 아닌 여러 창을 사용하는 방식이기 때문

스케치 = 하나의 폴더
폴더 = 하나의 독립 프로젝트
=> 프로젝트마다 별도의 창이 생기고 사용하는 것

---------------------------------------------------------------------------------

폴더 = 하나의 독립 프로젝트
.ino 파일은 새로운 폴더 안에 생김

아두이노는 폴더 이름과 동일한 .ino 파일을 "메인 파일"로 간주함.
같은 폴더 안의 .ino 파일은 하나의 코드처럼 합쳐서 컴파일

즉, 하나의 스케치 폴더 안에는 .ino 파일이 여러 개 있으면 하나의 큰 코드로 인식

하나의 스케치 폴더 안에는 setup(), loop()가 단 하나씩만 존재해야 함.

*/

int RED = 12;
int BLUE = 10;
int GREEN = 11;

void setup() {
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

// 버전 1: 0.5초 마다 하나씩 켜지고, 꺼지는 코드
// void loop() {
//   digitalWrite(RED, HIGH); 
//   delay(500);
//   digitalWrite(GREEN, LOW); 
//   delay(500);
//   digitalWrite(BLUE, HIGH); 
//   delay(500);
//   digitalWrite(RED, LOW); 
//   delay(500); 
//   digitalWrite(GREEN, LOW); 
//   delay(500);
//   digitalWrite(BLUE, LOW); 
//   delay(500); 
// }

// 버전 2: 모든 LED가 켜진 뒤 0.5초 동안 유지하고, 모든 LED를 끈 뒤 0.5초 유지
void loop() {
  digitalWrite(RED, HIGH); 
  digitalWrite(GREEN, HIGH); 
  digitalWrite(BLUE, HIGH); 
  delay(500);
  digitalWrite(RED, LOW); 
  digitalWrite(GREEN, LOW); 
  digitalWrite(BLUE, LOW); 
  delay(500);
}
