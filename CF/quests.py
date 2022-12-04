# https://codeforces.com/contest/1760/problem/F

for _ in range(int(input())) :
    n, c, d = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    A += [0] * max(0, d-n)
    s = 0
    S = [s := s + A[i] for i in range(max(n, d))] + [0]
    # 0 is for a S[-1] that can happen
    # when d%(k+1)-1 is round at line 20 (no rest)

    if A[0] * d < c :
        print("Impossible")
        continue

    if S[d-1] >= c :
        print("Infinity")
        continue

    for k in range(d-2, -1, -1) :
        if S[k] * (d//(k+1)) + S[d%(k+1)-1] >= c :
            print(k)
            break