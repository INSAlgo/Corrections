# https://codeforces.com/contest/1714/problem/E

res = []
for _ in range(int(input())) :
    n = int(input())
    A = list(map(int, input().split()))

    Ld = [a%10 for a in A]  # List of Last digits

    # Case : there are numbers ending in 0 and/or 5.
    # Numbers ending in 0 cannot be changed
    # Numbers ending in 5 can only be made into the next multiple of 10
    if (5 in Ld or 0 in Ld) :
        # Pushing every number ending in 5 to the next multiple of 10
        # They are now ending in 0 and cannot be changed anymore
        for i in range(n) :
            if Ld[i] == 5 :
                A[i] += 5
        # If all numbers are the same :
        if len(set(A)) == 1 :
            res.append("YES")
        else :
            res.append("NO")
        continue

    # Pushing every number to the closest number ending in 8 (by repeating the operation x += x%10)
    for i in range(n) :
        while A[i]%10 != 8 :
            A[i] += A[i]%10
    
    # Now, the only way to go from one number ending in 8 to the next is to add 20
    # because repeating the operation 4 times makes : 
    # X8 -> (X+1)6 -> (X+2)2 -> (X+2)4 -> (X+2)8
    for i in range(n-1) :
        if (A[i]-A[i+1])%20 != 0 :
            res.append("NO")
            break
    else :
        res.append("YES")

print(*res, sep='\n')