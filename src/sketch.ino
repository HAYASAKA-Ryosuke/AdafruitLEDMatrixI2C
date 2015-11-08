#include <Wire.h>
#define HT16K33_CMD_BRIGHTNESS 0xE0
uint16_t displaybuffer[8]; 
uint8_t address = 0x70;

int bitmap[] = {
 0,0,0,0,0,0,0,0,//0-7 -> 56-63
 0,0,0,0,0,0,0,0,//8-15 -> 0-7
 0,0,0,0,0,0,0,0,//16-23 -> 8-15
 0,0,0,0,0,0,0,0,//24-31 -> 16-23
 0,0,0,0,0,0,0,0,//32-39 -> 24-31
 0,0,0,0,0,0,0,0,//40-47 -> 32-39
 0,0,0,0,0,0,0,0,//48~55 -> 40-47
 0,0,0,0,0,0,0,0};//56~63 -> 0-8

int get_array[] = {
 0,1,1,1,1,1,1,0,
 1,0,0,0,0,0,0,1,
 1,0,0,0,0,0,0,1,
 1,0,0,0,0,0,0,1,
 1,0,0,0,0,0,0,1,
 1,0,0,0,0,0,0,1,
 1,0,0,0,0,0,0,1,
 0,1,1,1,1,1,1,0};
void setup()
{
   ledbegin(0x70, 10);
}

void loop()
{
    ledmatrixclear();      // clear display
    setBitmap();
    writeDisplay();  // write the changes we just made to the display
    delay(500);
}
void setBrightness(uint8_t b) {
  if (b > 15) b = 15;
  Wire.beginTransmission(address);
  Wire.write(HT16K33_CMD_BRIGHTNESS | b);
  Wire.endTransmission();  
}
void blinkRate() {
  Wire.beginTransmission(address);
  Wire.write(0x81); 
  Wire.endTransmission();
}
void ledbegin(int address, int brightness){
  Wire.begin();

  Wire.beginTransmission(address);
  Wire.write(0x21);  // turn on oscillator
  Wire.endTransmission();
  blinkRate();
  
  setBrightness(brightness); // max brightness

}

void ledmatrixclear(void) {
  for (uint8_t i=0; i<8; i++) {
    displaybuffer[i] = 0;
  }
}
void drawPixel(uint8_t x, uint8_t y, uint16_t color) {
  if ((y < 0) || (y >= 8)) return;
  if ((x < 0) || (x >= 16)) return;
  displaybuffer[y] |= 1 << x;
}

void writeDisplay(void) {
  Wire.beginTransmission(address);
  Wire.write((uint8_t)0x00); // start at address $00

  for (uint8_t i=0; i<8; i++) {
    Wire.write(displaybuffer[i] & 0xFF);    
    Wire.write(displaybuffer[i] >> 8);    
  }
  Wire.endTransmission();  
}

void trans(){
    for(int i=0; i<8; i++)
        bitmap[56+i] = get_array[i];
    for(int i=8; i<64; i++)
        bitmap[i-8] = get_array[i];
}

void setBitmap(){
    trans();
    for(int i=0; i < 8; i++){
        for(int j=0; j < 8; j++){
              if(bitmap[8*i+j]==1){
                  drawPixel(i, j, 1);
              }
        }
     }
}
