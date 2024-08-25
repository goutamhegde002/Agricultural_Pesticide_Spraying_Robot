#include <Servo.h>
#include <SoftwareSerial.h>

#define bluetoothTx 1 // TX pin of Bluetooth should be connected to pin 1 of Arduino
#define bluetoothRx 0 // RX pin of Bluetooth should be connected to pin 0 of Arduino

Servo servo;

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

void setup() {
  // Setup Bluetooth serial connection
  bluetooth.begin(9600);

  // Attach servo to pin 9
  servo.attach(9);
}

void loop() {
  if (bluetooth.available() > 0) {
    char command = bluetooth.read();
    // Control servo motor based on received commands
    switch(command) {
      case 'F':
        servo.write(0); // Forward direction
        delay(1000); // Spray for 1 second, adjust as needed
        break;
      case 'B':
        servo.write(180); // Backward direction
        delay(1000); // Spray for 1 second, adjust as needed
        break;
      case 'L':
        servo.write(90); // Left direction
        delay(1000); // Spray for 1 second, adjust as needed
        break;
      case 'R':
        servo.write(270); // Right direction
        delay(1000); // Spray for 1 second, adjust as needed
        break;
      case 'S':
        servo.write(45); // Diagonal left
        delay(1000); // Spray for 1 second, adjust as needed
        break;
      case 'T':
        servo.write(135); // Diagonal right
        delay(1000); // Spray for 1 second, adjust as needed
        break;
    }
    // After spraying, return to the neutral position
    servo.write(90);
  }
}
