

#include<stdio.h>
#include<stdlib.h>

typedef struct listnode{
    int data;
    struct listnode *next;
}node;


void push(node* head,int data){
    node *temp=(node*) malloc(sizeof(node));
    temp->data=data;

    temp->next=head->next;
    head->next=temp;

    return;
}

int pop(node* head){
    node *temp=head->next;
    int data=temp->data;
    head->next=temp->next;
    free(temp);
    return data;
}

int main(){
    node* head=(node*) malloc(sizeof(node));
    head->next=NULL;

    push(head,1);
    push(head,2);
    push(head,3);
    push(head,4);
    push(head,5);

    printf("%d",pop(head));

    return 0;
}