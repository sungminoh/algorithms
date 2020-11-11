#include <iostream>
#include <vector>

using namespace std;

typedef vector<vector<int> > matrix;

int getValue(int r, int c){
    if(r==0 && c==0){
        return 1;
    }else if(r < 0 && (r <= c && c <= -r)){
        return 4*r*r + 1 + r - c;
    }else if(r > 0 && (-r <= c && c <= r)){
        return 4*r*r + 3*r + 1 + c;
    }else if(c < r){
        return 4*c*c + 1 + r - c;
    }else if(c > r){
        return 4*(c-1)*(c-1) + 4*(c-1) + 1 + c - r;
    }
    return 0;
}

void printTornado(int r1, int c1, int r2, int c2){
    int edges[4];
    edges[0] = getValue(r1, c1);
    edges[1] = getValue(r1, c2);
    edges[2] = getValue(r2, c1);
    edges[3] = getValue(r2, c2);
    int m = 0;
    for(int i=0; i<4; ++i){
        if(edges[i] > m) m = edges[i];
    }
    int d = 0;
    while(m > 0){
        d++;
        m /= 10;
    }

    for(int r=r1; r<=r2; ++r){
        for(int c=c1; c<c2; ++c){
            printf("%*d ", d, getValue(r, c));
        }
        printf("%*d\n", d, getValue(r, c2));
    }
}

int main(){
    int r1, c1, r2, c2;
    scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
    printTornado(r1, c1, r2, c2);

    return 0;
}
