# https://codeforces.com/contest/1765/problem/B

for _ in range(int(input())) :
    n = int(input())
    w = input()
    t = ""
    i = 0
    d = False
    while i < n :
        if not d :
            t += w[i]
        else :
            t += 2*w[i]
            i += 1
        i += 1
        d = 1 - d
    
    if t == w :
        print("YES")
    else :
        print("NO")