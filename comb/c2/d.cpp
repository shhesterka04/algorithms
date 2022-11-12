#include <iostream>
#include <vector>

int main() {
    int n = 0, m = 0;
    std::cin >> n >> m;
    int ans = 1;
    int x = 1, y = 1;
    int psum = 0;
    std::vector<std::vector<int>> mat (n, std::vector<int> (m));
    std::vector<std::vector<int>> pre (n+1, std::vector<int> (m+1));
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < m; ++j){
            std::cin >> mat[i][j];
        }
    }
    for (int i = 1; i < n+1; ++i){
        for (int j = 1; j < m+1; ++j){
            pre[i][j]=pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+mat[i-1][j-1];
        }
    }
    for (int i = 1; i < n+1; ++i){
        for (int j = 1; j < m+1; ++j){
            for (int l = ans + 1; (j+l-1<=m) && (i+l-1 <= n); ++l){
                psum = pre[i+l-1][j+l-1]-pre[i-1][j+l-1]-pre[i+l-1][j-1]+pre[i-1][j-1];
                if (psum == l*l){
                    ans = l;
                    x = i;
                    y = j;
                }
            }
        }
    }
    std::cout << ans << "\n" << x << " " << y;
}