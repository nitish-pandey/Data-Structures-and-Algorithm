#include<bits/stdc++.h>
using namespace std;

vector<vector<bool>> row(9,vector<bool>(10,false));
vector<vector<bool>> col(9,vector<bool>(10,false));
vector<vector<bool>> sub(9,vector<bool>(10,false)); 

bool sudokuSolver(vector<vector<char>> &board,int i,int j){
    if(j>=9) {
        i++;
        j=0;
    }
    if(i>=9) return 1;

    if(board[i][j]!='.') return sudokuSolver(board,i,j+1);

    for(int k=1;k<=9;k++){
        if(row[i][k]) continue;
        if(col[j][k]) continue;
        if(sub[i/3*3+j/3][k]) continue;

        row[i][k]=true;
        col[j][k]=true;
        sub[i/3*3+j/3][k]=true;
        board[i][j]='0'+k;

        if(sudokuSolver(board,i,j+1)) return 1;

        board[i][j]='.';
        row[i][k]=false;
        col[j][k]=false;
        sub[i/3*3+j/3][k]=false;

    }
    return 0;
}

void sudokuSolver(vector<vector<char>> &board){
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            int a=board[i][j]-'0';
            if(a>9 || a<0) continue;

            row[i][a]=true;
            col[j][a]=true;
            sub[i/3*3+j/3][a]=true;
        }
    }
    sudokuSolver(board,0,0);
}

int main(){
    
    vector<vector<char>> board={{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}};
    
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cout<<board[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
    sudokuSolver(board);

    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cout<<board[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
    return 0;
}