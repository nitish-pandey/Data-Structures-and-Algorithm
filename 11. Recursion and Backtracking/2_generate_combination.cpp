#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> ans;

void solve(vector<int> &temp,int n,int k,int st){
    if(k==0){
        ans.push_back(temp);
        return ;
    }
    for(int i=st+1;i<=n;i++){
        temp.push_back(i);
        solve(temp,n,k-1,i);
        temp.pop_back();
    }

}

vector<vector<int>> generateCombination(int n,int k){
    vector<int> temp;
    solve(temp,n,k,0);
    return ans;
}

int main(){
    auto comb=generateCombination(4,2);

    for(auto a:comb){
        for(int i:a){
            cout<<i<<" ";
        }
        cout<<endl;
    }
    
    cout<<endl;
    return 0;
}