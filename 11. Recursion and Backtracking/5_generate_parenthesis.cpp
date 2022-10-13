#include<bits/stdc++.h>
using namespace std;

void solve(vector<string> &ans,string curr,int open,int close){
    if(open==0 && close==0){
        ans.push_back(curr);
        return;
    }
    if(open>close) return;
    if(close>0) solve(ans,curr+')',open,close-1);
    if(open>0) solve(ans,curr+'(',open-1,close);
   
}

vector<string> generateParenthesis(int n){
    vector<string> ans;
    
    solve(ans,"",n,n);
    return ans;
}

int main(){
    
    auto a=generateParenthesis(3);
    for(string s: a) cout<<s<<endl;
    cout<<endl;
    return 0;
}