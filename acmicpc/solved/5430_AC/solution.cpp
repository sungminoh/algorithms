#include <iostream>
#include <sstream>
#include <iterator>
#include <deque>
#include <cstring>


using namespace std;


deque<int> str2intDeq(string s){
    deque<int> ret;
    stringstream iss(s);
    string word;
    while(getline(iss, word, ',')){
        ret.push_back(stoi(word));
    }
    return ret;
}

string intDeq2str(deque<int> deq, bool isReverse){
    stringstream ss;
    ss << '[';
    while(deq.size() > 1){
        int value = isReverse ? deq.back() : deq.front();
        isReverse? deq.pop_back() : deq.pop_front();
        ss << value << ',';
    }
    if(deq.size() == 1)
        ss << deq.front();
    ss << ']';
    return ss.str();
}

int main(){
    int T;
    scanf("%d", &T);

    while(T--){
        char command[100005];
        scanf("%s", command); getchar();
        int commandLength = strlen(command);

        int n;
        scanf("%d", &n); getchar();

        string s;
        getline(cin, s);
        s = s.substr(1, s.length()-2);
        deque<int> deq = str2intDeq(s);

        bool isFail = false;
        bool isReverse = false;
        for(int i=0; i<commandLength; ++i){
            if(command[i] == 'R'){
                isReverse = !isReverse;
            }else{
                if(deq.empty()){
                    isFail = true;
                    break;
                }
                if(isReverse){
                    deq.pop_back();
                }else{
                    deq.pop_front();
                }
            }
        }

        if(isFail){
            printf("error\n");
        }else{
            string result = intDeq2str(deq, isReverse);
            printf("%s\n", result.c_str());
        }
    }

    return 0;
}
