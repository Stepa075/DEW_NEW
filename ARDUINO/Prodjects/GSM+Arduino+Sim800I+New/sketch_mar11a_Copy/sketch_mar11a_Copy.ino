//Начало скетча версии 2.0
#include <OneWire.h>         //библиотека для считывания кода ключей
#include "EEPROM.h"          //библиотека для для записи в энергонезависимую память
#include <SoftwareSerial.h>  //библиотека для создания второго программного UART для связи с GSM модулем

const int key_led = 5;       //Пин 5 для подключения светодиода для индикации о постановке на охрану
const int key_pin = 6;       //Пин 6 для считывания ключа таблетки RW1990, TM1990A
OneWire key (key_pin);
const int rx_prog = 2;       //программный rx для подключения GSM модуля SIM800L
const int tx_prog = 3;       //программный tx для подключения GSM модуля SIM800L
SoftwareSerial SIM800(rx_prog, tx_prog); //программные RX, TX для связи с модулем SIM800L
const int led_2   = 9;       //светодиод для индикации сигнализации
const int a1      = 15;      //линия А1 для подключения датчика
const int a2      = 16;      //линия А2 для подключения датчика
const int a3      = 17;      //линия А3 для подключения датчика
const int a4      = 18;      //линия А4 для подключения датчика
const int a5      = 19;      //линия А5 для подключения датчика
const int speaker = 8;       //контакт для подключения сирены
const int set_220 = 7;       //контакт для определения наличия питания в сети
const int relay   = 13;      //контакт для подключения твердотельного реле или релейного модуля

String phon = "+380975781595";
  //1 номер на который будет выполняться звонок если сработает сигнализация
  
String phones = "+380975781595";
  //1 или несколько номеров через запятую, с которых будет разрешено управления по СМС
  
String balance = "*111#";
  //1 номер для проверки баланса Sim карты GSM сигнализации

String SMS_phone = "+380975781595";
  //1 номер на который будут приходить SMS отчеты
  
String sms_otchet = "Ktr3";   //запрос SMS о состоянии сигнализации, датчиков сигнализации и реле
String sig_on     = "Sig1";   //поставить сигнализацию на охрану
String sig_off    = "Sig0";   //снять сигнализацию с охраны
String sms_on     = "Sms1";   //включить отправку SMS при срабатывании сигнализации
String sms_off    = "Sms0";   //выключить отправку SMS при срабатывании сигнализации
String ring_on    = "Ring1";  //включить исходящий вызов при срабатывании сигнализации
String ring_off   = "Ring0";  //выключить исходящий вызов при срабатывании сигнализации
String ballanse   = "Bal";    //проверка баланса SIM карты
String relay_on   = "Rel1";   //команда для включения реле
String relay_off  = "Rel0";   //команда для выключения реле

byte arr[8];
String read_key = "";

String open_key = "1f34bf6000f7";
  //1 разрешенный код ключ (для добавления нескольких ключей коды записываются через запятую)
   
int sig_pause    = 10;   //10 секунд пауза после считывания ключа при постановке на охрану
int block_pause  = 10;   //10 секунд пауза для повторного считывания ключа, после того как был считаный неверный ключ
long spiker_time = 30;   //20 секунд время работы сирены, после отключения датчиков
long ring_time   = 20;   //20 секунд пауза между звонками при срабатывании сигнализации
int batery_limit = 30;   //значение заряда батареи в процентах, при котором отправится СМС о разряженной батареи (оптимально от 30% до 60%)
int ring_x       = 3;    //пауза 3 минуты между сериями звонков, при постоянно сработанном концевике (от 1 до 32000 минут)

int val, send_mesag_state_Batery = 0, send_mesag_Balanse = 0, led_2_OFF, led_2_ON, readflag = 0;
int sig_st = 0, stat_a1 = 0, stat_a2  = 0, stat_a3 = 0, stat_a4 = 0, stat_a5 = 0;
int ring = 0, ring_st = 1, ring_fl = 0, ring_fl2 = 0, send_mesag = 0, sms_st = 1, blinker = 1, rel_st = 0;
String signalingS = "", signaling = "", str_a1 = "", str_a2 = "", str_a3 = "", str_a4 = "", str_a5 = "";
String signaling_OK = "Signaling OK";
int k=0, v=0, t=0, msgphone = 0, state_Batery = 100, flag_Button_KeY = 1, flag_Button_KeY_P = 0;

  // Переменные для работы с EEPROM
