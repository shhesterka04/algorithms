#include <iostream>
#include <vector>

int main(){
    int n = 0;
    int r = 0;
    int l = 0;
    int msum = 0;
    int mpos = -1;
    int now = 0;
    int sum = 0;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i){
        std::cin >> a[i];
    }
    int b = a[0];
    for (int i = 0; i < n; ++i){
        sum += a[i];
        now = sum - msum;
        if (now > b){
            b = now;
            l = mpos + 1;
            r = i;
        }
        if (sum < msum){
            msum = sum;
            mpos = i;
        }
    }
    std::cout << l + 1 << " " << r + 1 << " " << b;
}