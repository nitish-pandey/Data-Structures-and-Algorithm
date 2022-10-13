#include<bits/stdc++.h>
using namespace std;

int solve(vector<int> &nums,int k,int ind=0,int sum=0){
    if(ind>=nums.size()) return 0;
    
    int ans=INT_MIN;
    for(int i=1;i<=k;i++){
        int t=solve(nums,k,ind+1);
    }
}
int jumpGame(vector<int> &nums,int k){

}
int main(){
    
    vector<int> nums={};
    int k=2;

    cout<<jumpGame(nums,k);
    cout<<endl;
    return 0;
}