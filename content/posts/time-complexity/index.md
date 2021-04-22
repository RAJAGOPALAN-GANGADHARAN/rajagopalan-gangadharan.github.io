---
title: "Time Complexity Analysis"
date: 2020-06-08 08:06:25 +0600
description: How to analyze Time Complexity of algorithms
menu:
  sidebar:
    name: Time Complexity Analysis
    identifier: time-complexity
    weight: 10
---

### General TC

<img src="https://rajagopalan-gangadharan.github.io/Error404/time.png"></src>

### Harmonic Sum Analysis 

<blockquote>When a function goes in the form of</blockquote>

```cpp
for(int i=1;i<=n;++i)
{
    for(int j=2*i;j<=n;j+=i)
    cout<<(i,j);
}
```

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Csum_%7Bi%3D0%7D%5En%20%5Cfrac%7Bn%7D%7Bi%7D%20%5Cimplies%20n%2A%5Csum_%7Bi%3D0%7D%5En%20%5Cfrac%7B1%7D%7Bi%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0"></img>

The Summation part takes O(logN) hence the total time is O(N*logN)

<h5><b>Note: Find Why it is logN </b></h5>