int flag_EEPROM, start_FLAG = 2, address_FLAG = 0,  address_SMS = 2, address_SIG = 4, address_RING = 6, address_REL = 8;

// Переменные для хранения точек отсчета, для таймеров
unsigned long timing10, timing11, timing12, timing13, timing14, timing15, timing16, timing17; 

String _response = "";                                   // Переменная для хранения ответа модуля
long lastUpdate = millis();                              // Время последнего обновления
long updatePeriod = 60000;                               // Проверять каждую минуту

String waitResponse() {                                  // Функция ожидания ответа и возврата полученного результата
String _resp = "";                                       // Переменная для хранения результата
long _timeout = millis() + 10000;                        // Переменная для отслеживания тайм аута (10 секунд)
while (!SIM800.available() && millis() < _timeout)  {};  // Ждем ответа 10 секунд, если пришел ответ или наступил тайм аут, то...
if (SIM800.available()) {                                // Если есть, что считывать...
_resp = SIM800.readString();                             // считываем и запоминаем
}else {                                                  // Если пришел тайм аут, то...
Serial.println("Timeout...");                            // оповещаем об этом и...
}return _resp;                                           // возвращаем результат. Пусто, если проблема
}


String sendATCommand(String cmd, bool waiting) {
String _resp = "";                                       // Переменная для хранения результата
Serial.println(cmd);                                     // Дублируем команду в монитор порта
SIM800.println(cmd);                                     // Отправляем команду модулю
if (waiting) {                                           // Если необходимо дождаться ответа...
_resp = waitResponse();                                  // ... ждем, когда будет передан ответ
// Если Echo Mode выключен (ATE0), то эти 3 строки можно за комментировать
if (_resp.startsWith(cmd)) {                             // Убираем из ответа дублирующуюся команду
_resp = _resp.substring(_resp.indexOf("\r", cmd.length()) + 2);}
Serial.println(_resp);                                   // Дублируем ответ в монитор порта
}return _resp;                                           // Возвращаем результат. Пусто, если проблема
}

void parseSMS(String msg) {                               // Парсим SMS
String msgheader  = "";
String msgbody    = "";
String msgphone   = "";
msg = msg.substring(msg.indexOf("+CMGR: "));              // удаляем АТ команду
msgheader = msg.substring(0, msg.indexOf("\r"));          // выдергиваем телефон от начала до перехода на следующую строку
msgbody = msg.substring(msgheader.length() + 2);          // сохраняем в строку msgbody
msgbody = msgbody.substring(0, msgbody.lastIndexOf("OK"));// выдергиваем текст SMS от номера до ОК
msgbody.trim();                                           // удаляем пробелы в начале и в конце

int firstIndex = msgheader.indexOf("\",\"") + 3;
int secondIndex = msgheader.indexOf("\",\"", firstIndex);
msgphone = msgheader.substring(firstIndex, secondIndex);

Serial.println("Phone: " + msgphone);                     // Выводим номер телефона
Serial.println("Message: " + msgbody);                    // Выводим текст SMS

if (msgphone.length() > 6 && phones.indexOf(msgphone) > -1) { // Если телефон в белом списке, то...

//<<<<<<<<<<<<<<<<<<< SMS команды >>>>>>>>>>>>>>>>>>>>>>
if(msgbody == sms_otchet){ Serial.println(sms_otchet); delay(300); k=3;}
  //запрос SMS о состоянии сигнализации, и датчиков сигнализации
  
if(msgbody == sms_off){ Serial.println(sms_off); delay(300);   sms_st = 0;
  EEPROM.put(address_SMS, sms_st);}      //выключить отправку SMS при срабатывании сигнализации
  
if(msgbody == sms_on){ Serial.println(sms_on); delay(300);   sms_st = 1;
  EEPROM.put(address_SMS, sms_st);}      //включить отправку SMS при срабатывании сигнализации
  
if(msgbody == ring_off){Serial.println(ring_off); delay(300);   ring_st = 0;
  EEPROM.put(address_RING, ring_st);}    //выключить исходящий вызов при срабатывании сигнализации
  
if(msgbody == ring_on){Serial.println(ring_on); delay(300);ring_st = 1;ring = 0;
  EEPROM.put(address_RING, ring_st);}    //включить исходящий вызов при срабатывании сигнализации
  
if(msgbody == sig_off){ Serial.println(sig_off); delay(300);sig_st = 0;
  EEPROM.put(address_SIG, sig_st);}      //выключить сигнализацию
  
if(msgbody == sig_on){ Serial.println(sig_on); delay(300); sig_st = 1;
  EEPROM.put(address_SIG, sig_st);}       //включить сигнализацию

if(msgbody == relay_off){ Serial.println(relay_off); delay(300);rel_st = 0;
  EEPROM.put(address_REL, rel_st);} digitalWrite(relay, rel_st);     //выключить реле
  
if(msgbody == relay_on){ Serial.println(relay_on); delay(300); rel_st = 1;
  EEPROM.put(address_REL, rel_st);} digitalWrite(relay, rel_st);      //включить реле

if(msgbody == ballanse){  Serial.println(ballanse);   //проверка баланса SIM карты
  SIM800.println("AT+CUSD=1,\"" + balance + "\"");}
}else {
//Serial.println("Unknown phonenumber");
}}

