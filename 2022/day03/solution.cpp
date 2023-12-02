#include <iostream>
#include <stdio.h>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

vector<string> rucksacks;

void read_input(){
    string line;
    while(getline(cin, line)){
        rucksacks.push_back(line);
    }
}

void solve(){
    int n_elf = 0, sum_priorities = 0;
    string types = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    unordered_map<char, int> items, prio;

    for(int i = 0; i < types.size(); i++)
        prio[types[i]] = i+1;

    for(auto rucksack: rucksacks){

        // We end a group of rucksack, find common badge and reset
        if(n_elf == 3){
            for(auto &it: items){
                if(it.second == 3)
                    sum_priorities += prio[it.first];
            }
            n_elf = 0;
            items.clear();
        }
        // Initialize the first group elf's rucksack items
        if(n_elf == 0){
            for(auto item: rucksack)
                items[item] = 1;    
        }
        else{
            // Check for common items (little trick so we dont repeat the item for the same rucksack)
            for(auto item: rucksack){
                if(items[item]-n_elf ==0){
                    items[item] += 1;
                }
            }
        }
        n_elf++;
    }

    // Find the last group common item 
    for(auto &it: items){
                if(it.second == 3)
                    sum_priorities += prio[it.first];
    }
    cout << sum_priorities << endl;
}
    
int main(){
    read_input();
    solve();
    return 0;
}