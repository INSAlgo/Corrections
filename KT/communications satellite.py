# https://open.kattis.com/problems/communicationssatellite

from queue import PriorityQueue

class UnionFind:

    def __init__(self, singletons):
        self.parents = {e: e for e in singletons}
        self.rank = {e: 0 for e in singletons}

    def find(self, e):
        if e not in self.parents:
            return None
        if self.parents[e] != e:
            self.parents[e] = self.find(self.parents[e])
        return self.parents[e]

    def union(self, e1, e2):
        r1, r2 = self.find(e1), self.find(e2)
        if r1 == r2:
            return
        if self.rank[r1] < self.rank[r2]:
            r1, r2 = r2, r1
    
        self.parents[r2] = r1
        if self.rank[r1] == self.rank[r2]:
            self.rank[r1] += 1

    def is_same_set(self, e1, e2):
        return (self.find(e1) == self.find(e2))

N = int(input())
edges = PriorityQueue()
uf = UnionFind(range(N))

prbls = []

for i in range(N) :
    xi, yi, ri = map(int, input().split())
    prbls.append((xi, yi, ri))
    
    for j in range(i) :
        xj, yj, rj = prbls[j]
        
        d = ((xi-xj)**2 + (yi-yj)**2)**0.5 - ri - rj

        edges.put((d, i, j))

k = 1
res = 0

while k < N and not edges.empty() :
    d, i, j = edges.get()
    
    if uf.is_same_set(i, j) :
        continue
    
    uf.union(i, j)
    res += d
    k += 1

print(res)