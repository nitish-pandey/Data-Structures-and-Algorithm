
#include<stdio.h>

#include<stdlib.h>

typedef struct ListNode{
    int data;
    struct node *next;
}node;

node* create_queue(){
    node* head=(node*) malloc(sizeof(node));
    head->next=NULL;
    return head;
}

void enqueue(node* head,int data){
    node *temp=(node*) malloc(sizeof(node));
    temp->data=data;
    node *p=head;
    while(p->next!=NULL){
        p=p->next;
    }
    p->next=temp;
    temp->next=NULL;
    return;
}

int dequeue(node* head){
    node *temp=head->next;
    int data=temp->data;
    head->next=temp->next;
    free(temp);
    return data;
}

int main(){

    
}