---
title: "Template Library"
date: 2020-06-08 08:06:25 +0600
description: cp templates
menu:
  sidebar:
    name: Template Library
    identifier: template-library
    weight: 10
---

## Fenwick Tree

```cpp
#include<bits/stdc++.h>
using namespace std;
template<typename T>
class FenwickTree
{
    vector<T> BIT;
    int n;
public:
    FenwickTree(int n,vector<T>& arr,T def)
    {
        BIT.assign(n + 1, def);
        this->n = n;
    }
    void update(int i,T v)
    {
        while (i <= n)
            BIT[i] += v, i += i & -i;
    }
    T query(int i,T def)
    {
        //get from 0 to i
        T sum = def;
        while(i>0)
            sum += BIT[i], i -= i & -i;
            
        return sum;
    }
};

class RangeFenwickTree
{
    int n;
    vector<int> BIT1;
    vector<int> BIT2;
    public:
    RangeFenwickTree(int n,vector<int>& arr)
    {
        this->n = n;
        BIT1.assign(n + 1, 0);
        BIT2.assign(n + 1, 0);
        for (int i = 1; i <= n;++i)
            update_range(i, i, arr[i]);
    }
    static void update(vector<int>& BIT,int i,int v,int n)
    {
        while(i<=n)
            BIT[i] += v, i += i & -i;
    }
    void update_range(int l,int r,int v)
    {
        update(BIT1, l, v, n);
        update(BIT1, r + 1, -v, n);
        update(BIT2, l, v * (l - 1), n);
        update(BIT2, r+1, -v * r, n);
    }
    static int sum(int r,vector<int>& BIT)
    {
        int sum = 0;
        while(r>0)
            sum += BIT[r], r -= r & -r;

        return sum;
    }
    int prefix_sum(int r)
    {
        return sum(r, BIT1) * r - sum(r, BIT2);
    }
    int range_sum(int l,int r)
    {
        return prefix_sum(r) - prefix_sum(l - 1);
    }
};


int main()
{
    //Test program
    int n;
    cin >> n;
    vector<int> arr(n + 1);
    for (int i = 1; i <= n;++i)
        cin >> arr[i];
    RangeFenwickTree tree(n,arr);
    int q;
    cin >> q;
    while(q--)
    {
        int type;
        cin >> type;
        if(type==1)
        {
            //range sum
            int l, r;
            cin >> l >> r;
            cout << "Ans:" << tree.range_sum(l, r) << endl;
        }
        else{
            //add to all elements
            int l, r, v;
            cin >> l >> r >> v;
            tree.update_range(l, r, v);
        }
    }
    return 0;
}
```

## Segment Trees

```cpp
template<typename T>
class SegmentTree
{
    int n;
    vector<T> seg;
public:
    SegmentTree(int n,vector<T>& arr):seg(2*n+1,0)
    {
        this->n=n;
        for(int i=0;i<n;++i)
            seg[i+n]=arr[i];

        for(int i=n-1;i>0;--i)
            seg[i]=seg[2*i]+seg[2*i+1];
    }
    void update(int i,T v)
    {
        i+=n;
        seg[i]+=v;
        while(i>1)
        {
            i/=2;
            seg[i]=seg[2*i]+seg[2*i+1];
        }
    }
    T query(int l,int r)
    {
        //l inclusive r excluded
        l+=n;
        r+=n;
        T sum=0;
        while(l<r)
        {
            if(l&1)
                sum+=seg[l],l++;
            if(r&1)
                r--,sum+=seg[r];
            l/=2;
            r/=2;
        }
        return sum;
    }

};
```

## LCA
```cpp
class LCA
{
    int n, q, D;
    vector<int> lev;
    vector<vector<int>> adj;
    vector<vector<int>> dp;
    public:
    LCA(int n,vector<vector<int>>& adj)
    {
        this->n = n;
        this->adj = adj;
        lev.assign(n + 1, 0);
        D = 31;
        dp.assign(n + 1, vector<int>(D + 1, 0));
    }
    int walk(int i, int k)
    {
        for (int d = 0; d <= D; ++d)
            if (k & (1 << d))
                i = dp[i][d];

        return i;
    }

    
    void dfs(int i, int l, int p)
    {
        if (p != -1)
            dp[i][0] = p;
        lev[i] = l;
        for (auto it : adj[i])
            if (it != p)
                dfs(it, l + 1, i);
    }
    void preprocess()
    {
        for (int d = 1; d <= D; ++d)
        {
            for (int i = 1; i <= n; ++i)
            {
                int mid = dp[i][d - 1];
                if (mid != 0)
                {
                    dp[i][d] = dp[mid][d - 1];
                }
            }
        }
    }
    int lca(int x, int y)
    {
        if (lev[x] > lev[y])
            x = walk(x, lev[x] - lev[y]);
        else if (lev[x] < lev[y])
            y = walk(y, lev[y] - lev[x]);
        if (x == y)
            return x;
        for (int d = D; d >= 0; --d)
        {
            if (dp[x][d] != dp[y][d])
            {
                x = dp[x][d];
                y = dp[y][d];
            }
        }

        return dp[x][0];
    }
    int dist(int x,int y)
    {
        //handle root cases differently
        return lev[x] + lev[y] - 2 * lev[lca(x, y)];
    }
};
```