#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<int> cleaning_pairs;

void read_input(){
    int x1,y1,x2,y2;
    while(scanf("%d-%d-%d-%d\n", &x1,&y1,&x2,&y2) == 4){
        cleaning_pairs.push_back(x1);
        cleaning_pairs.push_back(y1);
        cleaning_pairs.push_back(x2);
        cleaning_pairs.push_back(y2);
    }
}

void solve(){
    int overlaps = 0;
    for(int i = 0; i < cleaning_pairs.size(); i+=4){
        int x1 =cleaning_pairs[i] , y1 = cleaning_pairs[i+1], x2 = cleaning_pairs[i+2], y2 = cleaning_pairs[i+3];
        if(x1 <= x2 && y1 >= y2 || x2 <= x1 && y2 >= y1 || x1 >= x2 && x1 <= y2 || y1 >= x2 && y1 <= y2){
            overlaps++;
        }        
    }
    cout << overlaps <<endl;
}

int main(){
    read_input();
    solve();
    return 0;
}