# https://codeforces.com/contest/1714/problem/B

for _ in range(int(input())) :
    n = int(input())
    A = list(map(int, input().split()))

    found = set()

    for i in range(n-1, -1, -1) :
        if A[i] in found :
            print(i+1)
            break
        found.add(A[i])
    else :
        print(0)