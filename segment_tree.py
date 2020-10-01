class SegmentTree:
    def __init__(self, arr):
        self._tree = 4*[None]*len(arr)
        self._arr = arr
        self._len = len(self._arr)
        self._build(0, 0, len(arr)-1)
    
    def _build(self, v, start, end):
        if start==end:
            self._tree[v]=self._arr[start]
        else:
            m=(start+end)//2
            l=self._build(v*2+1, start, m)
            r=self._build(v*2+2, m+1, end)
            self._tree[v]=l+r
        return self._tree[v]
    
    def _query(self, v, l, r, start, end):
        if r<start or l>end:
            return 0
        if l <= start and end <= r:
            return self._tree[v]
        m=(start+end)//2
        lsum = self._query(2*v+1, l, r, start, m)
        rsum = self._query(2*v+2, l, r, m+1, end)
        return lsum+rsum
    
    def _update(self, v, i, val, start, end):
        if start==end:
            d=val-self._tree[v]
            self._tree[v]=val
        else:
            m=(start+end)//2
            if i <= m:
                d=self._update(v*2+1, i, val, start, m)
            else:
                d=self._update(v*2+2, i, val, m+1, end)
            self._tree[v]+=d
        return d
    
    def query(self, l, r):
        return self._query(0, l, r, 0, self._len-1)
    
    def update(self, i, val):
        self._arr[i]=val
        self._update(0, i, val, 0, self._len-1)