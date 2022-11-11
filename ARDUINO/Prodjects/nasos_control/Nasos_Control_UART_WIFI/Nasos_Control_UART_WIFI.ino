#include <Wire.h> 
#include <LiquidCrystal_I2C.h>


//int PotenciometrPin = A0;    // select the input pin for the potentiometer
//int Value=0;
//float Value_volt=0;
LiquidCrystal_I2C lcd(0x27,16,2);  // Устанавливаем дисплей
//  lcd.init();                     
//  lcd.backlight();// Включаем подсветку дисплея
//  lcd.print("iarduino.ru");
//  lcd.setCursor(4, 1);
//  lcd.print("Potenciometr");
//   delay(1000);

int downPin1 = 2; // к выводу 2 подключён геркон 1
int upPin2 = 3; // к выводу 3 подключён геркон 2
int alarmPin3 = 4; // к выводу 4 подключён геркон 3 

int ledPin = 13;
int flag = 0;

String str1 = "gerkon_down=";
String str2 = "gerkon_up=";
String str3 = "gerkon_alarm=";

String stat1 = "0";
String stat2 = "0";
String stat3 = "0";
String stat4 = "0";
String stat5 = "0";
String stat6 = "0";
String stat7 = "0";
String stat8 = "0";
String stat9 = "0";

String stat10 = "0";
String stat11 = "0";
String stat12 = "0";
String stat13 = "0";
String stat14 = "0";
String stat15 = "0";



int relay1_on_off = 5; // к выводу 5 подключено реле 1 
int relay2 = 6; // к выводу 6 подключено реле 2
int relay3_alarm = 7; // к выводу 7 подключено реле 3 
//int relay1_on_off_d = 8; // к выводу 5 подключено реле 1 
//int relay2_d = 9; // к выводу 6 подключено реле 2
//int relay3_alarm_d = 10; // к выводу 7 подключено реле 3 
int flag_d = 11;

int tempSensor = A0;
float  Value_volt=0;
float gradus=0;
int led_light = 0;

boolean buttonWasUp = true;
boolean ledEnabled = false;

void setup() {
  lcd.init();                      // initialize the lcd 
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  Serial.begin(9600); // задействуем последовательный порт
  
  pinMode(downPin1, INPUT); // задаём вывод 2 в качестве входа (будем считывать с него)
  pinMode(upPin2, INPUT); // задаём вывод 3 в качестве входа (будем считывать с него)
  pinMode(alarmPin3, INPUT); // задаём вывод 4 в качестве входа (будем считывать с него)
  digitalWrite(downPin1, HIGH); // активируем внутренний подтягивающий резистор вывода
  digitalWrite(upPin2, HIGH); // активируем внутренний подтягивающий резистор вывода
  digitalWrite(alarmPin3, HIGH); // активируем внутренний подтягивающий резистор вывода
  
  pinMode(relay1_on_off, OUTPUT);  // D5 как выход
  pinMode(relay2, OUTPUT);  // D6 как выход
  pinMode(relay3_alarm, OUTPUT);  // D7 как выход
//  pinMode(relay1_on_off_d, OUTPUT);//D8
//  pinMode(relay2_d, OUTPUT);//D9
//  pinMode(relay3_alarm_d, OUTPUT);//D10
  pinMode(flag_d, OUTPUT);//D11
  pinMode(ledPin, OUTPUT); // задаём вывод 13 в качестве выхода
  pinMode (tempSensor, INPUT);   
  pinMode(12, INPUT_PULLUP);
digitalWrite(relay3_alarm, 1);
     digitalWrite(relay1_on_off, 1);

}

