# https://www.hackerrank.com/challenges/dijkstrashortreach/problem

import os

def shortestReach(n, edges, s):
    dists = [float('inf') for _ in range(n)]
    dists[s] = 0
    
    to_visit = set(range(n))
    visited = [False for _ in range(n)]
    
    while to_visit :
        cur = min(to_visit, key=lambda i: dists[i])
        
        if dists[cur] == float('inf') :
            break
        
        to_visit.discard(cur)
        visited[cur] = True
        
        for node, dist in edges[cur] :
            if visited[node] :
                continue
            
            dists[node] = min(dists[node], dists[cur] + dist)
        
    for i in range(n) :
        if dists[i] == float('inf') :
            dists[i] = -1
    
    dists.pop(s)
    
    return dists

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n, m = map(int, input().split())

        edges = {i: set() for i in range(n)}

        for _ in range(m):
            a, b, d = map(int, input().split())
            a, b = a-1, b-1
            edges[a].add((b, d))
            edges[b].add((a, d))

        s = int(input().strip()) - 1

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()