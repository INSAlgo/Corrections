# https://www.codingame.com/ide/puzzle/winamax-battle

from collections import deque

def replace_cards_numbers(card):
    return card.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "B").replace("10", "A")[0]

n = int(input())
p1 = deque()
for i in range(n):
    p1.append(replace_cards_numbers(input()))

m = int(input())
p2 = deque()
for i in range(m):
    p2.append(replace_cards_numbers(input()))

result = None
count = 0
while result is None:
    c1 = [p1.popleft()]
    c2 = [p2.popleft()]

    while c1[-1] == c2[-1]:
        if len(p1) < 4 or len(p2) < 4:
            result = "PAT"
            break
        
        for _ in range(4):
            c1.append(p1.popleft())
            c2.append(p2.popleft())
    
    if c1[-1] > c2[-1]:
        p1.extend(c1)
        p1.extend(c2)
    else:
        p2.extend(c1)
        p2.extend(c2)

    if len(p1) == 0:
        result = 2
    elif len(p2) == 0:
        result = 1

    count += 1

if result == "PAT":
    print(result)
else:
    print(result, count)
