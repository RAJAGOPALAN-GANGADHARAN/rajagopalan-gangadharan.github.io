---
title: "SCC"
date: 2020-06-08 08:06:25 +0600
description: Kosaraju's SCC explanation in layman terms
menu:
  sidebar:
    name: SCC
    identifier: scc
    parent: useful-tech
    weight: 10
---

### Kosaraju's SCC

A strongly Connected Component is for a directed graph. For an undirected graph we say it is a connected 
Component if we can reach a vertex from any vertex of a connected component. In case of SCC its same but called differently.

<img src="https://rajagopalan-gangadharan.github.io/Error404/usefultech/SCC.png"/>

### Steps

+ Perform DFS in forward graph and make a note of nodes in decreasing order of outtime.
+ Perform DFS in reverse graph(instead of for loop use the decreasing order u found).
+ Everything reachable in a component (during second DFS) falls inside an SCC.
+ Time Complexity is O(V+E)

```cpp
int sz = 200005;
vector<VII> adj(sz),rev(sz);
vector<bool> vis(sz,false);
vector<VII> SCC(sz);
int comp = 0;
VII topo;
void dfs_forward(int u)
{
  for(auto it:adj[u])
  {
      if(!vis[it])
      {
          vis[it] = true;
          dfs_forward(it);
      }
  }
  topo.pb(u);
}

void dfs_backward(int u)
{
  SCC[comp].pb(u);
  for(auto it:rev[u])
  {
      if(!vis[it])
      {
          vis[it] = true;
          dfs_backward(it);
      }
  }
}
main()
{
int n,m;
  cin >> n>>m;
  for (int i = 1; i <= m; ++i)
  {
      int x, y;
      cin >> x >> y;
      adj[x].pb(y);
      rev[y].pb(x);
  }
  for (int i = 1; i <= n;++i)
  {
      if(!vis[i])
      {
          vis[i] = 1;
          dfs_forward(i);
      }
  }
  reverse(all(topo));
  vis.assign(sz, false);

  for(auto x:topo)
  {
      if(!vis[x])
      {
          vis[x] = true;
          comp++;
          dfs_backward(x);
      }
  }

  for (int i = 1; i <= comp;++i)
  {
      for(auto sc:SCC[i])
          cout << sc << ' ';

      cout << '\n';
  }
}
```
