#include <iostream>
#include <string>

int options;

int xp = 0;
int requiredXP = 100;
int level = 0;

void checks() {
if (xp >= requiredXP) {
    level++;
    std::cout << "You leveled up! Current level: " << level << "\n";
    xp -= requiredXP;
    requiredXP += 100;
    checks();
}
}

//very secret dev hack haha
void giveXP(int number) {
    xp += number;
    checks();
}

void play() {
    std::cout << "1. pet your pet     2.feed your pet     3.stats\n";
    std::cin >> options;

    if (options == 1) {
        xp += 10;
        std::cout << "you pet your pet. +10xp\n";
        checks();
    }

    if (options == 2) {
        int food_options;
        std::cout << "What do you want to feed your pet?\n";
        std::cout << "1.Pizza     2.Donut\n";
        std::cin >> food_options;

        if (food_options == 1) {
            xp += 5;
            std::cout << "You feed pizza to your pet. +5xp\n";
            checks();
        }

        if (food_options == 2) {
            xp += 5; 
            std::cout << "You feed pizza to your pet. +5xp\n";
            checks();
        }

    }

    if (options == 3) {
        std::cout << "stats:\n";
        std::cout << "xp:" << xp << std::endl;
        std::cout << "xp for next level: " << requiredXP << std::endl;
        std::cout << "level: " << level << std::endl;
    }
    
    //😇
    if (options == 69) {
        int XPnumber;
        std::cout << "Enter the amount of XP:";
        std::cin >> XPnumber;
        std::cout << std::endl;
        giveXP(XPnumber);
    }

    play();
}


int main() {
    std::cout << "pet\n";
    play();
}
