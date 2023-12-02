#include <iostream>
#include <stdio.h>

using namespace std;

void solve(){
    int most_calories_1 = 0, most_calories_2 = 0,most_calories_3 = 0, elf_calories = 0, cal;
    while(cin >> cal){
        if(cal == -1){
            cout << "elf" << i << ":" << elf_calories << endl;
            if(elf_calories > most_calories_1){
                most_calories_3 = most_calories_2;
                most_calories_2 = most_calories_1;
                most_calories_1 = elf_calories;
            }
            else if(elf_calories > most_calories_2){
                most_calories_3 = most_calories_2;
                most_calories_2 = elf_calories;
            }
            else if (elf_calories > most_calories_3){
                most_calories_3 = elf_calories;
            }
            elf_calories = 0;
        }
        else{
            elf_calories += cal;
        }        
    }
    cout << sum << endl;
}

int main(){
    solve();
    return 0;
}
