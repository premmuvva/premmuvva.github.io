#include<stack>
#include<iostream>
#include <bits/stdc++.h>
#include<vector>
using namespace std;
#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for(int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
int count (int a,int b,int c){
    int d=a*c+b;
    if (d<10)
    return a;
    if(c*a+b%9<10||(c*a)%9+b<10)
    return a+1;
    {
        c=0;
        while(d>0){
            c+=d%10;
            d/=10;
        }
        if(c<10)
        return a+1;
        while(c>0){
            d+=c%10;
            c/=10;
        }
        if (d<10)
        return a+2;
        return a+3;
    }
    
}
int main(){
    int t,n,d;
    int arr[9][9][2]={//9   1    2      3     4     5     6     7     8
                    {{9,0},{1,1},{1,5},{3,1},{1,7},{1,2},{3,2},{1,4},{1,8}},//9
                    {{1,0},{1,0},{1,0},{1,0},{1,0},{1,0},{1,0},{1,0},{1,0}},//1
                    {{2,0},{1,8},{1,4},{2,0},{1,2},{1,7},{2,0},{1,5},{1,1}},//2
                    {{3,0},{1,7},{1,8},{3,0},{1,4},{1,5},{3,0},{1,1},{1,2}},//3
                    {{4,0},{1,6},{1,3},{1,2},{1,6},{1,3},{1,1},{1,6},{1,3}},//4
                    {{5,0},{1,5},{1,7},{2,2},{1,8},{1,1},{2,1},{1,2},{1,4}},//5
                    {{6,0},{1,4},{1,2},{3,2},{1,1},{1,8},{3,1},{1,7},{1,5}},//6
                    {{7,0},{1,3},{1,6},{1,1},{1,3},{1,6},{1,2},{1,3},{1,6}},//7
                    {{8,0},{1,2},{1,1},{2,1},{1,5},{1,4},{2,2},{1,8},{1,7}},//8
                    };
    in t;
    f(i,t){
        in n>>d;
        pr arr[n%9][d%9][0]<<" "<<count(arr[n%9][d%9][1],n,d)<<endl;
    }
    return 0;
}