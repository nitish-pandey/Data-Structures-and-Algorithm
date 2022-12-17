
#include<bits/stdc++.h>
using namespace std;


void for_C_Language(){


    // For C language we use 2 methods: Malloc and Calloc for allocation

    int n=10;

    int *a=(int*) malloc(sizeof(int)*n);

    for(int i=0;i<n;i++) a[i]=i*i;

    int *b=(int*) calloc(sizeof(int),n);

    for(int i=0;i<n;i++) b[i]=i*i;


    delete(a);
    delete(b);

}


void for_Cpp_Language(){

    // for C++ language we use new operators

    int n=10;

    int *a=new int();

    *a=10;
    cout<<a<<"\n";


    // Deallocate the memory using delete keyword
    delete(a);


    // allocate the memory dynamically pointed by same pointer 'a'

    a=new int[n];

    delete(a);

}

int main(){

    return 0;
}