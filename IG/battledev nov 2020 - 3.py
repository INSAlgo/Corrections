# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=70# (Exo 3)

n = int(input())

children = [[] for _ in range(n)]
for _ in range(n-1) :
    A, B = map(int, input().split())
    children[B].append(A)

pop = [0 for _ in range(10)]    # population des niveaux

def explore(node: int = 0, depth: int = 0) :
    # DFS récursif
    
    # On enregistre à quelle profondeur est le noeud actuel
    pop[depth] += 1
    
    # Récursion
    for child in children[node] :
        explore(child, depth+1)

# Appel initial
explore()

print(*pop)
