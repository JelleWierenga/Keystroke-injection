#include <Keyboard.h>
void setup() {
    Keyboard.begin();
    randomSeed(analogRead(A0));
    String chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    String result = "";
    for (int i = 0; i < 10; i++) {
        int index = random(0, chars.length());
        result += chars[index];
    }
    delay(2000);
    for (int i = 0; i < result.length(); i++) {
        Keyboard.print(result[i]);
        delay(20);
    }

}
void loop() {
}
