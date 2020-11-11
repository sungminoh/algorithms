#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef vector<vector<char> > matrix;

void decompress(matrix &decompressed, string::iterator &it, int y, int x, int size){
    char head = *(it++);
    if(head == 'b' || head == 'w'){
        for(int dy=0; dy<size; ++dy){
            for(int dx=0; dx<size; ++dx){
                decompressed[y+dy][x+dx] = head;
            }
        }
    }else{
        int half = size/2;
        decompress(decompressed, it, y, x, half);
        decompress(decompressed, it, y, x+half, half);
        decompress(decompressed, it, y+half, x, half);
        decompress(decompressed, it, y+half, x+half, half);
    }
}

string reverse(string::iterator &it){
    char head = *(it++);
    if(head == 'b' || head == 'w'){
        return string(1, head);
    }else{
        string ul = reverse(it);
        string ur = reverse(it);
        string ll = reverse(it);
        string lr = reverse(it);
        return string("x") + ll + lr + ul + ur;
    }
}

int getDepth(string::iterator &it){
    char head = *(it++);
    if(head == 'b' || head == 'w'){
        return 1;
    }else{
        int depths[4];
        depths[0] = getDepth(it);
        depths[1] = getDepth(it);
        depths[2] = getDepth(it);
        depths[3] = getDepth(it);
        int m = depths[0];
        for(int i=1; i<4; ++i){
            if( depths[i] > m)
                m = depths[i];
        }
        return 1 + m;
    }
}

void printMat(matrix &m){
    int size = m.size();
    for(int i=0; i<size; ++i){
        for(int j=0; j<size; ++j){
            if(m[i][j] == 'w'){
                printf(".");
            }else{
                printf("#");
            }
        }
        printf("\n");
    }
}


int main(){
    int c;
    scanf("%d", &c);
    while(c--){
        string s;
        cin >> s;
        string::iterator it = s.begin();
        int depth = getDepth(it);
        int size = pow(2, depth-1);
        it = s.begin();
        s = reverse(it);
        cout << "reversed: " << s << endl;
        it = s.begin();
        matrix decompressed;
        decompressed.resize(size, vector<char>(size));
        decompress(decompressed, it, 0, 0, size);
        printMat(decompressed);
    }
    return 0;
}
