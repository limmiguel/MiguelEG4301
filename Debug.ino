int Inflate[9] = {18, 20, 22, 24, 26, 28, 30, 32, 34};
int Deflate[9] = {19, 21, 23, 25, 27, 29, 31, 33, 35};
int Valve[9] = {10, 9 ,8 ,7 ,6 ,5 ,4 ,3 , 2};

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
  for (int i = 2; i < 36; i++)
  {
    pinMode(i,OUTPUT);
  }
  for (int i = 0; i < 9; i++)
  {
  digitalWrite(Inflate[i], HIGH);
  delay(5000);
  //digitalWrite(Valve[i], HIGH);
  //digitalWrite(Deflate[i], HIGH);
  digitalWrite(Inflate[i], LOW);
  //delay(10000);
  //digitalWrite(Valve[i], LOW);
  //digitalWrite(Deflate[i], LOW);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
delay(10000);
  
}
