#include <bits/stdc++.h>
using namespace std;


//creating local elemenst just to perform
int tim=0;
int u[N], v[N], vis[N];
int travin[N], tout[N], isBridge[M], ancestorleast[N];
vector<pair<int, int> > g[N]; //vertex, index of edge

void dfs(int k, int par)
{
	vis[k]=1;
	travin[k]=++tim;
	ancestorleast[k]=travin[k];
	for(auto it:g[k])
	{
		if(it.first==par)
			continue;
		if(vis[it.first])
		{	
			ancestorleast[k]=min(ancestorleast[k], travin[it.first]);
			continue;
		}
		dfs(it.first, k);
		ancestorleast[k]=min(ancestorleast[k], ancestorleast[it.first]);
		if(ancestorleast[it.first]>travin[k])
			isBridge[it.second]=1;
	}
	tout[k]=tim;
}
