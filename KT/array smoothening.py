# https://open.kattis.com/problems/arraysmoothening

N, K = map(int, input().split())
A = list(map(int, input().split()))

values = list(set(A))

counter = {a: 0 for a in values}

for a in A :
    counter[a] += 1

qtty = list(counter.values())
qtty.sort()

transpose = [0 for _ in range(qtty[-1])]
transpose[-1] = qtty.count(qtty[-1])

i = len(qtty) - 1
c = 0
t = qtty[-1] - 2

while i >= 0 and t >= 0 :
    if qtty[i] > t :
        c += 1
        i -= 1
    
    else :
        transpose[t] = c + transpose[t+1]
        t -= 1

if i < 0 :
    for j in range(t, -1, -1) :
        transpose[j] = c + transpose[j+1]

for j in range(len(transpose)-1, -1, -1) :
    if K < transpose[j] :
        print(j + 1)
        break

else :
    print(0)
