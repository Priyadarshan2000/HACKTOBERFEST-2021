// 05 Partition Equal Subset Sum

/* Given an array arr[] of size N, check if it can be partitioned into
 two parts such that the sum of elements in both parts is the same.*/
 
 

#include <bits/stdc++.h>
using namespace std;



int equalPartition(int n, int a[])
    {

        int sum = 0;
    int i, j;

    for (i = 0; i < n; i++)
        sum += a[i];
 
    if (sum % 2 != 0)
        return false;
 
    bool part[sum / 2 + 1];

    for (i = 0; i <= sum / 2; i++) {
        part[i] = 0;
    }

 
    for (i = 0; i < n; i++) {
        for (j = sum / 2; j >= a[i];
             j--) { 
            if (part[j - a[i]] == 1 || j == a[i])
                part[j] = 1;
        }
    }
 
    return part[sum / 2];
    }




int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        int arr[N];
        for(int i = 0;i < N;i++)
            cin>>arr[i];
        
        if(equalPartition(N, arr))
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
    return 0;
}
