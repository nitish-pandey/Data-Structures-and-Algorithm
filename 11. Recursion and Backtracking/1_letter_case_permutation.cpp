#include<bits/stdc++.h>
using namespace std;

void swapCase(char &c1){
    if (c1>='a' && c1<='z') c1+='A'-'a';

    else if(c1>='A' && c1<='Z') c1-='A'-'a';


}

vector<string> ans;

void letterCasePermutation(string s,int st=0){
    if(st==s.length()){
        ans.push_back(s);
        return ;
    }
    if(s[st]>='0' && s[st]<='9') {
        letterCasePermutation(s,st+1);
        return ;
    }
    
    letterCasePermutation(s,st+1);
    swapCase(s[st]);
    letterCasePermutation(s,st+1);
    swapCase(s[st]);
}


int main(){

    letterCasePermutation("324z");
    for(string s :ans){
        cout<<s<<endl;
    }
    
    cout<<endl;
    return 0;
}