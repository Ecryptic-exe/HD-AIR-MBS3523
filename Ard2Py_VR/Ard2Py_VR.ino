int VR;

void setup() {
  pinMode (A0, INPUT);
  Serial.begin (115200);
  

}

void loop() {
  VR = analogRead (A0);
  Serial.println(VR);
  delay(100);
}
