# https://www.hackerrank.com/challenges/poisonous-plants/problem

def poisonousPlants(p):
    day_it_fucking_dies = [0] * len(p)
    
    for i in range(1, len(p)):
        j = i - 1
        day = 0
        while day_it_fucking_dies[j] != 0 and p[i] <= p[j]:
            day = max(day, day_it_fucking_dies[j])
            j -= day_it_fucking_dies[j]
        
        if p[i] > p[j]:
            day_it_fucking_dies[i] = day + 1
    
    return max(day_it_fucking_dies)
