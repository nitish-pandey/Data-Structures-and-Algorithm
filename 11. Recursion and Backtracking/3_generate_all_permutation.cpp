#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> ans;

void generateAllPermutation(vector<int> &temp,int st=0){
    if(st==temp.size()-1){
        ans.push_back(temp);
        return ;
    }
    for(int i=st;i<temp.size();i++){

        swap(temp[st],temp[i]);
        generateAllPermutation(temp,st+1);
        swap(temp[st],temp[i]);
    }
}

int main(){
    vector<int> nums={1,2,3};
    generateAllPermutation(nums);

    for(auto a:ans){
        for(int i:a){
            cout<<i<<" ";
        }
        cout<<endl;
    }
    
    cout<<endl;
    return 0;
}