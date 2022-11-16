
#include<stdio.h>
#include<stdlib.h>

int vertices[100];
int no_of_vertices=0;

int edges[100][100];


void add_vertex(int vertex){
    if(no_of_vertices==100){
        printf("Graph is full\n");
        return;
    }

    if (vertex<0){
        printf("Vertex cannot be negative\n");
        return;
    }

    if(vertices[vertex]==1){
        return;
    }

    vertices[no_of_vertices++]=vertex;
}

void add_edge(int vertex1,int vertex2){
    if(vertex1==vertex2){
        printf("Self loop not allowed\n");
        return;
    }
    if(vertex1<0 || vertex2<0){
        printf("Negative vertices not allowed\n");
        return;
    }
    if(vertex1>100 || vertex2>100){
        printf("Vertex not found\n");
        return;
    }
    add_vertex(vertex1);
    add_vertex(vertex2);

    edges[vertex1][vertex2]=1;
}



int main(){

    add_edge(0,1);
    add_edge(0,2);
    add_edge(1,2);
    add_edge(2,0);
    add_edge(2,3);
    add_edge(3,3);

    for(int i=0;i<no_of_vertices;i++){
        for(int j=0;j<no_of_vertices;j++){
            printf("%d ",edges[i][j]);
        }
        printf("\n");

    }

    return 0;
}