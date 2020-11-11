#include <iostream>

using namespace std;

int paper[2187][2187];
int cnt[4];


int getAnswer(int x, int y, int n){
    if(n == 1){
        return paper[x][y];
    }
    int leftUpper;
    bool one = true;
    for(int i=0; i<3; ++i){
        int x_ = x + (i*(n/3));
        for(int j=0; j<3; ++j){
            int y_ = y + (j*(n/3));
            int sub = getAnswer(x_, y_, n/3);
            if(x_ == x && y_ == y){
                if(sub == 2){
                    one = false;
                }
                leftUpper = sub;
            }else{
                if(leftUpper != sub && one){
                    one = false;
                    cnt[leftUpper+1] += (i*3 + j);
                }
                if(!one){
                    cnt[sub+1] ++;
                }
            }
        }
    }
    if(one){
        return leftUpper;
    }else{
        return 2;
    }
}

int main(){
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j){
            scanf("%d", &paper[i][j]);
        }
    }

    getAnswer(0, 0, n);

    for(int i=0; i<3; ++i){
        printf("%d\n", cnt[i]);
    }

    return 0;
}
