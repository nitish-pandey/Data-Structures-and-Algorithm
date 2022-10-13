#include<bits/stdc++.h>
using namespace std;

struct node {
    int data;
    node* left;
    node* right;
    node(int a){
        data=a;
        left=NULL;
        right=NULL;
    }
    node(){
        left=NULL;
        right=NULL;
        data=-1;
    }
};

node* insert(node* root,int data){
    if(!root){
        return new node(data);
    }
    if(root->data >data){
        root->left=insert(root->left,data);
    }
    else {
        root->right=insert(root->right,data);
    }
    return root;
}

map<pair<node*,int> ,int> dp;

int houseRobber3(node* root,int mode=0){
    if(!root) return 0;
    if(dp.count({root,mode})>0) return dp[{root,mode}];

    if(mode==0){
        int opt1=houseRobber3(root->left,0)+houseRobber3(root->right);
        int opt2=root->data+houseRobber3(root->left,1)+houseRobber3(root->right,1);
        dp[{root,mode}]= max(opt1,opt2);
    }
    else dp[{root,mode}]= houseRobber3(root->left)+houseRobber3(root->right);

    return dp[{root,mode}];
}

int main(){
    
    vector<int> nums={3,4,5,2,6,1,9};
    node* root=NULL;
    for(int i: nums) root=insert(root,i);

    cout<<houseRobber3(root);

    cout<<endl;
    return 0;
}