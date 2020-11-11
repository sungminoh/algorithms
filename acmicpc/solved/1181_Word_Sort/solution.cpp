#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main(){
    int N;
    set<string> words[51];
    string word;
    scanf("%d ", &N);
    for(int i=0; i<N; ++i){
        getline(cin, word);
        words[word.length()].insert(word);
    }

    for(int i=0; i<51; ++i){
        //sort(words[i].begin(), words[i].end());
        for(auto& it : words[i]){
            cout << it << endl;
        }
    }
    return 0;
}
