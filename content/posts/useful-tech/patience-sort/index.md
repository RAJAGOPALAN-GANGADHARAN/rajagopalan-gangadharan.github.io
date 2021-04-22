---
title: "Patience Sort"
date: 2020-06-08 08:06:25 +0600
description: Patience sort explanation in layman terms
menu:
  sidebar:
    name: Patience Sort
    identifier: patience-sort
    parent: useful-tech
    weight: 10
---

It is an online sorting algorithm aimed to create piles of cards in such a way that piles are in increasing order down wards.

It can be used to find LIS in O(NlogN) time. Can also be used to find (minimum)number of distinct LIS.

<img src="https://rajagopalan-gangadharan.github.io/Error404/usefultech/PS1.PNG"/>

```cpp
VII dp;
for(int i=arr.size()-1;i>=0;--i)
{
    int x=arr[i];
    auto it=upper_bound(all(dp),x);
    if(it==dp.end())
    dp.pb(x);
    else *it=x;
}
cout<<dp.size();
```

