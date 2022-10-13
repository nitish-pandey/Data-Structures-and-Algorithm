#include<bits/stdc++.h>
using namespace std;

int solve(vector<int> nums){
    
    int ans=*max_element(nums.begin(),nums.end());

    int currMin=1,currMax=1;

    for(int a: nums){
        if(a==0){
            currMax=1;
            currMin=1;
            continue;
        }
        if(a<0) swap(currMax,currMin);

        currMax=max(currMax*a,a);
        currMin=min(currMin*a,a);

        ans=max(currMax,ans);
    }
    
    return ans;
    
}

int main(){
    vector<int> nums={-2,0,-1};
    cout<<solve(nums);
    
    cout<<endl;
    return 0;
}