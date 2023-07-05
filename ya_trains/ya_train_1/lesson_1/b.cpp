#include <iostream>

int main(){
    int a = 0;
    int b = 0;
    int c = 0;
    std::cin >> a >> b >> c;
    if ((a + b > c) && (c + a > b) && (b + c > a)) {
        std::cout << "YES";
    } else std::cout << "NO";

}