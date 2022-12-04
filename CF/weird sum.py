# https://codeforces.com/contest/1648/problem/A

n, m = map(int, input().split())

C: dict[int, list[list[int]]] = {}
for r in range(n) :
    line = list(map(int, input().split()))
    for c in range(m) :
        color = line[c]
        if color not in C :
            C[color] = [[], []]
        C[color][0].append(r)
        C[color][1].append(c)

s = 0

for coords in C.values() :
    l = len(coords[0])
    # We treat the X and Y coordinates of each color completely separately from each other
    for vals in coords :
        # Here is an efficient way to compute sum(sum(abs(A[i]-A[j]) for i in range(l)) for j in range(i+1, l)) in O(nln(n)) :
        vals.sort()
        cum_vals = [0]  # Cumulative sum of vals
        for i in range(l) :
            cum_vals.append(cum_vals[-1] + vals[i])
        
        # The magic happens here :
        for i in range(l) :
            s += vals[i] * i - cum_vals[i]

print(s)