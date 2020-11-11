#include <iostream>
#include <map>

using namespace std;

int main(void){
    map<string, int> dic;
    dic.insert(make_pair("monday", 0));
    dic.insert(make_pair("tuesday", 1));
    dic.insert(make_pair("wednesday", 2));
    dic.insert(make_pair("thursday", 3));
    dic.insert(make_pair("friday", 4));
    dic.insert(make_pair("saturday", 5));
    dic.insert(make_pair("sunday", 6));

    string day1, day2;
    cin >> day1;
    cin >> day2;
    //cout << dic.find(day1)->first << "\n";
    //cout << dic.find(day1)->second << "\n";
    //cout << dic.find(day2)->first << "\n";
    //cout << dic.find(day2)->second << "\n";

    int gap = dic.find(day2)->second - dic.find(day1)->second;
    if (gap < 0){
        gap += 7;
    }
    if (gap == 3 || gap == 0 || gap == 2){
        cout << "YES";
    }else{
        cout << "NO";
    }
}
