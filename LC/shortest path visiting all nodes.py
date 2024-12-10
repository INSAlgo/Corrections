# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        visited = set()

        q = [(i, 1 << i) for i in range(n)]
        nb_steps = 0

        while True:
            next_q = []
            for current, mask in q:
                if mask == (1 << n) - 1:
                    return nb_steps

                for neighbour in graph[current]:
                    next_node = (neighbour, mask | 1 << neighbour)
                    if next_node not in visited:
                        next_q.append(next_node)
                        visited.add(next_node)

            q = next_q
            nb_steps += 1
