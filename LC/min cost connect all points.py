# https://leetcode.com/problems/min-cost-to-connect-all-points/

# Partie implicite :

from typing import List
import heapq

# Partie à coder :

# Prim's version :

class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def distance(a,b):
            return abs(a[1]-b[1])+abs(a[0]-b[0])
        
        n=len(points)
        adj=[[] for _ in range(n+1)]
        
        for p in range(n):
            for u in range(p+1,n):
                dist=distance(points[u],points[p])
                adj[p].append((u,dist))
                adj[u].append((p,dist))
                
        nodesInTree = {0}

        availableEdges = []
        for edge in adj[0]:
            heapq.heappush(availableEdges,(edge[1],0,edge[0]))
        rep=0
        while(len(nodesInTree)<n):
            currentEdge=heapq.heappop(availableEdges)

            if currentEdge[2] not in nodesInTree:
                nodesInTree.add(currentEdge[2])
                rep+=currentEdge[0]
                for edge in adj[currentEdge[2]]:
                    if edge[0] not in nodesInTree:
                        heapq.heappush(availableEdges,(edge[1],currentEdge[2],edge[0]))
        return rep

# Kruskal version :
# (union find lib : https://github.com/INSAlgo/trainings-2018/blob/master/W14_feb4_feb10/unionfind.py)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        
        edges=[]
        
        for i in range(n-1):
            for j in range(i+1,n):
                edges.append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j))
        edges.sort(reverse=True)
        
        
        uf = UnionFind(range(n))
        rep = 0
        
        while edges:
            currentEdge = edges.pop()
            
            if not uf.is_same_set(currentEdge[2],currentEdge[1]):
                uf.union(currentEdge[2],currentEdge[1])
                rep+=currentEdge[0]
        return(rep)