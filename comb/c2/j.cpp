#include<iostream>
#include<vector>

int main() {
    int n = 0, m = 0, k = 0;
    int q = 0;
    int x1 = 0, y1 = 0, z1 = 0, x2 = 0, y2 = 0, z2 = 0;
    std::cin >> n >> m >> k;
    std::vector<std::vector<std::vector<int>>> mat(n, std::vector<std::vector<int>>(m, std::vector<int>(k)));
    std::vector<std::vector<std::vector<int>>> pre(n+1, std::vector<std::vector<int>>(m+1, std::vector<int>(k+1)));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j){
            for (int z = 0; z < k; ++z) {
                std::cin >> mat[i][j][z];
            }
        }
    }
    for (int i = 1; i < n+1; ++i) {
        for (int j = 1; j < m+1; ++j){
            for (int z = 1; z < k+1; ++z) {
                pre[i][j][z] = mat[i-1][j-1][z-1] + pre[i-1][j][z] + pre[i][j-1][z] + pre[i][j][z-1] + pre[i-1][j-1][z-1]
                 - pre[i-1][j-1][z] - pre[i][j-1][z-1] - pre[i-1][j][z-1];
            }
        }
    }
    std::cin >> q;
    for (int i = 0; i < q; ++i){
        std::cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
        int ans = pre[x2][y2][z2] - pre[x1-1][y1][z1] - pre[x1][y1-1][z1] - pre[x1][y1][z1-1] + pre[x1-1][y1-1][z1] + pre[x1][y1-1][z1-1] + pre[x1-1][y1][z1-1] - pre[x1-1][y1-1][z1-1];
        std::cout << ans << "\n";
    }
}
