#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> combinationalSum1(vector<int> &candidates,int target);
vector<vector<int>> combinationalSum2(vector<int> &candidates,int target);
void solve1(vector<int> &candidates,vector<int> temp,int target,int ind);
void solve1(vector<int> &candidates,vector<int> temp,int target,int ind);


int main(){
    
    vector<int> candidate={10,1,2,7,6,1,5};
    int target=8;

    vector<vector<int>> t=combinationalSum2(candidate,target);

    for(auto a: t){
        for(int i:a) cout<<i<<" ";
        cout<<endl;
    }
    cout<<endl;
    return 0;
}


// in this , we find all the possible combination of the sum of elements of candidates to get the target value
// taking one value multiple times is allowed

vector<vector<int>> ans;

void solve1(vector<int> &candidates,vector<int> temp,int target,int ind){

    if(target==0) {
        ans.push_back(temp);
        return ;
    }
    if(target<0) return ;

    while(ind<candidates.size() && candidates[ind]<=target){

        temp.push_back(candidates[ind]);
        solve1(candidates,temp,target-candidates[ind],ind);
        ind++;

        // backtracking
        temp.pop_back();
    }

    
}
vector<vector<int>> combinationalSum1(vector<int> &candidates,int target){
    
    sort(candidates.begin(),candidates.end());
    
    // remove the duplicates
    candidates.erase(unique(candidates.begin(), candidates.end()), candidates.end());

    vector<int> temp;

    solve1(candidates,temp,target,0);

    return ans;

}



// in this , we find all the unique possible combination of the sum of elements of candidates to get the target value
// we can take one element only one time and we can't take the same element twice ( allowed if repeated in candidates)

vector<vector<int>> ans2;


void solve2(vector<int> &candidates,vector<int> temp,int target,int ind,vector<int> hash){
    if(target==0){
        ans2.push_back(temp);
        return ;
    }
    if(target<0) return ;
    if(ind>=candidates.size()) return ;

    solve2(candidates,temp,target,ind+1,hash);

    int a=candidates[ind];
    if(target<a) return ;

    temp.push_back(a);
    if(hash[a]>0){
        hash[a]--;
        solve2(candidates,temp,target-a,ind,hash);
    }
    temp.pop_back();
}


vector<vector<int>> combinationalSum2(vector<int> &candidates,int target){

    sort(candidates.begin(),candidates.end());

    vector<int> hash(target+1,0);
    for(int i:candidates) hash[i]++;
    
    // remove the duplicates
    candidates.erase(unique(candidates.begin(), candidates.end()), candidates.end());

    vector<int> temp;


    solve2(candidates,temp,target,0,hash);

    return ans2;

}
