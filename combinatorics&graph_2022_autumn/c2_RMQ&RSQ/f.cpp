#include <iostream>
#include <vector>
#include <algorithm>
struct Query{
    int l=0, r=0, ans=0, id = -1;
};
struct Mo{
    std::vector<int> vi;
    Mo(const std::vector<int>& v):vi(v){};
    int ans = 0;
    int a=0,b=-1;
    void get(Query& q){
        int l = q.l, r = q.r;
        while(a<l){
            if(vi[a]==0)
                ans--;
            a++;
        }
        while(a>l){
            a--;
            if(vi[a]==0)
                ans++;
        }
        while(b<r){
            b++;
            if(vi[b]==0)
                ans++;
        }
        while(b>r){
            if(vi[b]==0)
                ans--;
            b--;
        }
        q.ans=ans;
    };
};
 
 
int main(){
    int n = 0;
    std::cin >> n;
    std::vector<int> vi(n);
    for(size_t i =0; i < n; ++i)
        std::cin >> vi[i];
    int k = 0;
    std::cin >> k;
    std::vector<Query> qu(k);
    for(size_t i = 0; i < k; ++i){
        std::cin >> qu[i].l >> qu[i].r;
        qu[i].l--;
        qu[i].r--;
        qu[i].id = i;
    }
    Mo mo(vi);
    const int buben = 500;
    std::sort(qu.begin(),qu.end(),
              [](const Query& a, const Query& b) {
        if(a.l/buben == b.l/buben)
            return a.r < b.r;
        else
            return a.l < b.l;
            });
 
    for(size_t i = 0; i < k; ++i){
        mo.get(qu[i]);
    }
 
    std::sort(qu.begin(),qu.end(),
              [](const Query& a, const Query& b) {
            return a.id < b.id;
              });
 
    for(size_t i = 0; i < k; ++i){
        std::cout << qu[i].ans << " ";
    }
    return 0;
}