#include <Servo.h>
Servo myServo;
int servoPIN = 9;
String servoPos;
int pos;

void setup() {
  Serial.begin(115200);
  myServo.attach(servoPIN);
  myServo.write(90);
  
}

void loop() {
  if(Serial.available()==0)
  {
   servoPos = Serial.readStringUntil('\r');
   pos = servoPos.toInt();
   myServo.write(pos) ;
   delay(100);
  }
}
