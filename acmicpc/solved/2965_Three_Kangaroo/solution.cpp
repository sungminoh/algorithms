#include <iostream>

using namespace std;

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    b-a > c-b ? printf("%d\n", b-a-1) : printf("%d\n", c-b-1);
    return 0;
}
