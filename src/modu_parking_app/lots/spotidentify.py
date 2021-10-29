int Buzzer = 7;    // 버저 핀을 7번에 연결
int Sensor = 9;    // 센서핀은 9번에 연결
int val;
 
void setup () {
  pinMode(Buzzer, OUTPUT);   // 버저를 출력으로 설정
  pinMode(Sensor, INPUT);    // 센서값을 입력으로 설정
}
 
void loop () {
  val = digitalRead(Sensor);  // 센서값 읽어옴
  if (val == HIGH) {          // 장애물 감지가 안되면
    noTone(7);                // 버저가 울리지 않는다
    delay(100);        
  }
  else {                    // 장애물이 감지되면
    tone(7, 220);             // 버저가 울린다
    delay(100);
  }
}
