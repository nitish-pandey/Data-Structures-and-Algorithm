#include<bits/stdc++.h>
using namespace std;

vector<int> searchRange(vector<int> &nums,int target){
    int n=nums.size();
    if(n==0) return vector<int> {};

    int first=-1;
    int st=0,end=n-1;

    while(st<=end){
        int mid=(st+end)/2;
        if(nums[mid]==target){
            first=mid;
            
            while(first>0 && nums[first-1]==nums[mid]) first--;
            break;
        }
        if(nums[mid]>target) end=mid-1;
        else st=mid+1;
    }
    if(first==-1) return vector<int> {-1,-1};

    int last=first;
    while(last<nums.size()&& nums[last]==nums[first]){
        last++;
    }
    return vector<int> {first,last-1};

}

int main(){
    
    vector<int> nums={5,7,7,8,8,10};
    auto a=searchRange(nums,6);
    for(int i :a){
        cout<<i<<" ";
    }
    cout<<endl;
    return 0;
}