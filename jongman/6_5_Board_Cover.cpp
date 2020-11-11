#include <iostream>
#include <vector>

using namespace std;

typedef vector<vector<bool> > matrix;

matrix getBoard(int h, int w){
    matrix board;
    board.resize(h, vector<bool>(w, false));
    int cnt = 0;
    for(int i=0; i<h; ++i){
        char s[21];
        scanf("%s", s);
        for(int j=0; j<w; ++j){
            if(s[j] == '.'){
                board[i][j] = true;
                cnt ++;
            }
        }
    }
    return board;
}

void printMat(matrix &m){
    for(matrix::iterator it=m.begin(); it!=m.end(); ++it){
        for(vector<bool>::iterator itt=(*it).begin(); itt!=(*it).end(); ++itt){
            printf("%c", (*itt) ? '.' : '#');
        }
        printf("\n");
    }
}

bool put(int i, int j, matrix &board, int tile[3][2]){
    int h = board.size(), w = board[0].size();
    for(int k=0; k<3; ++k){
        int toX = tile[k][0];
        int toY = tile[k][1];
        int x = i + toX;
        int y = j + toY;
        if(x>=h || x<0 || y>=w || y<0 || !board[x][y]){
            return false;
        }
    }
    for(int k=0; k<3; ++k){
        int toX = tile[k][0];
        int toY = tile[k][1];
        int x = i + toX;
        int y = j + toY;
        board[x][y] = false;
    }
    return true;
}

void unput(int i, int j, matrix &board, int tile[3][2]){
    for(int k=0; k<3; ++k){
        int toX = tile[k][0];
        int toY = tile[k][1];
        int x = i + toX;
        int y = j + toY;
        board[x][y] = true;
    }
}


int numberOfWaysToCover(matrix &board){
    int h = board.size(), w = board[0].size();

    int x = -1, y = -1;
    for(int i=0; i<h; ++i){
        for(int j=0; j<w; ++j){
            if(board[i][j]){
                x = i;
                y = j;
                break;
            }
        }
        if(y != -1) break;
    }
    if(y == -1) return 1;

    int ret = 0;
    int tiles[4][3][2] = {
        {{0, 0}, {1, 0}, {0, 1}},
        {{0, 0}, {1, 0}, {1, 1}},
        {{0, 0}, {0, 1}, {1, 1}},
        {{0, 0}, {1, 0}, {1, -1}}
    };
    for(int k=0; k<4; ++k){
        if(put(x, y, board, tiles[k])){
            ret += numberOfWaysToCover(board);
            unput(x, y, board, tiles[k]);
        }
    }

    return ret;
}

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int h, w;
        scanf("%d %d", &h, &w);
        matrix board = getBoard(h, w);
        // if the number of whites are not divided by 3.
        int numberOfWhites = 0;
        for(int i=0; i<h; ++i)
            for(int j=0; j<w; ++j)
                if(board[i][j])
                    numberOfWhites ++;
        if(numberOfWhites % 3 != 0){
            printf("0\n");
            continue;
        }
        // otherwise.
        printf("%d\n", numberOfWaysToCover(board));
    }
    return 0;
}
