
#include<stdio.h>
#include<stdlib.h>

typedef struct Treenode{
    int data;
    struct Treenode *left;
    struct Treenode *right;
} node;


node* insert(node* head,int data){

    if(head==NULL){

        node* temp=(node*)malloc(sizeof(node));
        temp->data=data;
        temp->left=NULL;
        temp->right=NULL;
        return temp;

    }

    if(data<head->data){
        head->left=insert(head->left,data);
    }
    else{
        head->right=insert(head->right,data);
    }

    return head;
}


void inorder(node* head){

    if(head==NULL){
        return;
    }

    inorder(head->left);
    printf("%d ",head->data);
    inorder(head->right);

}

void preorder(node* head){

    if(head==NULL){
        return;
    }

    printf("%d ",head->data);
    preorder(head->left);
    preorder(head->right);

}


void postorder(node* head){

    if(head==NULL){
        return;
    }

    postorder(head->left);
    postorder(head->right);
    printf("%d ",head->data);

}


int main(){

    node* head=NULL;
    head=insert(head,10);
    head=insert(head,5);
    head=insert(head,15);
    head=insert(head,3);
    head=insert(head,7);
    head=insert(head,12);
    head=insert(head,18);

    printf("Inorder: ");
    inorder(head);
    printf("\n");

    printf("Preorder: ");
    preorder(head);
    printf("\n");
    
    printf("Postorder: ");
    postorder(head);
    printf("\n");

    return 0;
}