#include <iostream>
#include <vector>
#include <algorithm>


class Tree{
private:
    std::vector<int> t;
    std::vector<int> a;
    std::vector<int> t_index;

    void build(int v, int left, int right){
        if (right - left == 1) {
            this->t[v] = this->a[left];
        } else {
            int m = (left + right) / 2;
            build(2 * v + 1, left, m);
            build(2 * v + 2, m, right);
            this->t[v] = std::max(this->t[2 * v + 1],this->t[2 * v + 2]);
        }
    }

    int sum(int v, int left, int right, int qleft, int qright) {
        if (qright <= left || right <= qleft) {
            return 0;
        } else if (qleft <= left && right <= qright) {
            return this->t[v];
        } else {
            int m = (left + right) / 2;
            return std::max(sum(2 * v + 1, left, m, qleft, qright), sum(2 * v + 2, m, right, qleft, qright));
        }
    }
public:
    Tree(std::vector<int> arr){
        int k = 1;
        while (k < arr.size())
        {
            k *= 2;
        }
        this->a.resize(k,0);
        for (int i = 0; i < a.size(); ++i) {
            this->a[i] = arr[i];
        }
        this->t.resize(2*k-1,0);
        this->t_index.resize(2*k-1,1);
        build(0,0,this->a.size());
    }
    int sum(int qleft, int qright){
        return sum(0, 0, this->a.size(), qleft, qright);       
    }

    
};

int main(){
    int n = 0;
    int temp = 0, count = 0;
    std::cin >> n;
    std::vector<int> q(n,0);
    for (int i = 0; i < n; i++){
        std::cin >> q[i];
    }
    int m = 0, a = 0, b = 0;
    std:: cin >> m;
    Tree ts = Tree(q);
    for (int i = 0; i < m; ++i){
        std::cin >> a >> b;
        temp = ts.sum(a-1,b);
        std::cout << temp << " " << count << "\n";
        count = 1;
    }
    return 0;
}