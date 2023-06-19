//
// Created by Kevin Ha on 3/26/23.
//

#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n,q; cin>>n;
    vector<long long> input;
    vector<long long> input2;
    vector<long long> pfx(n+1,0);
    set<long long> ref;
    map<long long, int> ref2;
    for(int i=0; i<n;i++){
        long long a; cin>>a; input.push_back(a);
        input2.push_back(a);
        ref.insert(a);
    }
    sort(input.begin(), input.end());
    pfx[1]=input[0];
    for(int i=2; i<=n;i++){
        pfx[i]=pfx[i-1]+input[i-1];
    }
    long long T=0;
    for(int i=0; i<n;i++){
        T+=input[i]*(i+1);
        if(ref2.count(input[i]))ref2.erase(input[i]);
        ref2.insert(make_pair(input[i],i+1));
    }
    cin>>q;
    while(q--){
        long long a, b;  cin>>a>>b;a--;
        long long temp=T;
        long long oldpos=ref2[input2[a]];
        temp-=oldpos*input2[a];
        auto blah=--ref.upper_bound(b);
        long long newpos = ref2[*(blah)]+1;
        if(newpos>oldpos)newpos--;
        temp+=newpos*b;
        if(newpos<oldpos){
            temp+=(pfx[oldpos-1]-pfx[newpos-1]);
        }
        if(oldpos<newpos){
            temp-=(pfx[newpos]-pfx[oldpos]);
        }
        cout<<temp<<endl;
    }
}