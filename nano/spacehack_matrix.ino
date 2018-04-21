#include "LedControl.h"

#define MAX_FRAMES 50

// Data, Clock, Chip Select, 1 board
LedControl lc=LedControl(12,11,10,1);

int frame_delay[MAX_FRAMES];
int frame_bright[MAX_FRAMES];
byte frames[MAX_FRAMES][8];
int n_frames = 0;

byte readHexByte() {
  byte b=0;
  for(int i=0; i<2; ++i)
  {
    b <<= 4;
    byte n;
    Serial.readBytes(&n, 1);
    if(n >= '0' && n <= '9')      b += n - '0';
    else if(n >= 'a' && n <= 'f') b += n - 'a' + 10;
    else if(n >= 'A' && n <= 'F') b += n - 'A' + 10;
    else --i;
  }

  return b;
}

void receiveFrameData() {
  int f;
  int x;

  for(f=0; f < MAX_FRAMES; ++f){
    x = Serial.parseInt();
    frame_delay[f] = constrain(x, 0, 10000);
    if(frame_delay[f] == 0)
      break;

    x = Serial.parseInt();
    frame_bright[f] = constrain(x, 0, 15);

    for(int r=0; r<8; ++r)
      frames[f][r] = readHexByte();

    while(Serial.read() != '\n');
  }

  while(Serial.available()) Serial.read();

  n_frames = f;
  Serial.print("Received ");
  Serial.print(n_frames);
  Serial.print(" frames\n");
}

void setFrame(int f) {
  lc.setIntensity(0,frame_bright[f]);
  
  for(int r=0; r<8; ++r)
    lc.setRow(0, r, frames[f][r]);
}

void setup() {
  Serial.begin(9600, SERIAL_8N1);
  lc.shutdown(0,false);
}

void loop() {
  if(Serial.available())
    receiveFrameData();

  for(int f=0; !Serial.available() && f<n_frames; ++f)
  {
    setFrame(f);
    for(int t=frame_delay[f]; !Serial.available() && t>0; --t)
      delay(1);
  }
}

