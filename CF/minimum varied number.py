# https://codeforces.com/contest/1714/problem/C

for _ in range(int(input())) :

    s = int(input())
    sum_ = 0
    nb = ""
    for i in range(9, 0, -1) :
        if sum_ + i >= s :
            nb = str(s - sum_) + nb
            break
        
        else :
            sum_ += i
            nb = str(i) + nb
    
    print(nb)