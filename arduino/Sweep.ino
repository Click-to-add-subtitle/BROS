/*
 * Oh yeah oh wow oh yeah oh wow
 * oh yeah yeah baby oh yeah oh wow
 * oooohhh yeah baby 
 * oh yeah oh wowo oh yeah
 * oh yeah baby
 * swaaaaaagggg
 */

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards


int pos = 90;

    int goal;

unsigned long nowTime;
unsigned long earlierTime;

void setup() {
    Serial.begin(9600);
    myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {

    nowTime = millis();

    if (earlierTime != nowTime) {
      myservo.write(pos); 
      earlierTime = nowTime ;
      int error = goal - pos;
        int sign = abs(error)/error;

        if (error == 0) {return;}

        if (abs(error) > 1.0)
          pos += 1.0*sign;
        else
          pos = goal;
    }
      
     
    //myservo.write(pos);
    if (Serial.available()>0){

        goal = Serial.read();


        myservo.write(pos);
    }
//
 //     Serial.println(pos);
    
     
     
}
