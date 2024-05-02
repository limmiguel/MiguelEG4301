
int i = 0;
int Inflate[9] = {18, 20, 22, 24, 26, 28, 30, 32, 34};
int Deflate[9] = {19, 21, 23, 25, 27, 29, 31, 33, 35};
int Valve[9] = {10, 9 ,8 ,7 ,6 ,5 ,4 ,3 , 2};
int Order[9] = {4,1,2,5,8,7,6,3,0};
int cycle = 5000;

// TODO you need to adjust to your calibrate numbers


void setup()
{
  Serial.begin(115200);
  for (int i = 2; i < 36; i++)
  {
    pinMode(i,OUTPUT);
  }
}

void loop()
{
  for (int x = 0; x < 9; x++)
  { 
    i = Order[x];
  digitalWrite(Inflate[i], HIGH);
  delay(cycle);
  digitalWrite(Valve[i], HIGH);
  digitalWrite(Deflate[i], HIGH);
  digitalWrite(Inflate[i],LOW);
  delay(cycle);
  digitalWrite(Valve[i], LOW);
  digitalWrite(Deflate[i], LOW);  
  }
}


//  -- END OF FILE --