void numbr_sms(){ 
  SIM800.println("AT+CMGS=\"" + SMS_phone + "\"");
  delay(3000);
}

void text_sms(){
SIM800.println("Set = " + String(v) + " volt");delay(300);
if (state_Batery == 10){state_Batery = 100;}
SIM800.println("Battery = " + String(state_Batery) + "%");delay(300);
SIM800.println(signaling);delay(300);
SIM800.println(signalingS);delay(300);
SIM800.println(str_a1);delay(300);
SIM800.println(str_a2);delay(300);
SIM800.println(str_a3);delay(300);
SIM800.println(str_a4);delay(300);
SIM800.println(str_a5);delay(300);
SIM800.println("Ring = " + String(ring_st)); delay(300);
SIM800.println("SMS = " + String(sms_st)); delay(300);
SIM800.println("REL = " + String(rel_st));
}

void go_sms(){
    delay(300);
    SIM800.print((char)26);    //команда для отправки SMS
    delay(300);
}

void read_Button_KeY(){        //функция для считывания ключа
  if(flag_Button_KeY == 1){
    if (!key.search (arr)) {
    key.reset_search(); delay(50);
    return; }
  for (byte x = 0; x < 8; x++) { read_key = read_key + String(arr[x], HEX);}
  byte crc; crc = key.crc8(arr, 7);
 Serial.println(read_key);

if (read_key.length() > 10 && open_key.indexOf(read_key) > -1) {
  timing15 = millis(); flag_Button_KeY_P = 1; flag_Button_KeY = 0; Serial.println("Key OK!");
  digitalWrite(key_led, HIGH);
  }else{
    timing17 = millis(); flag_Button_KeY = 0; Serial.println("Key ERROR!");
}
 read_key = "";
}}

void setup() {  //>>>>>>>>>>>>>>>>> SETUP <<<<<<<<<<<<<<<<<<<

    //набор функций для записи настроек в энергонезависимую память при первом запуске
  EEPROM.get(address_FLAG, flag_EEPROM); 
  if(flag_EEPROM < start_FLAG){
    EEPROM.put(address_FLAG, start_FLAG);
    EEPROM.put(address_SMS, sms_st);
    EEPROM.put(address_SIG, sig_st);
    EEPROM.put(address_RING, ring_st);
    EEPROM.put(address_REL, rel_st);
  } 
  EEPROM.get(address_SMS, sms_st); 
  EEPROM.get(address_SIG, sig_st); 
  EEPROM.get(address_RING, ring_st);
  EEPROM.get(address_REL, rel_st);
  
Serial.begin(9600);                           // Скорость обмена данными с компьютером
SIM800.begin(115200);                           // Скорость обмена данными с модемом
analogReference(INTERNAL);

sendATCommand("AT", true);                    // Отправили AT для настройки скорости обмена данными
sendATCommand("AT+CMGDA=\"DEL ALL\"", true);  // Удаляем все SMS, чтобы не забивать память
sendATCommand("AT+CMGF=1;&W", true);          // Включаем текстовый режима SMS (Text mode) и сразу сохраняем значение (AT&W)!
sendATCommand("AT+CSCB=1;&W", true);        // Включаем приём специальных сообщений и сразу сохраняем значение (AT&W)!
lastUpdate = millis();                        // Обнуляем таймер

pinMode(set_220, INPUT);
pinMode(a1, INPUT_PULLUP);
pinMode(a2, INPUT_PULLUP);
pinMode(a3, INPUT_PULLUP);
pinMode(a4, INPUT_PULLUP);
pinMode(a5, INPUT_PULLUP);
pinMode(speaker, OUTPUT);
pinMode(led_2, OUTPUT);
pinMode(relay, OUTPUT); digitalWrite(relay, rel_st);
pinMode(key_led, OUTPUT); digitalWrite(key_led, LOW);
}
bool hasmsg = false;                          // Флаг наличия сообщений к удалению

