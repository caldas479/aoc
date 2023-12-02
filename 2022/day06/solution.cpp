#include <iostream>
#include <stdio.h>
#include <unordered_map>
#include <string>

using namespace std;

int main(){
    string input;
    getline(cin,input);
    int l = 0, r = 13;
    unordered_map<char,int> seen_index;
    while(l <= r){
        char c = input[l];
        if(!seen_index[c]){
            seen_index[c] = l + 1;
            l++;
        }
        else{
            l = seen_index[c];
            r = l + 13;
            seen_index.clear();
        }
    }
    cout << l << endl;
}