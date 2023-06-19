//
// Created by Kevin Ha on 3/26/23.
//

#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
using namespace std;
struct bessie{
    int start,end;
};
int main(){
    string s; cin>>s; int n=s.size();
    vector<bessie> input;
    long long res=0;
    string b="bessie"; int counter=0; int i=0;
    while(i<n){
        if(s[i]=='b') {
            int start=i;
            while (counter < 6 && i < n) {
                if (s[i] == b[counter]) {
                    counter++;
                }
                if(counter!=0&&s[i]=='b'){
                    i--;
                    break;
                }
                i++;
            }
            if(counter==6){
                input.push_back(bessie{start, --i});
            }
            counter=0;
        }
        i++;
    }
    cout<<"hi";

}