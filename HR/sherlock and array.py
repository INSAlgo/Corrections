# https://www.hackerrank.com/challenges/sherlock-and-array/problem

import os

def balancedSums(arr):
    somme_droite=sum(arr)-arr[0]
    somme_gauche=0
    print(0,somme_gauche,somme_droite)
    if(somme_droite==somme_gauche):
            return("YES")
    else:
        for i in range(1,len(arr)):
            somme_gauche+=arr[i-1]
            somme_droite-=arr[i]
            print(i,somme_gauche,somme_droite)
            if(somme_droite==somme_gauche):
                return("YES")
                break
        else:
            return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()