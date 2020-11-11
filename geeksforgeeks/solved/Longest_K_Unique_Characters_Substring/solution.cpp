#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int getLogestKUniqueCharactersSubstring(string s, int k){
    int len = s.length();
    int i=0, j=0, cnt=0;
    unordered_map<char, int> m;
    while(j < len){
        auto lit = m.find(s[i]);
        auto rit = m.find(s[j]);
        if(rit == m.end()){
            cnt++;
            m.insert(make_pair(s[j], 1));
        }else{
            (*rit).second++;
        }
        if(cnt > k){
            (*lit).second --;
            if((*lit).second == 0){
                m.erase(lit);
                cnt--;
            }
            i++;
            j++;
        }else{
            j++;
        }
    }
    if(cnt < k){
        return -1;
    }
    return j-i;
}

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        string s;
        cin >> s;
        int k;
        cin >> k;
        printf("%d\n", getLogestKUniqueCharactersSubstring(s, k));
    }
    return 0;
}
