---
title: "Trees"
date: 2020-06-08 08:06:25 +0600
description: trees datastructure
menu:
  sidebar:
    name: Trees
    identifier: trees
    parent: useful-datastructures
    weight: 10
---

## Some Facts about trees 

+ Simple path is a path that doesn't contain any node twice. A tree has n-1 edges!

## Segment Trees

Use segment trees for questions on updating values and querying.
Can be used with complex operations like pairs,sets etc.
Find very effecient and faster updating (used to insert too),
by Finding path to root from one node.

```cpp
void update(int pos,int val){
    pos += k;
    tree[pos] = val;
    int odd = 1;
    //this switches between alternate levels of the segment tree goes upwards
    while(pos>>=1 >0){
        /*
        use this in case for level switching
        if(odd) tree[pos] = tree[2*pos] | tree[2*pos+1];
        else tree[pos] = tree[2*pos] ^ tree[2*pos+1];
        odd = 1-odd;
        */
        tree[pos]=tree[2*pos]+tree[2*pos+1];
    }
}
for(int i=0;i<n;i++){
        int val;
        cin>>val;
        update(i,val);
}
```