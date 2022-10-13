#include<bits/stdc++.h>
using namespace std;


int solve(int n,int i){
    if(i==n) return 1;
    if(i>n || i<1) return 0;

    return solve(n,i-1)+solve(n,n-i);
}
int uniqueBST(int n){
    if(n<=1) return n;

    int ans=0;
    for(int i=1;i<=n;i++) ans+=solve(n,i);
    return ans;
}

int main(){
    
    cout<<uniqueBST(3);
    cout<<endl;
    return 0;
}