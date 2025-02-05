#include <Keyboard.h>

void setup() {
    Keyboard.begin();
    delay(2000);

    Keyboard.print("Hello, this is my first BadUSB test!");
}

void loop() {
}
