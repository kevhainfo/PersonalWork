//
// Created by Kevin Ha on 12/18/22.
//

#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#include<math.h>
#include<cstring>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n; cin>>n;
    vector<int> numbers; numbers.push_back(10000000000);numbers.push_back(10000000000);
    for(int i=0; i<n;i++){
        int a; cin>>a; numbers.push_back(a);
        numbers.push_back(10000000000);
    }
    string res="";

    int pointer=1;
    while(pointer>0){
        if(pointer==1&&numbers[2]==0)break;
        while(numbers[pointer+1]>1&&pointer<n*2+1){
            if(pointer%2!=0) {
                res+="R";
            }
            numbers[pointer]--;
            pointer++;
        }
        while(numbers[pointer-1]>=1&&pointer>1){
            if(numbers[pointer-1]==1){
                if(pointer!=n*2+1&&numbers[pointer+1]>1){
                    break;
                }
            }
            if(pointer%2!=0){
                res+="L";
            }
            numbers[pointer]--;
            pointer--;
        }
    }
    cout<<res<<endl;
}

