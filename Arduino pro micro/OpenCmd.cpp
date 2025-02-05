#include <Keyboard.h>

void setup() {
    Keyboard.begin();
    delay(2000);
    // Open run
    Keyboard.press(KEY_LEFT_GUI);
    Keyboard.press('r');
    delay(100);
    Keyboard.releaseAll();
    delay(1000);
    // open cmd
    Keyboard.print("cmd");
    delay(20);
    Keyboard.press(KEY_RETURN);
    Keyboard.releaseAll();
    // type and enter ipconfig fo tests
    delay(2000);
    Keyboard.print("ipconfig");
    delay(100);
    Keyboard.press(KEY_RETURN);
    Keyboard.releaseAll();
}

void loop() {
}
