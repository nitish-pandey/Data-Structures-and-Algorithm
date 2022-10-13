#include<bits/stdc++.h>
using namespace std;

vector<int> memo;
int solve(vector<int> &nums,int k=0){
    if(k>=nums.size()-1) return 0;

    int a=nums[k];
    if(a==0) return 10e4;
    if(memo[k]!=-1) return memo[k];
    int ans=INT_MAX;

    for(int i=1;i<=a;i++){
        int t=solve(nums,k+i);
        ans=min(ans,t);
    }
    memo[k]=1+ans;
    return 1+ans;
}

int main(){
    vector<int> nums={2,3,1,1,4},nums2={2,3,0,1,4},nums3={2,1};
    memo.resize(nums3.size(),-1);
    cout<<solve(nums3);    
    cout<<endl;
    return 0;
}