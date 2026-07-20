//
// Created by Kotake on 2021/9/7.
//

#include <iostream>
#include <vector>
using namespace std;
int main(){
    int count=1;
    int M,N;cin>> M >> N;
    vector<vector<int>> map;
    for(int i=0;i<M;i++){
        vector<int> a;
        for(int j=0;j<N;j++){
            char i;
            cin >> i;
            if(i=='M')a.push_back(0);
            else a.push_back(1);
        }
        map.push_back(a);
    }
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            if(map[i][j]==0)continue;
            pair<int,int> left,right,up,down;
            pair<int,int> ul,ur,dl,dr;
            left.second = j==0?j:j-1;
            right.second = j==N-1?j:j+1;
            left.first=i;right.first=i;
            up.first=i==0?i:i-1;
            down.first=i==M-1?i:i+1;
            up.second=j;down.second=j;
            ul.second=j==0?j:j-1;
            dl.second=j==0?j:j-1;
            ul.first=i==0?i:i-1;
            dl.first=i==M-1?i:i+1;
            ur.second=j==N-1?j:j+1;
            dr.second=j==N-1?j:j+1;
            ur.first=i==0?i:i-1;
            dr.first=i==M-1?i:i+1;
            int Max = max(map[left.first][left.second],
                          max(map[right.first][right.second],
                              max(map[up.first][up.second],
                                  max(map[down.first][down.second],
                                      max(map[ul.first][ul.second],
                                          max(map[ur.first][ur.second],
                                              max(map[dl.first][dl.second],
                                                  map[dr.first][dr.second])))))));
            int Min = min(map[left.first][left.second],
                          min(map[right.first][right.second],
                              min(map[up.first][up.second],
                                  min(map[down.first][down.second],
                                      min(map[ul.first][ul.second],
                                          min(map[ur.first][ur.second],
                                              min(map[dl.first][dl.second],
                                                  map[dr.first][dr.second])))))));

            if(Max>1)map[i][j]=Max;
            else if(Max<=1)map[i][j]=++count;
        }
    }

//    for(int i=0;i<M;i++)
//    {
//        for(int j=0;j<N;j++){
//            cout << map[i][j] << ' ' ;
//        }
//        cout << endl;
//    }
//    cout << "------------"<<endl;
    for(int i=M-1;i>=0;i--){
        for(int j=N-1;j>=0;j--){
            if(map[i][j]==0)continue;
            pair<int,int> left,right,up,down;
            pair<int,int> ul,ur,dl,dr;
            left.second = j==0?j:j-1;
            right.second = j==N-1?j:j+1;
            left.first=i;right.first=i;
            up.first=i==0?i:i-1;
            down.first=i==M-1?i:i+1;
            up.second=j;down.second=j;
            ul.second=j==0?j:j-1;
            dl.second=j==0?j:j-1;
            ul.first=i==0?i:i-1;
            dl.first=i==M-1?i:i+1;
            ur.second=j==N-1?j:j+1;
            dr.second=j==N-1?j:j+1;
            ur.first=i==0?i:i-1;
            dr.first=i==M-1?i:i+1;
            int Max = max(map[left.first][left.second],
                          max(map[right.first][right.second],
                              max(map[up.first][up.second],
                                  max(map[down.first][down.second],
                                      max(map[ul.first][ul.second],
                                          max(map[ur.first][ur.second],
                                              max(map[dl.first][dl.second],
                                                  map[dr.first][dr.second])))))));
            int Min = min(map[left.first][left.second],
                          min(map[right.first][right.second],
                              min(map[up.first][up.second],
                                  min(map[down.first][down.second],
                                      min(map[ul.first][ul.second],
                                          min(map[ur.first][ur.second],
                                              min(map[dl.first][dl.second],
                                                  map[dr.first][dr.second])))))));

            if(Min==0 && Max==0)continue;
            else if(Min==0 && Max!=0)map[i][j]=Max;
        }
    }

//    for(int i=0;i<M;i++)
//    {
//        for(int j=0;j<N;j++){
//            cout << map[i][j] << ' ' ;
//        }
//        cout << endl;
//    }
//    cout << "------------"<<endl;
    int MM[99999]={0};
    int c=0;
    for(int i=0;i<M;i++)
        for(int j=0;j<N;j++) {
            if(MM[map[i][j]]!=1 && map[i][j]>=1)
                c++;
            MM[map[i][j]] = 1;
        }

    cout << c;
    return 0;
}