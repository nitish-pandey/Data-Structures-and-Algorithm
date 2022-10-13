#include<bits/stdc++.h>
using namespace std;

int robHelper(vector<int> &nums,int k,unordered_map<int,int> &memo){

    if(memo.count(k)>0) return memo[k];
    if(k>=nums.size()) return 0;

    int ans=max(nums[k]+robHelper(nums,k+2,memo),robHelper(nums,k+1,memo));
    memo[k]=ans;

    return ans;
}

int rob(vector<int> &nums){
    int n=nums.size();
    if(n==0) return 0;
    if(n==1) return nums[0];
    vector<int> a={nums.begin(),nums.end()-1};
    vector<int> b={nums.begin()+1,nums.end()};
    unordered_map<int,int> memo1,memo2;
    return max(robHelper(a,0,memo1),robHelper(b,0,memo2));
}

int main(){
    
    vector<int> nums={2,3,2};
    cout<<rob(nums);
    cout<<endl;
    return 0;
}