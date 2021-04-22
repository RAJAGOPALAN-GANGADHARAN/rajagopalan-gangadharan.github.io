---
title: "Math facts"
date: 2020-06-08 08:06:25 +0600
description: Some awesome facts related to math
menu:
  sidebar:
    name: Math Tricks
    identifier: maths
    weight: 10
---

### Segmented Sieve
<p>Use When we have to generate large number of prime Numbers <a href="https://www.geeksforgeeks.org/segmented-sieve/">Click Here</a></p>
<hr/>

### BitHacks
Number of bits required to represent a number: <img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Clfloor%20%7B%5Clog_2%7Bn%7D%7D%20%5Crfloor%20%2B%201&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0"></img>

<div>For More Bit Tricks:<a href="http://graphics.stanford.edu/~seander/bithacks.html">Click Here</a></div>
<hr/>

### Useful nCr Technique 
Divide by their GCD's to prevent overflow

For fast Calculation:
```cpp
ll NcR(ll n, ll r) 
{  
    ll p = 1, k = 1;  
    if (n - r < r) 
        r = n - r; 

    if (r != 0) { 
        while (r) { 
            p *= n; 
            k *= r; 
            ll m = __gcd(p, k); 
            p /= m; 
            k /= m; 
            n--; 
            r--; 
        } 
    } 

    else
        p = 1; 

    return p;
} 
```

<hr/>

### Cool Geometry Properties

+ Find Area of triangle using Side length Heron's Formula.

<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5CDelta%20%3D%20%20%5Csqrt%7BP%2A%28P-A%29%2A%28P-B%29%2A%28P-C%29%7D%3B%0AP%20%3D%20%20%5Cfrac%7BA%2BB%2BC%7D%7B2%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0"></img>

<hr/>

###  Cool Mod properties 

```cpp
(a+b) % m = (a % m+b % m) % m
(a-b) % m = (a % m−b % m) % m
(a*b) % m = (a % m*b % m) % m
```

<hr/>

### Comparing Double values

```cpp
if(abs(a-b)<1e-9)
{
	cout<<"a and b are equal";
}
```

<hr/>

### GCD Properties

+ gcd(a,b)=gcd(a,b%a) Let X=gcd(a,b) then gcd(X/a,X/b)=1

</hr>

###  Find divisors of a number 

```cpp
for (int i = 2; i * 1ll * i <= x; ++i) {
    if (x % i == 0) {
        dd.push_back(i);
        if (i != x / i) {
            dd.push_back(x / i);
        }
    }
}
```

<hr/>

### Goldbachs Conjecture

+  It says any number can be expressed as a sum of 2 prime numbers.

<hr/>

###  Cool Problems

+ <p> When asked how to make two numbers equal by series of divisions
      Represent those numbers in terms of powers of those numbers.

                for eg allowed operations are /2,/3,/5 then
                A=x*2^a * 3^b * 5^c
                B=y*2^a2 * 3^b2 * 5^c2
                if x is same as y it can be made equal</p>
   <hr/>