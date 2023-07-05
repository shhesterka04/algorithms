#include <iostream>

int main() {
    int a = 0, b = 0, c = 0;
    std::cin >> a >> b >> c;
    if (c < 0) {
        std::cout << "NO SOLUTION";
    }
    else if (a == 0) {
        if (b == c * c) {
            std::cout << "MANY SOLUTIONS";
        }
        else {
            std::cout << "NO SOLUTION";
        }
    }
    else {
        int x = 0;
        if ((c*c-b) % a == 0) {
            x = (c*c-b) / a;
            std::cout << x;
        }
        else {
            std::cout << "NO SOLUTION";
        }
    }
}