void loop() { //>>>>>>>>>>>>>>>>>> LOOP <<<<<<<<<<<<<<<<<<

/* Следующие 11 строк после этого комментария служат для отладки и управления по UART.
То есть если в UART отправить 3 то должен прийти SMS отчет, а если отправить 4,
то выполнится проверка баланса сим карты, и так далее.
 */


if (Serial.available() > 0) { 
char val = Serial.read();
if(val == '3'){k = 3;}            //запрос SMS отчета
if(val == '4'){  delay(1000); SIM800.println("AT+CUSD=1,\"" + balance + "\"");}//проверка баланса SIM карты
if(val == '5'){sig_st = 1;}       //включить сигнализацию
if(val == '6'){sig_st = 0;}       //выключить сигнализацию
if(val == '7'){ring_st = 1; ring = 0;}   //включить исходящий вызов при срабатывании сигнализации
if(val == '8'){ring_st = 0;}      //выключить исходящий вызов при срабатывании сигнализации
if(val == '9'){sms_st = 1;}       //включить отправку SMS при срабатывании сигнализации
if(val == '0'){sms_st = 0;}       //выключить отправку SMS при срабатывании сигнализации
}

if (lastUpdate + updatePeriod < millis() ) {                // Пора проверить наличие новых сообщений
do {
_response = sendATCommand("AT+CMGL=\"REC UNREAD\",1", true);// Отправляем запрос чтения непрочитанных сообщений
if (_response.indexOf("+CMGL: ") > -1) {                    // Если есть хоть одно, получаем его индекс
  Serial.println ("POLUCHENO 1 SMS");
int msgIndex = _response.substring(_response.indexOf("+CMGL: ") + 7, _response.indexOf("\"REC UNREAD\"", _response.indexOf("+CMGL: ")) - 1).toInt();
char i = 0;                                                  // Объявляем счетчик попыток
do { i++;                                                    // Увеличиваем счетчик
_response = sendATCommand("AT+CMGR=" + (String)msgIndex + ",1", true);  // Пробуем получить текст SMS по индексу
_response.trim();                                            // Убираем пробелы в начале/конце
if (_response.endsWith("OK")) {                              // Если ответ заканчивается на "ОК"
  if (!hasmsg) hasmsg = true;                                // Ставим флаг наличия сообщений для удаления
  sendATCommand("AT+CMGR=" + (String)msgIndex, true);        // Делаем сообщение прочитанным
  sendATCommand("\n", true);                                 // Перестраховка - вывод новой строки
  parseSMS(_response);                                       // Отправляем текст сообщения на обработку
  break;                                                     // Выход из do{}
}else {                                                      // Если сообщение не заканчивается на OK
  Serial.println ("Error answer");                           // Какая-то ошибка
  sendATCommand("\n", true);                                 // Отправляем новую строку и повторяем попытку
}} while (i < 10);
break;}
else {
lastUpdate = millis();                              // Обнуляем таймер
if (hasmsg) {
sendATCommand("AT+CMGDA=\"DEL READ\"", true);       // Удаляем все прочитанные сообщения
hasmsg = false;
}break;}} while (1);}

if (SIM800.available())   {                         // Если модем, что-то отправил...
_response = waitResponse();                         // Получаем ответ от модема для анализа
_response.trim();                                   // Убираем лишние пробелы в начале и конце
  Serial.println(_response);                          // Если нужно выводим в монитор порта

if (_response.indexOf("+CMTI:")>-1) {               // Пришло сообщение об отправке SMS
lastUpdate = millis() -  updatePeriod;              // Теперь нет необходимости обрабатывать SMS здесь, достаточно просто
}

if (_response.indexOf("+CBC:")>-1) {                //Если пришел ответ о состоянии батареи
state_Batery = _response.substring(17, 19).toInt(); //Выдергиваем часть строки с данными о состоянии батареи, переводим в integer

/*Закомментированые строки с функциями Serial.print или Serial.println служат для более удобной отладки по UART.
Чтобы наблюдать все процессы в мониторе порта, необходимо раскомментировать все подобные строки находящиеся во всем void loop()*/
Serial.print("Batery = "); Serial.println(state_Batery);
Serial.print("Set = "); Serial.println(v);
}

//команды для проверки баланса
if (_response.indexOf("+CUSD:")>-1) {               //Если пришел ответ о состоянии баланса
Serial.println(">>Balanse!<<");
send_mesag_Balanse++;
}}

if (k == 3){delay(300);
   Serial.println("<<Send SMS (Ktr3)>>");
numbr_sms(); text_sms(); go_sms();k=0;} 

//опрос датчиков
 stat_a1 = digitalRead(a1);
if (stat_a1 == LOW && signalingS == signaling_OK) { str_a1 = "A1 OK!";} 
if (stat_a1 == HIGH) {str_a1 = "A1 OPEN!";}

 stat_a2 = digitalRead(a2);
if (stat_a2 == LOW && signalingS == signaling_OK) { str_a2 = "A2 OK!";}
if (stat_a2 == HIGH) {str_a2 = "A2 OPEN!";}

 stat_a3 = digitalRead(a3);
if (stat_a3 == LOW && signalingS == signaling_OK) { str_a3 = "A3 OK!";}
if (stat_a3 == HIGH) {str_a3 = "A3 OPEN!";}

 stat_a4 = digitalRead(a4);
if (stat_a4 == LOW && signalingS == signaling_OK) { str_a4 = "A4 OK!";}
if (stat_a4 == HIGH) {str_a4 = "A4 OPEN!";}

 stat_a5 = digitalRead(a5);
if (stat_a5 == LOW && signalingS == signaling_OK) { str_a5 = "A5 OK!";}
if (stat_a5 == HIGH) {str_a5 = "A5 OPEN!";}

//Сигнализация выключена
if(sig_st == 0){ 
  send_mesag = 0; ring = 0; ring_fl = 0;
  signaling = "Signal OFF";  digitalWrite(speaker, LOW);}
  
//Сигнализация включена 
if(sig_st == 1){   signaling = "Signal ON";
 
// если датчик сработает
if (ring == 0 && led_2_ON == 200 && ring_fl == 0) 
  { signalingS = "POPYTKA VZLOMA";  digitalWrite(speaker, HIGH); 
if (ring_st == 1){ring ++; Serial.println("<<ring ++;>>");}
if(sms_st == 1){send_mesag++; }
  timing10 = millis(); Serial.println("VZLOM");
  } else { signalingS = signaling_OK; 
   if (millis() - timing12 > spiker_time){timing12 = millis(); digitalWrite(speaker, LOW);}
   }
 }

// 3 звонка при срабатывании датчиков
if (ring > 0 && millis() - timing10 > ring_time * 1000 && ring_st == 1 && ring_fl == 0){ 
      timing10 = millis(); ring++;
      String ring1 = String(ring-1);
    Serial.println("<< Ring " + ring1 + " >>");
   SIM800.println("ATD" + phon + ";");
  }
  
if (ring > 3) {ring = 0; send_mesag = 0; ring_fl = 1;} 

//опрос датчиков
if(stat_a1 == LOW && stat_a2 == LOW && stat_a3 == LOW && stat_a4 == LOW && stat_a5 == LOW)
{blinker = 1;}else{blinker = 0;}

//блинк для индикации сигнализации
if(sig_st == 0 && blinker == 1){led_2_ON = 1000; led_2_OFF = 1000;}
if(sig_st == 1 && blinker == 1){led_2_ON = 3000; led_2_OFF = 100;}

//опрос датчиков
if(stat_a1 == HIGH || stat_a2 == HIGH || stat_a3 == HIGH || stat_a4 == HIGH || stat_a5 == HIGH)
{led_2_ON = 200; led_2_OFF = 100; 
if(sig_st == 1){digitalWrite(speaker, HIGH);}
}else {
if (millis() - timing12 > spiker_time*1000){timing12 = millis(); digitalWrite(speaker, LOW);}
}


if (millis() - timing13 > led_2_ON){
timing13 = millis();timing14 = millis(); 
digitalWrite(led_2, HIGH);
}
if (millis() - timing14 > led_2_OFF){digitalWrite(led_2, LOW);}
 
  if (send_mesag == 1 && sms_st == 1){
   Serial.println("<<<Soobshenie Otpravleno (Pri vzlome)>>>");
numbr_sms(); text_sms(); go_sms(); send_mesag++;
 }
 if (send_mesag > 2) {send_mesag = 2;}
 
 if (send_mesag_Balanse == 1){
   Serial.println("<<SMS Balanse>>");
numbr_sms();  SIM800.println(_response); go_sms();
send_mesag_Balanse = 0; delay(1000);
sendATCommand("AT+CMGDA=\"DEL ALL\"", true);// Удаляем все SMS, чтобы не забивать память
 }
 if (send_mesag_Balanse >= 2) {send_mesag_Balanse = 0;}

//Сообщение о разряженной батареи
if(state_Batery > 11 && state_Batery < batery_limit){send_mesag_state_Batery++;}
 if (send_mesag_state_Batery == 1){
   Serial.println("<<SMS Batery < 50%>>");
numbr_sms(); 
SIM800.println("Set = " + String(v) + " volt");
delay(300); 
SIM800.print("Battery = " + String(state_Batery) + "%");
go_sms();
 }
 if (send_mesag_state_Batery > 2) {send_mesag_state_Batery = 2;}

 if(state_Batery > 80){send_mesag_state_Batery = 0;}
 
int sensorVal = digitalRead(set_220);   // для получения состояния сети 220 
if (sensorVal == HIGH) { v = 220;} else {v = 0;}
 
  if (millis() - timing11 > 1000){
        timing11 = millis();
    read_Button_KeY();                       // считывание ключа и если ключ верный то изменить состояние сигнализации 

 if(t == 60){
    SIM800.println("AT+CBC");           // Получить уровень заряда батареи
    Serial.print ("Ring = " + String(ring_st));
    Serial.print ("SMS = " + String(sms_st));
    Serial.println ("STAT BAT?");
    
if (ring_fl == 1){ring_fl2++;}
if (ring_fl2 == ring_x+1){ring_fl = 0; ring_fl2 = 0;}
 }t++; if(t > 60){t = 0;}
}

  //постановка на охрану ключом таблеткой
if(sig_st == 0 && flag_Button_KeY_P == 1 && millis() - timing15 > sig_pause * 1000){  
      sig_st = 1; flag_Button_KeY_P = 0; //задержка срабатывания после считывания ключа, выставляется переменной sig_pause в начале скетча 
      flag_Button_KeY = 1;               //разрешаем считывание ключа
      EEPROM.put(address_SIG, sig_st);   //сохранить состояние в энергонезависимую память   
      digitalWrite(key_led, LOW);
}

  //снятие с охраны ключом таблеткой
if(sig_st == 1 && flag_Button_KeY_P == 1){
      sig_st = 0; flag_Button_KeY_P = 0;  timing16 = millis();
      EEPROM.put(address_SIG, sig_st);   //сохранить состояние в энергонезависимую память
      digitalWrite(key_led, LOW);
}

if(sig_st == 0 && flag_Button_KeY_P == 0 && flag_Button_KeY == 1 && millis() - timing16 > 3000){
  flag_Button_KeY = 1;                   //через 3 секунды после снятия с охраны разрешаем считывание ключа
}

  //при неверном коде ключа не разрешать считывать ключ в течении времени block_pause
if(flag_Button_KeY == 0 && millis() - timing17 > block_pause * 1000){
  flag_Button_KeY = 1;}                 //разрешить сканирование ключа после истечения времени block_pause

}
