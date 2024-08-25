# Agricultural_Pesticide_Spraying_Robot
A simple IoT based remote control pesticide spraying robot.

This project involves the development of an Agriculture Pesticide Spraying Robot controlled via Bluetooth using Arduino Uno. The project is divided into two main components: controlling the robot's movement and controlling the pesticide sprayer using a servo motor. Additionally, a Python-based Bluetooth app is developed to send control commands from a smartphone or computer.

## Table of Contents

- [Introduction](#introduction)
- [Components Used](#components-used)
- [Circuit Diagram](#circuit-diagram)
- [Arduino Code](#arduino-code)
  - [Motor Control](#motor-control)
  - [Servo Motor Control](#servo-motor-control)
- [Python Bluetooth App](#python-bluetooth-app)
- [How to Use](#how-to-use)
- [Installation](#installation)
  - [Arduino IDE](#arduino-ide)
  - [Python Environment](#python-environment)
- [License](#license)
- [Contributing](#contributing)

## Introduction

The Agriculture Pesticide Spraying Robot is designed to assist farmers by automating the pesticide spraying process. The robot can be controlled via Bluetooth, allowing it to move in different directions and spray pesticides in specific directions. This project utilizes Arduino Uno boards, a Bluetooth module, motor drivers, and a servo motor.

## Components Used

- Arduino Uno (2 units)
- L298N Motor Driver
- DC Motors (2 units)
- Bluetooth Module (e.g., HC-05 or HC-06)
- Servo Motor (for spraying)
- Power Supply (Battery)
- Connecting Wires
- Robot Chassis
- Smartphone or Computer (with Bluetooth capability)

## Circuit Diagram

[Include an image or description of the circuit diagram here]

## Arduino Code

The project includes two separate Arduino codes: one for controlling the robot's movement and the other for controlling the pesticide sprayer using a servo motor.

### Motor Control

This code is responsible for controlling the movement of the robot. The robot can move forward, backward, turn left, turn right, and stop based on commands received via Bluetooth.

```cpp
#include <SoftwareSerial.h>

// Bluetooth module pins
#define bluetoothTx 1 // TX pin of Bluetooth should be connected to pin 1 of Arduino
#define bluetoothRx 0 // RX pin of Bluetooth should be connected to pin 0 of Arduino

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

// Motor Driver pins
#define motorA1 2
#define motorA2 3
#define motorB1 4
#define motorB2 5

void setup() {
  // Setup motor pins as outputs
  pinMode(motorA1, OUTPUT);
  pinMode(motorA2, OUTPUT);
  pinMode(motorB1, OUTPUT);
  pinMode(motorB2, OUTPUT);
  
  // Setup Bluetooth serial connection
  bluetooth.begin(9600);
}

void loop() {
  if (bluetooth.available() > 0) {
    char command = bluetooth.read();
    // Control robot movement based on received commands
    switch(command) {
      case 'F':
        moveForward();
        break;
      case 'B':
        moveBackward();
        break;
      case 'L':
        turnLeft();
        break;
      case 'R':
        turnRight();
        break;
      case 'S':
        stopRobot();
        break;
    }
  }
}

void moveForward() {
  digitalWrite(motorA1, HIGH);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, HIGH);
  digitalWrite(motorB2, LOW);
}

void moveBackward() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, HIGH);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, HIGH);
}

void turnLeft() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, HIGH);
  digitalWrite(motorB1, HIGH);
  digitalWrite(motorB2, LOW);
}

void turnRight() {
  digitalWrite(motorA1, HIGH);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, HIGH);
}

void stopRobot() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, LOW);
}

```

Servo Motor Control
This code is responsible for controlling the servo motor that sprays pesticides. The servo motor adjusts its angle based on commands received via Bluetooth.

```cpp
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

```

Python Bluetooth App
A Python-based Bluetooth app was developed to send commands to the robot from a smartphone or computer. The app uses the Kivy framework for the GUI and pybluez for Bluetooth communication.

```
Bluetooth App Code
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import bluetooth

class BluetoothApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Create label
        label = Label(text="Pesticide Spraying Robot Control")
        layout.add_widget(label)
        
        # Create buttons for robot control
        buttons = {
            "Forward": "F",
            "Backward": "B",
            "Left": "L",
            "Right": "R",
            "Stop": "S",
            "Spray Left": "S",
            "Spray Right": "T"
        }

        for button_text, command in buttons.items():
            button = Button(text=button_text, size_hint=(1, 0.2))
            button.bind(on_press=lambda btn, cmd=command: self.send_bluetooth_command(cmd))
            layout.add_widget(button)

        return layout

    def send_bluetooth_command(self, command):
        # Bluetooth address and port
        bd_addr = "XX:XX:XX:XX:XX:XX"  # Replace with your Bluetooth module's MAC address
        port = 1

        try:
            # Connect to Bluetooth device
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((bd_addr, port))

            # Send command
            sock.send(command)

            # Close connection
            sock.close()

        except bluetooth.btcommon.BluetoothError as err:
            print(f"Bluetooth error: {err}")

if __name__ == "__main__":
    BluetoothApp().run()
```

## How to Use

1. Upload the respective Arduino code to the two Arduino Uno boards.
2. Pair the Bluetooth module with your smartphone or computer.
3. Run the Python Bluetooth app.
4. Use the buttons in the app to control the robot's movement and the servo motor for pesticide spraying.

## Installation

### Arduino IDE

1. Download and install the [Arduino IDE](https://www.arduino.cc/en/software).
2. Open the provided `.ino` files and upload them to the Arduino Uno boards.

### Python Environment

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the required Python libraries:
   ```bash
   pip install kivy pybluez
## How to Use

1. Upload the respective Arduino code to the two Arduino Uno boards.
2. Pair the Bluetooth module with your smartphone or computer.
3. Run the Python Bluetooth app.
4. Use the buttons in the app to control the robot's movement and the servo motor for pesticide spraying.

## Installation

### Arduino IDE

1. Download and install the [Arduino IDE](https://www.arduino.cc/en/software).
2. Open the provided `.ino` files and upload them to the Arduino Uno boards.

### Python Environment

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the required Python libraries:
   ```bash
   pip install kivy pybluez
   ```


