#include<bits/stdc++.h>
using namespace std;

vector<int> dp;

int solve(vector<int> &nums,int k){

    if(k>=nums.size()) return 0;

    if(dp[k]!=-1) return dp[k];
    
    int ans=max(solve(nums,k+1),solve(nums,k+2)+nums[k]);
    dp[k]=ans;
    return ans;
}

int main(){
    
    vector<int> nums={ 1, 2, 9, 4, 5, 0, 4, 11, 6 };
    
    dp=vector<int> (nums.size(),-1);
    cout<<solve(nums,0);    
    
    cout<<endl;
    return 0;
}