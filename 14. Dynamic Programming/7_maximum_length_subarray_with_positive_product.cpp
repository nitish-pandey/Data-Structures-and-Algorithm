#include<bits/stdc++.h>
using namespace std;

int solve(vector<int> &nums){
    int ans=0;
    int pos=0,neg=0;

    for(int a:nums){
        if(a==0){
            pos=0;
            neg=0;
            continue;
        }

        if(a>0){
            pos++;
            if(neg) neg++;
        }
        else{
            swap(pos,neg);

            neg++;
            if(pos) pos++;
        }
        ans=max(ans,pos);
    }
    return ans;
}

int main(){
    
    
    cout<<endl;
    return 0;
}