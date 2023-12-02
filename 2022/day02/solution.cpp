#include <iostream>
#include <stdio.h>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

vector<string> rounds;

void read_input(){
    string line;
    while(getline(cin, line)){
        rounds.push_back(line);
    }
}

void solve(){
    int score = 0;
    unordered_map<char, int> points;
    unordered_map<char, int> play2win;
    unordered_map<char, int> play2lose;

    points['A'] = 1;
    points['B'] = 2;
    points['C'] = 3;

    play2win['A'] = 'B';
    play2win['B'] = 'C';
    play2win['C'] = 'A';

    play2lose['A'] = 'C';
    play2lose['B'] = 'A';
    play2lose['C'] = 'B';
     
    for(auto round: rounds){
        char adv = round[0], choice = round[2];
        score += points[choice];
        if(choice == 'X')
            score += points[play2lose[adv]];
        else if(choice == 'Y')
            score += 3 + points[adv];
        else
            score += 6 + points[play2win[adv]];
    }
    cout << score << endl;    
}

int main(){
    read_input();
    solve();
    return 0;
}
