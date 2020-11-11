#include <iostream>
#include <cstring>

using namespace std;

const int MAX = 101;

string p, s;
int cache[MAX][MAX];

bool match(int i, int j){
    int &ret = cache[i][j];
    if(ret != -1){
        return ret;
    }

    if(i < p.size() && j < s.size() && (p[i] == '?' || p[i] == s[j])){
        return ret = match(i+1, j+1);
    }

    if(i == p.size()){
        return ret = (j == s.size());
    }

    if(p[i] == '*'){
        return ret = (match(i+1, j) || (j < s.size() && match(i, j+1)));
    }

    return ret = 0;
}

int main(){
    int c;
    scanf("%d", &c);
    while(c--){
        cin >> p;
        int n;
        scanf("%d", &n);
        while(n--){
            cin >> s;
            memset(cache, -1, sizeof cache);
            if(match(0, 0)){
                cout << s << endl;
            }
        }
    }
    return 0;
}
