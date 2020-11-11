#include <iostream>

int T, M, N, x, y, k, i;
bool found;

int main(){
    scanf("%d", &T);
    while(T--){
        scanf("%d%d%d%d", &M, &N, &x, &y);
        x--;
        y--;
        found = false;
        for(i=0; ; ++i){
            if((M * i + x) % N == y){
                found = true;
                break;
            }
            if(i != 0 && (M * i) % N == 0){
                break;
            }
        }
        if(found){
            printf("%d\n", i*M + x+1);
        }else{
            printf("%d\n", -1);
        }
    }

    return 0;
}
