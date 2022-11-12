#include <iostream>
#include <algorithm>
#include <vector>
 
struct Tree {
 
    std::vector<std::pair<int,int>> t;
    int m = 1;
 
    Tree(int n){
        while(m < n)m *= 2;
        t.resize(2*m-1);
    }
    
    void build(int i,int val,int v,int qleft,int qright){
        
        if(qright - qleft  == 1){
            t[v] = std::make_pair(val,1);
            return;
        }
        
        int mid = (qleft+qright)/2;
        
        if(i < mid)build(i,val,v*2+1,qleft,mid);
        else build(i,val,v*2+2,mid,qright);
        
        if(t[v*2+1].first > t[v*2+2].first){
            t[v] = t[v*2+1];  
        }
        if(t[v*2+1].first < t[v*2+2].first){
            t[v] = t[v*2+2];
        }
        if(t[v*2+1].first == t[v*2+2].first){
            t[v].first = t[v*2+1].first;
            t[v].second = t[v*2+1].second + t[v*2+2].second;
        }
        
    }
    
    void build(int i,int val){
        build(i,val,0,0,m);
    }
    
    
    std::pair<int,int> max_count(int left,int right,int v,int qleft,int qright){
        
        if(left >= qright || qleft >= right){
            return std::make_pair(-1,0);
        }
        if(qleft >= left && qright <= right){
            return t[v];
        }
        
        int mid = (qleft+qright)/2;
        
        std::pair<int,int> first = max_count(left,right,v*2+1,qleft,mid);
        std::pair<int,int> second = max_count(left,right,v*2+2,mid,qright);
        
        if(first.first > second.first){
            return first;
        }
        else if(first.first < second.first) {
            return second;
        }
        else {
            return std::make_pair(first.first,first.second + second.second);
        }
        
    }
    
    std::pair<int,int> max_count(int left,int right){
        return max_count(left,right,0,0,m);
    }
    
    
    
};
 
int main() 
{
    int n = 0;
    int q = 0;
    int x = 0;
    std::cin >> n;
    Tree t(n);
    for(int i = 0;i<n;++i){
        std::cin >> x;
        t.build(i,x);
    }
    std::cin >> q;
    for(int i = 0;i<q;++i){
        int left = 0;
        int right = 0;
        std::cin >> left >> right; 
        std::pair<int,int> ans = t.max_count(left-1,right);
        std::cout << ans.first << ' ' << ans.second << "\n";
    }
    return 0;
}