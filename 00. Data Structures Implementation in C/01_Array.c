

#include<stdio.h>
#include<stdlib.h>

// 1   2   3     4    5    6


typedef struct Array_ds{
    int arr[100];
    int size;
    int capacity;
}array;

array* create(){
    array *arr=(array*) malloc(sizeof(array));

    arr->size=0;
    arr->capacity=100;
}

void append(array *a,int value){
    if(a->size==a->capacity){
        return;
    }
    a->arr[a->size]=value;
    a->size++;
}

void insert(array *a,int value,int index){

    int x=a->size;

    for(int i=x;i>index;i--){
        a->arr[i]=a->arr[i-1];
    }

    a->arr[index]=value;

    a->size++;
}


void delete(array *a,int index){

    for(int i=index;i<a->size;i++){
        a->arr[i]=a->arr[i+1];
    }

    a->size--;

}



int main(){


    return 0;
}