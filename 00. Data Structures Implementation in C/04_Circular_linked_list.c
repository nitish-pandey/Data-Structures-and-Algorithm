

#include<stdio.h>
#include<stdlib.h>

typedef struct listnode{
    int data;
    struct listnode *next;
}node;

// We create a linked list with a Empty head node
// Head node won't contain any data
// The data Storage will start from next of head

node* create_linkedlist(){
    node* head=(node*) malloc(sizeof(node));
    head->next=NULL;

    return head;
}

void insert_begin(node* head,int data){

    node *temp=(node*) malloc(sizeof(node));
    temp->data=data;

    temp->next=head->next;
    head->next=temp;

    return;
}

// Printing a Linked list

void print_ll(node* head){
    node* temp=head->next;
    if(temp ==NULL){
        printf("Empty Linked list");
    }
    printf("The Linked list is :\n");
    while(temp){
        printf("%d-> ",temp->data);
        temp=temp->next;
    }

    return ;
}

int main(){

    node* head=create_linkedlist();
    insert_begin(head,10);
    insert_begin(head,20);
    insert_begin(head,30);

    print_ll(head);

    return 0;
}
