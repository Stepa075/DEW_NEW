void setup() {
  // initialize digital pin LED_BUILTIN as an output.
 
  pinMode(LED_BUILTIN, OUTPUT);
   pinMode(2, OUTPUT);
   pinMode(3, OUTPUT);
   pinMode(4, OUTPUT);
   pinMode(5, OUTPUT);
   pinMode(6, OUTPUT);
   pinMode(7, OUTPUT);
   pinMode(8, OUTPUT);
   pinMode(9, OUTPUT);
   pinMode(10, OUTPUT);
   pinMode(11, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, LOW);
  for(int  i = 0;i<5;i++){              //Мигаем через один.
   digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    digitalWrite(5, LOW);
    digitalWrite(6, HIGH);
    digitalWrite(7, LOW);
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
    digitalWrite(10, HIGH);
    digitalWrite(11, LOW);
  
  delay(500);                      
//  digitalWrite(LED_BUILTIN, LOW); 
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);
  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(10, LOW);
  digitalWrite(11, HIGH);
  delay(500);       
  }
  
   for(int counter =2; counter<12; counter ++){       // Зажигаем все.
        digitalWrite(counter, HIGH);
   }
   delay(500);
   for(int x = 0;x<5;x++){

      for(int counter =2; counter<12; counter ++){    // Тушим по очереди.
        digitalWrite(counter, LOW);
        delay(200);
      }
      for(int counter =2; counter<12; counter ++){    // Зажигаем по одной.
        digitalWrite(counter, HIGH);
       delay(200);
      }

 } 

 for(int  y = 0;y<5;y++){            //Мигаем всеми.
for(int counter =2; counter<12; counter ++){       // Зажигаем все.
        digitalWrite(counter, LOW);
   }

  delay(500);  
for(int counter =2; counter<12; counter ++){       // Зажигаем все.
        digitalWrite(counter, HIGH);
   }
  delay(500);  
 }


for(int z = 0;z<5;z++){

      for(int counter =11; counter>1; counter --){    // Тушим по очереди.
        digitalWrite(counter, LOW);
        delay(200);
      }
      for(int counter =11; counter>1; counter --){    // Зажигаем по одной.
        digitalWrite(counter, HIGH);
       delay(200);
      }
 } 

 
 }
 
