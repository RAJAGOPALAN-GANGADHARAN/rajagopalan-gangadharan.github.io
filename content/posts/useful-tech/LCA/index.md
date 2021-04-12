---
title: "LCA"
date: 2020-06-08 08:06:25 +0600
description: LCA explanation in layman terms
menu:
  sidebar:
    name: LCA
    identifier: lca
    parent: useful-tech
    weight: 10
---

## LCA Using Binary Lifting 

    k=0 means the parent node
    Create a table P[K][N] -> N is number of nodes 
    2^k<=N 
    So k<=logN 
    Hence Size of table is N*logN

    jumps are made in order of powers of 2 ->1,2,4...etc
    trying to divide by 2 

    let mid=par[i][k-1] (2^(k-1)th parent if exists)
    par[i][k] is par[mid][k-1] 

    Its basically dividing a big jump into 2.


    First make 2 nodes that we are going to find LCA to same depth using Walk function
    if current jump results -1 then we have jumped of the table.

    During LCA jump just close to LCA.
    Check if jumping makes them equal if not then make the jump.
    Do this until ur able to make a jump.

    Finally the answer would be an immediate parent of a node.


    Preprocessing is O(NlogN) and per query its O(logN)
    Space is O(NlogN)
    
  
{{<img src="https://rajagopalan-gangadharan.github.io/Error404/usefultech/LCA1.png" align="center" title="lca-explanation" width="500px" height="500px">}}

{{< vs >}}

{{<img src="https://rajagopalan-gangadharan.github.io/Error404/usefultech/LCA4.PNG" align="center" title="lca-explanation" width="500px" height="500px">}}

{{< vs >}}

{{<img src="https://rajagopalan-gangadharan.github.io/Error404/usefultech/LCA2.jpg" align="center" title="lca-explanation" width="500px" height="500px">}}

{{< vs >}}

{{<img src="https://rajagopalan-gangadharan.github.io/Error404/usefultech/LCA3.jpg" align="center" title="lca-explanation" width="500px" height="500px">}}

{{< vs >}}

### Do Bfs for depth wrt to any root node

```cpp
void bfs(vector& adj,vector& par,VII& depth,int& n)
    {
        //arbitrarily root the tree
        VII vis(n,false);
        depth[0]=0;
        vis[0]=true;
        queue q;
        q.push(0);
        while(!q.empty())
        {
            int u=q.front();
            q.pop();
            for(auto it:adj[u])
            if(!vis[it])
            {
                vis[it]=true;
                depth[it]=depth[u]+1;
                par[0][it]=u;
                q.push(it);
            }

        }
    }
```

### Preprocess

```cpp
void preprocess(vector<VII>& par,int& n,int& D)
{
    for(int d=0;d<=D;++d)
    {
        for(int i=0;i<n;++i)
        {

            int mid=par[d-1][i];
            if(mid!=-1)
            par[d][i]=par[d-1][mid];
        }
    }
}
```

### Walk and LCA

```cpp
int walk(int i,int k,int& D,vector<VII>& par)
{
    //To make a node i at depth d
    for(int d=0;d<=D && i!=-1;++d)
    if((1<<d)&k)i=par[d][i];

    return i;
}
int LCA(int a,int b,vector<VII>& par,VII& depth,int &D)
{
    if(depth[a]>depth[b])
    a=walk(a,depth[a]-depth[b],D,par);
    else if(depth[b]>depth[a])
    b=walk(b,depth[b]-depth[a],D,par);

    if(a==b)
    return a;

    for(int d=D;d>=0;--d)
    {
        //to go close faster make big jumps
        if(par[d][a]!=par[d][b])
        {
            a=par[d][a];
            b=par[d][b];
        }
    }
    return par[0][a];
}


int D=log2(n);
```