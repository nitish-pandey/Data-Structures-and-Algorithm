#include<bits/stdc++.h>
using namespace std;

#define ll long long int
map<pair<int,int>, ll> memo;

ll solve(int n,int k,int target){

    if(memo.count({n,target})>0) return memo[{n,target}];
    if(n==0) return (target==0);

    if(target<0 || n*k <target || n>target) return 0;

    ll ans=0;
    for(int i=1;i<=k;i++){
        ans+=solve(n-1,k,target-i);
    }

    ll a=10e9+7;
    ans=ans%a;
    memo[{n,target}]=ans;
    return ans;
}

int main(){

    cout<<solve(30,30,500)<<endl;
    
    return 0;
}