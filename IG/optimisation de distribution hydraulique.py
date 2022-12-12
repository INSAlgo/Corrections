# https://www.isograd-testingservices.com//FR/solutions-challenges-de-code?cts_id=86#

# Exercice 4

N = int(input())

class Node:

    def __init__(self, num, quant, f1 = None, pert1 = None, f2 = None, pert2 = None) -> None:
        self.num = num
        self.quant = quant
        self.f1 = f1
        self.pert1 = pert1
        self.f2 = f2
        self.pert2 = pert2

dico = {}
for i in range(N+1):
    new = Node(*list(map(int, input().split())))
    dico[new.num] = new

def recur(node):
    if node.f1 is None:
        return (node.quant, 0)
    quant1, max1 = recur(dico[node.f1])
    quant2, max2 = recur(dico[node.f2])
    quant = node.quant + quant1 + quant2
    maxi = max(quant1 * node.pert1, quant2 * node.pert2, max1, max2) 
    return (quant, maxi)

ori = dico[0]
print(recur(ori)[1])
