
String numberCall_1 = "+380975781595"; // Номер абонента №1 для звонка
String numberSMS_1 = "+380975781595"; // Номер абонента №1 для СМС (отличается только знаком +)

String numberCall_2 = "+380679378284"; // Номер абонента №2 для звонка
String numberSMS_2 = "+380679378284"; // Номер абонента №2 для СМС (отличается только знаком +)

String textZone_1 = "Alarm! Zone1";    // Свое название зоны ,  на латинице.
String textZone_2 = "Alarm! Zone2";    // Свое название зоны ,  на латинице.
String textZone_3 = "Alarm! Zone3";    // Свое название зоны ,  на латинице.
String textZone_4 = "Alarm! Zone4";    // Свое название зоны ,  на латинице.

#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3); 

#define pinSensor_0 4 
#define pinSensor_1 5 
#define pinSensor_2 6 
#define pinSensor_3 7 
#define pinSensor_4 8 

void initGSM(void) {
  delay(2000);                            
  mySerial.begin(9600);                   // Выставляем скорость общения с GSM-модулем 9600 Бод/сек.  
  mySerial.println("AT+CLIP=1");          
  delay(300);                             
  mySerial.println("AT+CMGF=1");          
  delay(300);                             
  mySerial.println("AT+CSCS=\"GSM\"");    
  delay(300);                             
  mySerial.println("AT+CNMI=2,2,0,0,0");  
  delay(300);                             
}

/* Отправка SMS */
void sendSMS(String text, String phone) {
  mySerial.println("AT+CMGS=\"" + phone + "\""); 
  delay(500);
  mySerial.print(text);                         
  delay(500);
  mySerial.print((char)26);       
  delay(2500);  
}


unsigned long timerTemp = 0;  
uint8_t hours = 0;            

uint8_t flagSensor_0 = 0;
uint8_t flagSensor_1 = 0;
uint8_t flagSensor_2 = 0;
uint8_t flagSensor_3 = 0;
uint8_t flagSensor_4 = 0;

void setup() {
  mySerial.begin(9600);
  initGSM(); 
  
  pinMode(pinSensor_0, INPUT);
  pinMode(pinSensor_1, INPUT);
  pinMode(pinSensor_2, INPUT);
  pinMode(pinSensor_3, INPUT);
  pinMode(pinSensor_4, INPUT);

  timerTemp = millis();
}

void loop() {
    if(millis() - timerTemp >= 3600000) {timerTemp = millis(); hours++;}

  if(hours >= 168) {// Меняем время контроля системы на свое,144 часа.кол-во часов .
    sendSMS(String("The system works normally.OK"), numberSMS_1); 
    delay(10000);                                  
    sendSMS(String("The system works normally.OK"), numberSMS_2); 
    delay(10000);                                  
    hours = 0;                                     
    timerTemp = millis();                         
  }
 
  if(flagSensor_0 == 0 && digitalRead(pinSensor_0) == 0) flagSensor_0 = 1; 
  if(flagSensor_1 == 0 && digitalRead(pinSensor_1) == 0) flagSensor_1 = 1; 
  if(flagSensor_2 == 0 && digitalRead(pinSensor_2) == 0) flagSensor_2 = 1; 
  if(flagSensor_3 == 0 && digitalRead(pinSensor_3) == 0) flagSensor_3 = 1;
  if(flagSensor_4 == 0 && digitalRead(pinSensor_4) == 0) flagSensor_4 = 1;

  if(flagSensor_0 == 1) {
    String command;

    command = "ATD+" + numberCall_1 + ";";  
    mySerial.println(command);              
    delay(20000);                           
    mySerial.println("ATH");                
    delay(1000);                            

   
    command = "ATD+" + numberCall_2 + ";";  
    mySerial.println(command);              
    delay(20000);                           
    mySerial.println("ATH");                
    delay(1000);                            

    flagSensor_0 = 2;                       
  }


  if(flagSensor_1 == 1) {
    sendSMS(textZone_1, numberSMS_1); 
    delay(10000);                     
    sendSMS(textZone_1, numberSMS_2); 
    delay(10000);                     
    flagSensor_1 = 2;                 
  }


  if(flagSensor_2 == 1) {
    sendSMS(textZone_2, numberSMS_1); 
    delay(10000);                     
    sendSMS(textZone_2, numberSMS_2); 
    delay(10000);                     
    flagSensor_2 = 2;                 
  }


  if(flagSensor_3 == 1) {
    sendSMS(textZone_3, numberSMS_1); 
    delay(10000);                     
    sendSMS(textZone_3, numberSMS_2); 
    delay(10000);                     
    flagSensor_3 = 2;                 
  }


  if(flagSensor_4 == 1) {
    sendSMS(textZone_4, numberSMS_1); 
    delay(10000);                    
    sendSMS(textZone_4, numberSMS_2); 
    delay(10000);                     
    flagSensor_4 = 2;                
  }

  if(flagSensor_0 == 2 && digitalRead(pinSensor_0) != 0) flagSensor_0 = 0;
  if(flagSensor_1 == 2 && digitalRead(pinSensor_1) != 0) flagSensor_1 = 0;
  if(flagSensor_2 == 2 && digitalRead(pinSensor_2) != 0) flagSensor_2 = 0;
  if(flagSensor_3 == 2 && digitalRead(pinSensor_3) != 0) flagSensor_3 = 0;
  if(flagSensor_4 == 2 && digitalRead(pinSensor_4) != 0) flagSensor_4 = 0;
}
