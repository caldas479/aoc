#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>
#include <stack>
#include <bits/stdc++.h>

using namespace std;

#define N_STACKS 9

vector<vector<char>> vecs={{},{},{},{},{},{},{},{},{}};
vector<stack<char>> stacks;
vector<vector<int>> moves;

void solve(){  
    string line;
    int c =0;
    while(c < 8){
        getline(cin,line);
        for(int i = 1, index = 0; i < line.size(); i+= 4, index ++){
            if(line[i] != ' ')
                vecs[index].push_back(line[i]);
        }
        c++;
    }
    for(int i = 0; i < N_STACKS; i++){
        stack<char> s;
        stacks.push_back(s);
        reverse(vecs[i].begin(),vecs[i].end());
        for(auto x: vecs[i]){
            stacks[i].push(x);
            
        } 
    }

    // APLYING MOVES
    int n, src, dst;
    while(scanf(" %d  %d  %d",&n,&src,&dst)==3){
        vector<char> newstack;
        while(n){
            newstack.push_back(stacks[src-1].top());
            stacks[src-1].pop();
            n--;
        }
        reverse(newstack.begin(), newstack.end());
        for(auto c: newstack){
            stacks[dst-1].push(c);
        }
    }

    // PRINTING ANSWER
    for(int i = 0; i < N_STACKS; i++){
        stack<char> s = stacks[i];
        cout << s.top();
    }
        cout << endl;
     
}

int main(){
    solve();
    return 0;
}