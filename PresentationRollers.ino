int Inflate[9] = {18, 20, 22, 24, 26, 28, 30, 32, 34};
int Deflate[9] = {19, 21, 23, 25, 27, 29, 31, 33, 35};
int Valve[9] = {10 ,9 ,8 ,7 ,6 ,5 ,4 ,3 ,2};
int start = 0;
int counter = 0;
int cycle = 15000;
int elapsed = 0;

const uint8_t dataPin[9] = { 36, 38, 40, 42, 44, 46, 48, 50, 52 };
const uint8_t clockPin[9] = {37, 39, 41, 43, 45, 47, 49, 51, 53};

void setup()
{
  Serial.begin(115200);
  for (int i = 2; i < 36; i++)
  {
    pinMode(i,OUTPUT);
    Serial.println(i);
  }

}

void loop()
{
digitalWrite(Inflate[0], HIGH);
digitalWrite(Inflate[1], HIGH);
digitalWrite(Inflate[2], HIGH);
delay(cycle);

digitalWrite(Inflate[0], LOW);
digitalWrite(Inflate[1], LOW);
digitalWrite(Inflate[2], LOW);
digitalWrite(Inflate[3], HIGH);
digitalWrite(Inflate[4], HIGH);
digitalWrite(Inflate[5], HIGH);
digitalWrite(Valve[0], HIGH);
digitalWrite(Valve[1], HIGH);
digitalWrite(Valve[2], HIGH);
delay(cycle);

digitalWrite(Inflate[3], LOW);
digitalWrite(Inflate[4], LOW);
digitalWrite(Inflate[5], LOW);
digitalWrite(Inflate[6], HIGH);
digitalWrite(Inflate[7], HIGH);
digitalWrite(Inflate[8], HIGH);
digitalWrite(Valve[0], LOW);
digitalWrite(Valve[1], LOW);
digitalWrite(Valve[2], LOW);
digitalWrite(Valve[3], HIGH);
digitalWrite(Valve[4], HIGH);
digitalWrite(Valve[5], HIGH);
delay(cycle);

digitalWrite(Inflate[6], LOW);
digitalWrite(Inflate[7], LOW);
digitalWrite(Inflate[8], LOW);
digitalWrite(Valve[3], LOW);
digitalWrite(Valve[4], LOW);
digitalWrite(Valve[5], LOW);
digitalWrite(Valve[6], HIGH);
digitalWrite(Valve[7], HIGH);
digitalWrite(Valve[8], HIGH);

delay(cycle);
digitalWrite(Valve[6], LOW);
digitalWrite(Valve[7], LOW);
digitalWrite(Valve[8], LOW);




}