

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

// inserting at the end

void insert_end(node* head,int data){
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

// inserting at a given position

void insert_pos(node* head,int data,int pos){
    node *temp=(node*) malloc(sizeof(node));
    temp->data=data;

    node *p=head;
    int i=1;
    while(i<pos){
        p=p->next;
        i++;
    }
    temp->next=p->next;
    p->next=temp;

    return;
}

// deleting from the beginning

void delete_begin(node* head){
    node *temp=head->next;
    head->next=temp->next;
    free(temp);

    return;
}

// deleting from the end

void delete_end(node* head){
    node *p=head;
    while(p->next->next!=NULL){
        p=p->next;
    }
    node *temp=p->next;
    p->next=NULL;
    free(temp);

    return;
}

// deleting from a given position

void delete_pos(node* head,int pos){
    node *p=head;
    int i=1;
    while(i<pos){
        p=p->next;
        i++;
    }
    node *temp=p->next;
    p->next=temp->next;
    free(temp);

    return;
}



// Printing a Linked list

void print_ll(node* head){
    node* temp=head->next;
    if(temp ==NULL){
        printf("Empty Linked list\n");
        return ;
    }
    printf("The Linked list is :\n");
    while(temp){
        printf("%d-> ",temp->data);
        temp=temp->next;
    }
    printf("NULL\n");
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