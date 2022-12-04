# https://www.hackerrank.com/challenges/flatland-space-stations/problem

import os

def flatlandSpaceStations(n, c):
    c.sort()
    maxi=c[0]
    
    for i in range(len(c)-1):
        maxi = max(maxi,int((c[i+1]-c[i])/2))
    maxi = max(maxi,n-1-c[-1])
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()