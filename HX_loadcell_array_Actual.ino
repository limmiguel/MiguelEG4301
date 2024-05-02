//
//    FILE: HX_loadcell_array.ino
//  AUTHOR: Rob Tillaart
// PURPOSE: HX711 demo
//     URL: https://github.com/RobTillaart/HX711
//
//  TODO: test with hardware

#include "HX711.h"

int Inflate[9] = {18, 20, 22, 24, 26, 28, 30, 32, 34};
int Deflate[9] = {19, 21, 23, 25, 27, 29, 31, 33, 35};
int Valve[9] = {10, 9 ,8 ,7 ,6 ,5 ,4 ,3 , 2};
int Order[9] = {4,1,2,5,8,7,6,3,0}
HX711 scale0;
HX711 scale1;
HX711 scale2;
HX711 scale3;
HX711 scale4;
HX711 scale5;
HX711 scale6;
HX711 scale7;
HX711 scale8;

HX711 scales[9] = { scale0, scale1, scale2, scale3, scale4, scale5, scale6, scale7, scale8 };

const uint8_t dataPin[9] = { 36, 38, 40, 42, 44, 46, 48, 50, 52 };
const uint8_t clockPin[9] = {37, 39, 41, 43, 45, 47, 49, 51, 53};

// TODO you need to adjust to your calibrate numbers
float calib[9] = { 420.0983, 421.365, 419.200, 410.236, 420.0983, 421.365, 419.200, 410.236, 420.920 };

uint32_t count = 0;

void setup()
{
  Serial.begin(115200);
  for (int i = 2; i < 36; i++)
  {
    pinMode(i,OUTPUT);
  }

  for (int i = 0; i < 9; i++)
  {
    scales[i].begin(dataPin[i], clockPin[i]);
    scales[i].set_scale(calib[i]);
    // reset the scale to zero = 0
    scales[i].tare();
  }
}

void loop()
{
  Serial.print(count);
  for (int i = 0; i < 9; i++)
  {
    Serial.print("\t");
    Serial.print(scales[i].get_units(5));
    if ((scales[i].get_units(5)) <= 3000) {
  digitalWrite(Inflate[i], HIGH);
  } else { if ((scales[i].get_units(5)) >= 10000) {
  digitalWrite(Valve[i], HIGH);
  digitalWrite(Inflate[i],LOW);

  } else {
    digitalWrite(Valve[i],LOW);
    digitalWrite(Inflate[i],LOW);

  }
   count++;
  }
  Serial.println();
}
}

//  -- END OF FILE --
