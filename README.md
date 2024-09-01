# Hand Gesture-Controlled LED Project

This repository contains the code and documentation for a hand gesture-controlled LED system. The project utilizes computer vision techniques to detect hand gestures and control the illumination of LEDs connected to an Arduino board.

## Project Overview

The Hand Gesture-Controlled LED project aims to create an interactive system where users can control the state of LEDs using hand gestures captured by a webcam. The system employs computer vision algorithms for hand detection and gesture recognition, coupled with Arduino-based LED control. Users can perform predefined gestures, such as thumbs-up or peace sign, to toggle the LEDs on or off in real-time.

## Hardware Requirements

* Arduino Uno board
* LEDs (quantity as desired)
* USB webcam
* Breadboard
* Jumper wires

## Software Requirements

* Python 3
* Arduino IDE
* OpenCV library
* cvzone library (specifically the HandTrackingModule)
* pySerial library

## Installation and Setup

1. Connect the LEDs to the digital pins of the Arduino board using jumper wires.
2. Connect the Arduino board to your computer via USB.
3. Install the required Python libraries:
content_copy
Use code with caution.

pip install opencv-python cvzone pyserial

4. Upload the Arduino code (`ARDUINO_CODE.ino`) to the Arduino board using the Arduino IDE.
5. Update the `com_port` variable in the Python code (`PYTHON_CODE.py`) to match the serial port of your Arduino board.

## Usage

1. Run the Python script:
content_copy
Use code with caution.

python main.py

2. The system will initialize the webcam and hand detection module.
3. Perform hand gestures in front of the webcam.
4. The LEDs will illuminate or extinguish based on the recognized gestures.

## Project Report

A detailed project report [(`project_report.pdf`)](https://github.com/harinarayanan-kp/Hand-Gesture-Controller-Arduino/blob/main/report1.pdf) is included in the repository, providing comprehensive information on the project's objectives, methodology, results, and analysis.

## Future Enhancements

* Implement additional hand gestures for more complex LED control.
* Develop a graphical user interface (GUI) for improved user interaction.
* Integrate with IoT platforms for remote control and automation features.
* Explore the use of depth-sensing cameras for enhanced gesture recognition accuracy.

## Acknowledgments

This project was inspired by the growing field of human-computer interaction and the potential of hand gesture recognition technology.
content_copy
Use code with caution.
