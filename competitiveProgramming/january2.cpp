//
// Created by Kevin Ha on 12/18/22.
//
#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#include<math.h>
#include<queue>
using namespace std;
char grid[1560][1560];
struct bale{
    int id;
    int x,y;
};
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;cin>>n;
    vector<int> baleCosts;
    vector<int> baleCounts(n*2,0);
    vector<bale> bales;
    int cost=0;
    for(int i=0; i<n;i++){
        string row; cin>>row;
        for(int j=0; j<n;j++){
            grid[i][j]=row[j];
        }
        int a; cin>>a;
        baleCosts.push_back(a);
        bales.push_back(bale{i,i,n});
    }
    for(int i=0; i<n;i++){
        int a; cin>>a;
        baleCosts.push_back(a);
        bales.push_back(bale{n+i,n,i});
    }
    queue<bale> q;
    for(int i=0; i<bales.size();i++){
        q.push(bales[i]);
    }
    int dirx[] ={0,-1};
    int diry[]={-1,0};
    while(!q.empty()){
        bale current=q.front();
        q.pop();
        for(int i=0; i<2; i++){
            int nx=current.x+dirx[i];
            int ny=current.y+diry[i];
            if(nx>=0&&nx<n&&ny>=0&&ny<n){
                if(i==0&&grid[nx][ny]=='R'){
                    q.push(bale{current.id,nx,ny});
                    baleCounts[current.id]++;
                }
                else if(i==1&&grid[nx][ny]=='D'){
                    q.push(bale{current.id,nx,ny});
                    baleCounts[current.id]++;
                }
            }
        }
    }
    //cout<<"yay"<<endl;
    for(int i=0; i<n*2;i++){
        cost+=baleCosts[i]*baleCounts[i];
    }
    //cout<<cost;
    int tests; cin>>tests;
    while(tests--){
        cout<<cost<<endl;
        int x,y; cin>>x>>y; x--; y--;
        grid[x][y]=(grid[x][y]=='R'?'D': 'R');
        for(int i=0; i<n*2;i++){
            baleCounts[i]=0;
        }
        for(int i=0; i<bales.size();i++){
            q.push(bales[i]);
        }
        while(!q.empty()){
            bale current=q.front();
            q.pop();
            for(int i=0; i<2; i++){
                int nx=current.x+dirx[i];
                int ny=current.y+diry[i];
                if(nx>=0&&nx<n&&ny>=0&&ny<n){
                    if(i==0&&grid[nx][ny]=='R'){
                        q.push(bale{current.id,nx,ny});
                        baleCounts[current.id]++;
                    }
                    else if(i==1&&grid[nx][ny]=='D'){
                        q.push(bale{current.id,nx,ny});
                        baleCounts[current.id]++;
                    }
                }
            }
        }
        cost=0;
        for(int i=0; i<n*2;i++){
            cost+=baleCosts[i]*baleCounts[i];
        }
    }
    cout<<cost;
}
