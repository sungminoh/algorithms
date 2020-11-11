#include <iostream>
#include <string.h>


using namespace std;


const int MAX = 1000;
char s1[MAX+1];
char s2[MAX+1];
int m[MAX+1][MAX+1];
int r[MAX+1][MAX+1];
char c[MAX+1];


void print_mat(int m[][MAX+1]){
    int l1 = strlen(s1);
    int l2 = strlen(s2);
    printf(" \t");
    for(int i=0; i<l2; ++i){
        printf("%c\t", s2[i]);
    }
    printf("\n");
    for(int i=1; i<=l1; ++i){
        printf("%c\t", s1[i-1]);
        for(int j=1; j<=l2; ++j){
            printf("%d\t", m[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    printf("%d\n", m[l1][l2]);
}


char* recover(int l1, int l2, int n){
    c[n] = '\0';
    while(n--){
        while(true){
            if(r[l1][l2] == 2){
                l2--;
            }else if(r[l1][l2] == 3){
                l1--;
            }else{
                break;
            }
        }
        c[n] = s1[l1-1];
        l1--;
        l2--;
    }
    return c;
}


int main(){
    scanf("%s %s", s1, s2);

    int l1 = strlen(s1);
    int l2 = strlen(s2);
    for(int i=1; i<=l1; ++i){
        char c1 = s1[i-1];
        for(int j=1; j<=l2; ++j){
            char c2 = s2[j-1];
            if(c1 == c2){
                m[i][j] = m[i-1][j-1]+1;
                r[i][j] = 1;
            }else{
                if(m[i][j-1] > m[i-1][j]){
                    m[i][j] = m[i][j-1];
                    r[i][j] = 2;
                }else{
                    m[i][j] = m[i-1][j];
                    r[i][j] = 3;
                }
            }
        }
    }

    printf("%d\n", m[l1][l2]);
    printf("%s\n", recover(l1, l2, m[l1][l2]));

    return 0;
}
