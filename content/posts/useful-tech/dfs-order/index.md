---
title: "DFS Order"
date: 2020-06-08 08:06:25 +0600
description: Pre and post ordering in DFS explanation in layman terms
menu:
  sidebar:
    name: DFS - Ordering
    identifier: dfs-order
    parent: useful-tech
    weight: 10
---

A very useful technique.It basically has 2 arrays
one is Intime and the other is outTime. inTime says when it enters a recursion stack and outTime says 
when it exits the recursion stack.
It is useful to check if a node v is present in the subtree of node u. If inTime\[u]<inTime\[v] and 
outTime\[u]> outTime\[v].

It can also be useful in counting number of nodes that belong to a particular tree at a particular height.

```cpp
void dfs(int u,int par,int level){
    startTime[u]=++tim; 
    for(int v: g[u]){
        if(v!=par){
            dfs(v,u,level+1);
        }
    }
    endTime[u]=tim;
}
int count()
{
    //number of nodes at cur level that is descendent of pth par is counted.
    int ans=(upper_bound(all(lvl[cur]),endTime[pthpar])-lower_bound(all(lvl[cur]),startTime[pthpar]));
}
```
