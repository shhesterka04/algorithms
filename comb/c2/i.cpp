#include<iostream>
#include<vector>
#include<algorithm>
 
struct req {
    int id = 0;
    int l = 0;
    int r = 0;
    int result = 0;
};
 
bool cmp(const req &a, const  req &b){
    if (a.l / 500 == b.l / 500)
        return a.r < b.r;
    else
        return a.l < b.l;
}
 
bool cmp2(const req &a, const  req &b){
    return a.id < b.id;
}
 
int answer = 0;
 
std::vector<int> arr(300001, 0);
 
int a = 0, b = -1;
void mo(std::vector<int>&v, req &q){
    int l = q.l, r = q.r;
    while(b < r){
        b++;
        if (arr[v[b]] == 0) answer++;
        arr[v[b]]++;
    }
    while(b > r){
        arr[v[b]]--;
        if (arr[v[b]] == 0) answer--;
        b--;
    }
    while(a < l){
        arr[v[a]]--;
        if (arr[v[a]] == 0) answer--;
        a++;
    }
    while(a > l){
        a--;
        if (arr[v[a]] == 0) answer++;
        arr[v[a]]++;
    }
    q.result = answer;
}
 
 
int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);
    int n = 0, m = 0;
    std::cin >> n;
    std::vector<int> v(n), pos;
    for (size_t i = 0; i < v.size(); ++i) {
        std::cin >> v[i];
    }
    pos = v;
    std::sort(pos.begin(), pos.end());
    for (size_t i = 0; i < v.size(); ++i) {
        v[i] = int(lower_bound(pos.begin(), pos.end(), v[i]) - pos.begin());
    }
    std::cin >> m;
    std::vector<req> q(m);
    for (size_t i = 0; i < q.size(); ++i) {
        int l = 0, r = 0;
        std::cin >> l >> r;
        q[i].id = i;
        q[i].l = l - 1;
        q[i].r = r - 1;
    }
    std::sort(q.begin(), q.end(), cmp);
    for(size_t i = 0; i < q.size(); ++i){
        mo(v, q[i]);
    }
    std::sort(q.begin(), q.end(), cmp2);
    for(size_t i = 0; i < q.size(); ++i){
        std::cout << q[i].result << '\n';
    }
    return 0;
}