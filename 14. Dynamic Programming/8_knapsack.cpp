#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> dp(100001,vector<int> (1001,-1));

int knapSack(vector<int> &values,vector<int> &weights,int w,int ind=0){

    if(ind==values.size() || w==0) return 0;
    if (dp[ind][w]!=-1) return dp[ind][w];
    
    int a=weights[ind];

    int ans= max(knapSack(values,weights,w,ind+1),values[ind]+knapSack(values,weights,w-a,ind+1));
    dp[ind][w]=ans;

    return ans;

}

int main(){
    
    vector<int> values={4,5,3,7},weights={2,3,1,4};
    int w=5;

    cout<<knapSack(values,weights,w);
    
    cout<<endl;
    return 0;
}