#include <iostream>
#include <map>
#include <stdlib.h>

using namespace std;

void insert(map<string, int> &m, string type){
    if(m.find(type) != m.end()){
        m[type]++;
    }else{
        m.insert(make_pair(type, 1));
    }
}

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        map<string, int> m;
        while(n--){
            char cloth[22];
            string type;
            cin >> cloth >> type;
            //scanf("%s %s", cloth, type);
            insert(m, type);
        }
        int sum = 1;
        for(map<string, int>::iterator it=m.begin(); it!=m.end(); it++){
            //cout << "key: " << (*it).first << ", cnt: " << (*it).second << endl;
            sum *= (*it).second + 1;
        }
        printf("%d\n", sum-1);
    }
    return 0;
}
