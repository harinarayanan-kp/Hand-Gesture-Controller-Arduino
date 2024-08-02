int ledPins[] = {8, 9, 10, 11, 12};
const int num_leds = sizeof(ledPins) / sizeof(ledPins[0]);

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < num_leds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
}

void loop() {
  if (Serial.available() > 0) {
    // Read the string from serial until newline character is encountered
    String command = Serial.readStringUntil('\n');

    // Control LEDs based on finger counts
    for (int i = 0; i < num_leds; i++) {
      if (command[i] == '1') {
        // Turn on LED if corresponding finger is up
        digitalWrite(ledPins[num_leds - 1 - i], HIGH);
      } else {
        // Turn off LED if corresponding finger is down
        digitalWrite(ledPins[num_leds - 1 - i], LOW);
      }
    }
  }
}