void loop() {

    
  int g1 = digitalRead(downPin1); // считываем показания с геркона
  int g2 = digitalRead(upPin2); // считываем показания с геркона
  int g3 = digitalRead(alarmPin3); // считываем показания с геркона
  g1 = !g1; 
  g2 = !g2;
  g3 = !g3;

  boolean buttonIsUp = digitalRead(12);
  if (buttonWasUp && !buttonIsUp) {
      delay(10);
      buttonIsUp = digitalRead(12);
      if (!buttonIsUp) { 
         ledEnabled = !ledEnabled;
         if(ledEnabled){
          lcd.noDisplay();
          lcd.noBacklight();}
          else{lcd.display();
              lcd.backlight();}
         }
       }
      
   buttonWasUp = buttonIsUp;
//  Serial.println(g1);
  digitalWrite(ledPin, led_light); // инвертированные показания записываем в порт со светодиодом
  led_light = !led_light;
//  Serial.println(str1 + g1); // посылаем в последовательный порт значения с геркона
  stat1 = (str1 + g1);
  //когда геркон замкнут, значение "1" (HIGH), когда разомкнут - "0" (LOW)
//  Serial.println(str2 + g2); // посылаем в последовательный порт значения с геркона
  stat2 = (str2 + g2);
  //когда геркон замкнут, значение "1" (HIGH), когда разомкнут - "0" (LOW)
//  Serial.println(str3 + g3); // посылаем в последовательный порт значения с геркона
  stat3 = (str3 + g3);
  //когда геркон замкнут, значение "1" (HIGH), когда разомкнут - "0" (LOW)

   
   
   if (g1==1&&g2==1&&g3==1){//вкл вкл вкл 
//    {Serial.println("status= 1.1.1 ALARM!!!");     1 
    stat4 = "_1.1.1";
    lcd.clear();
    lcd.print("1.1.1 ALARM!!!");
   
     digitalWrite(relay3_alarm, 1);
     digitalWrite(relay1_on_off, 1);
     
     digitalWrite(flag_d, 0);
     flag = 1;
    }
    else if (g1==0&&g2==1&&g3==0){//вкл вкл выкл
//    {Serial.println("status= 1.1.0 ALARM!!!");      2
    stat4 = "_0.1.0";
    lcd.clear();
    lcd.print("1.1.0 ALARM!!!");
    
     digitalWrite(relay3_alarm, 1);
     digitalWrite(relay1_on_off, 1);

     digitalWrite(flag_d, 0);
     flag = 1;
    }
    else if (g1==0&&g2==0&&g3==1){// выкл выкл вкл 
//    {Serial.println("status= 0.0.1 ALARM!!!");          3
    stat4 = "_0.0.1";
    lcd.clear();
    lcd.print("0.0.1 ALARM!!!");
  
     digitalWrite(relay3_alarm, 1);
     digitalWrite(relay1_on_off, 1);
     digitalWrite(flag_d, 0);
     flag = 1;
    }
    else if (g1==0&&g2==1&&g3==1){// выкл вкл вкл 
//    {Serial.println("status= 0.1.1 ALARM!!!");           4
    stat4 = "_0.1.1";
    lcd.clear();
    lcd.print("0.1.1 ALARM!!!");

     digitalWrite(relay3_alarm, 1);
     digitalWrite(relay1_on_off, 1);

     digitalWrite(flag_d, 0);
     flag = 1;
    }
     else if (g1==1&&g2==0&&g3==1){//вкл выкл вкл 
//    {Serial.println("status= 1.0.1 ALARM!!!");           5
    stat4 = "_1.0.1";
    lcd.clear();
    lcd.print("1.0.1 ALARM!!!");

     digitalWrite(relay3_alarm, 1);
     digitalWrite(relay1_on_off, 1);

     digitalWrite(flag_d, 0);
     flag = 1;
    }
    else if(g1==0&&g2==0&&g3==0) //набор воды
    {digitalWrite(relay3_alarm, 0);
     delay(300);
     digitalWrite(relay1_on_off, 0);
     digitalWrite(flag_d, 1);
//     Serial.println("status= Intake has begun, level low");       6
     stat4 = "Int_st";
     lcd.clear();
     lcd.print("Status = Intake ");
     lcd.setCursor(0, 1);
     lcd.print("   has begun");
     flag = 3;
    }
   else if(g1==1&&g2==1&&g3==0)//окончание набора воды
    {digitalWrite(relay3_alarm, 1);
     delay(300);
     digitalWrite(relay1_on_off, 1);
     digitalWrite(flag_d, 1);
//     Serial.println("status= Intake is over, level high");         7
     stat4 = "Int_en";
     lcd.clear();
     lcd.print("Intake is over,");
     lcd.setCursor(0, 1);
     lcd.print("  level high");
     flag = 4;
    }
   
   else if(g1==1&&g2==0&&g3==0)//Уровень в норме.          Проверить с этим условием и второй скобкой от {if(flag==0){ внизу!!!
    {
//      digitalWrite(relay3_alarm, 1);
//     delay(300);
//     digitalWrite(relay1_on_off, 1);
//     if(flag==0){
//      Serial.println("status= Status temporarily unknown");
    stat4 = "L_norm";
    lcd.clear();
    lcd.print("Level is normal");
//    digitalWrite(relay3_alarm, 1);
//    delay(300);
//    digitalWrite(relay1_on_off, 1);
//                }
//    else if(flag==1){
////  Serial.println("status= flag1 ALARM!!!");
//     stat4 = "f1_ALA";
//     lcd.clear();
//     lcd.print("flag1 ALARM!!!");
////     digitalWrite(relay3_alarm, 1);
////     delay(300);
////     digitalWrite(relay1_on_off, 1);                
//}
//     else if(flag==3){
////      Serial.println("status= flag3 Intake has begun");
//     stat4 = "f3_I_s";
//     lcd.clear();
//     lcd.print("Flag 3 Intake");
//     lcd.setCursor(0, 1);
//     lcd.print("  has begun");  
//       
//                     }
//     else if(flag==4){
////      Serial.println("status= flag4 Intake is over");
//     stat4 = "f4_I_e";
//     lcd.clear();
//     lcd.print("Flag 4 Intake ");
//     lcd.setCursor(0, 1);
//     lcd.print("  is over");
//                     }
//    else{
////      Serial.println("status= Status be updated by flag");
//     stat4 = "upbyfl";
//     lcd.clear();
//     lcd.print("Status be");
//     lcd.setCursor(0, 1);
//     lcd.print("updated by flag");
//////     digitalWrite(relay3_alarm, 1);
//////     delay(300);
//////     digitalWrite(relay1_on_off, 1);
//}
    }
//    Serial.println("Position relay1_on_off= " + String(digitalRead(relay1_on_off)));
      int alpha = digitalRead(relay1_on_off);
      alpha = !alpha;
    stat5 = "r1=" + String(alpha);
//    Serial.println("Position relay2= " + String(digitalRead(relay2)));
      int beta = digitalRead(relay2);
      beta = !beta;
    stat6 = "r2=" + String(beta);
//    Serial.println("Position relay3_alarm= " + String(digitalRead(relay3_alarm)));
      int gamma = digitalRead(relay3_alarm);
      gamma = !gamma;
    stat7 = "r3=" + String(gamma);

//    Serial.println(stat1 + "\r\n" + stat2 + "\r\n" + stat3 + "\r\n" + stat4 + "\r\n" + stat5 + "\r\n" + stat6 + "\r\n" + stat7); 
    Serial.println(stat1 + ";" + stat2 + ";" + stat3 + ";" + stat4 + ";" + stat5 + ";" + stat6 + ";" + stat7); 
//  
    delay(1000); // повторяем цикл через 1000 мсек 
    }

  
 
