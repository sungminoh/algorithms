#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

template<typename Out>
void split(const string &s, char delim, Out result) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        *(result++) = stoi(item);
    }
}

vector<int> split(const string &s, char delim) {
    vector<int> elems;
    split(s, delim, back_inserter(elems));
    return elems;
}

string intVecToString(vector<int> v, char delim){
    ostringstream ss;
    for_each(v.begin(), v.end(), [&ss, delim](int n){
            string c = to_string(n);
            ss << c;
            ss << delim;
            });
    ss.seekp(-1, ss.cur);
    return ss.str();
}


string join(vector<int>& v, string delim){
    stringstream ss;
    for_each(v.begin(), v.end()-1, [&](int x){ss << to_string(x) << delim;});
    ss << *v.rbegin();
    return ss.str();
}


vector<int> getInput(){
    string s;
    getline(cin, s);
    stringstream ss(s);
    vector<int> v;
    int n;
    while(ss >> n)
        v.push_back(n);
    return v;

}

