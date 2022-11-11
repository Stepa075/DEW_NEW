#include <Wire.h> 
#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal_I2C.h>
// контакты
#define SS_PIN 2
#define RST_PIN 0
//#include <LCD_ST7032.h>

LiquidCrystal_I2C lcd(0x27,16,2);


// Создание экземпляра объекта MFRC522
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Создание экземпляра MFRC522

void setup() {
  Serial.begin(9600);
  SPI.begin();
  
  
  
  // инициализация MFRC522
  mfrc522.PCD_Init();
  
  // выводим номер версии прошивки ридера
  mfrc522.PCD_DumpVersionToSerial();
  lcd.init();                      // initialize the lcd 
  lcd.init();
  // Print a message to the LCD.
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Hello!");
  
}

void loop() {


  // Ожидание
  if ( ! mfrc522.PICC_IsNewCardPresent())
    return;

  // чтение
  if ( !mfrc522.PICC_ReadCardSerial())
    return;
//lcd.setCursor(0, 0);
//lcd.print("ALEX");
  // вывод данных
  lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("UID= ");
    lcd.setCursor(0,1);
    lcd.print("Hello!"); 
  Serial.print("UID DEC= ");
  view_data(mfrc522.uid.uidByte, mfrc522.uid.size);
//  Serial.println();
//  Serial.print("type = ");
//  byte piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
//  Serial.print(mfrc522.PICC_GetType(piccType));
  Serial.println();

  Serial.print("UID HEX= ");
  view_hex(mfrc522.uid.uidByte, mfrc522.uid.size);
  Serial.println();
  Serial.print("type = ");
  MFRC522::PICC_Type piType = mfrc522.PICC_GetType(mfrc522.uid.sak);
      Serial.println(mfrc522.PICC_GetTypeName(piType));

  Serial.println();
  delay(1000);
}

// преобразование в HEX
void view_data (byte *buf, byte size) {
  for (byte j = 0; j < size; j++) {
//    Serial.print(buf [j]);
    Serial.print(buf [j], DEC);
//    lcd.clear();
//    lcd.setCursor(0,0);
//    lcd.print("UID= ");
//    lcd.setCursor(0,1);
//    lcd.print(buf [j], DEC);
  }
}
void view_hex (byte *buf, byte size) {
  
  lcd.clear();
  for (byte j = 0; j < size; j++) {
//    Serial.print(buf [j]);
    Serial.print(buf [j], HEX);
    lcd.print(buf [j], DEC);
  }
  
}
