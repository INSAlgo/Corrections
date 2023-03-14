# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# Partie implicite :

from typing import List

# Partie à coder :

# BFS borné :

from queue import Queue

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = {i: set() for i in range(n)}
        for a, b, d in flights :
            edges[a].add((b, d))

        prices = [-1 for _ in range(n)]
        prices[src] = 0

        stops = 0
        q = Queue()
        q.put(src)

        while q and stops <= k :

            new_prices = prices.copy()

            for _ in range(q.qsize()) :
                cur = q.get()

                for node, price in edges[cur] :
                    new_price = prices[cur] + price
                    if new_prices[node] == -1 or new_prices[node] > new_price :
                        new_prices[node] = new_price
                        q.put(node)

                            
            prices = new_prices
            stops += 1
        
        return prices[dst]

# Dijkstra avec une dimension supplémentaire :

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = {i: {} for i in range(n)}
        for a, b, d in flights :
            edges[a][b] = d

        prices = [{s: float('inf') for s in range(-1, k+1)} for _ in range(n)]
        prices[src][-1] = 0

        to_visit = {(i, s) for i in range(n) for s in range(-1, k+1)}
        visited = [{s: False for s in range(-1, k+1)} for _ in range(n)]

        cur_node = src
        cur_stops = -1

        while True :
            tot_price = prices[cur_node][cur_stops]

            if tot_price == float('inf') :
                return -1
            
            if cur_node == dst :
                return prices[dst][cur_stops]
            
            visited[cur_node][cur_stops] = True
            to_visit.discard((cur_node, cur_stops))

            if cur_stops < k :
                for next_node, price in edges[cur_node].items() :
                    if visited[next_node][cur_stops+1] :
                        continue
                    prices[next_node][cur_stops+1] = min(prices[next_node][cur_stops+1], tot_price + price)
            
            cur_node, cur_stops = min(to_visit, key=lambda t: prices[t[0]][t[1]])