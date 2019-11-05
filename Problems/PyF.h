#ifndef  PYF_H
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <ctime>
#include <cstring>
#define PYF_H

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::to_string;
using std::count;
using std::vector;
using std::move;

class Agent{
private:

    vector<string> ans;
    string guess;

    static vector<string> findPossAns(){
        vector<string> ans;
        for(int i = 122; i<9880;i++){
            string x;
            if(i<1000) x = "0"+ to_string(i);
            else x = to_string(i);
            bool valid = 1 == count(x.begin(), x.end(), x[0]) == count(x.begin(), x.end(), x[1]) == count(x.begin(), x.end(), x[2]) == count(x.begin(), x.end(), x[3]);
            if(valid) ans.push_back(x);
        }
        return ans;
    };

    void decrease(int picas, int fijas){
        int index = 0;
        while(index < ans.size()){
            if(remove(ans[index], picas, fijas))
                ans.erase(ans.begin()+index);
            else
                index ++;
        }
    };

    bool remove(string poss_ans, int picas, int fijas){
        int nPicas = 0;
        int nFijas = 0;
        for(ulong i = 0; i < guess.size(); i++){
            if(count(poss_ans.begin(),poss_ans.end(),guess[i])){
                int k = poss_ans.find(guess[i]);
                if(k == i) nFijas++;
                if(k != i) nPicas++;
            }
        }
        return !(nFijas == fijas && nPicas == picas);
    };

public:

    Agent(){
        ans =  findPossAns();
        guess = "";
        srand (time(nullptr));
    };

    string sensors(string perception){
        if(perception == "START"){
            srand (time(nullptr));
            guess = ans[rand() % ans.size()];
            return guess;
        }else{
            if((perception[1]-'0') == 4)return "STOP";
            decrease(perception[0]-'0', perception[1]-'0');
            if(ans.size() == 0)return "TRAMPA";
            srand (time(nullptr));
            guess = ans[rand() % ans.size()];
            return guess;
        }
    };
};

class Environment{
private:

    int turn;
    Agent agent;

    string perception(){
        if(turn == 0){
            turn++;
            return "START";
        }else{
            turn++;
            string p,f;
            cout << "P F"<<endl;
            cin >> p >> f;
            return p+f;
        }
    }

    void OneAgentPlay(){
        string action = agent.sensors(perception());
        int c1 = action.compare("STOP");
        int c2 = action.compare("TRAP");
        while(c1 != 0 && c2 != 0){
            cout << "Turn: "<< turn << endl;
            cout << action << endl;
            action = agent.sensors(perception());
            c1 = action.compare("STOP");
            c2 = action.compare("TRAP");
        }if(action == "STOP") cout << endl << "GOOD GAME" << endl;
        if(action == "TRAP") cout << endl << "YOU CHEATED" << endl;
    }

public:

    explicit Environment(Agent in){
        turn = 0;
        agent = move(in);
    }

    void start(){
        cout << endl;
        OneAgentPlay();
    }
};
#endif