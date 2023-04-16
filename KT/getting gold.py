# https://open.kattis.com/problems/gold

W, H = map(int, input().split())

grid = []

for y in range(H) :
    line = input()
    grid.append(line)

    x = line.find('P')
    if x > -1 :
        P = (x, y)

def has_risk(x, y) :
    for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)} :
        nx, ny = x+dx, y+dy
        if 0 <= nx < W and 0 <= ny < H :
            if grid[ny][nx] == 'T' :
                return True
    return False

fifo = [P]
res = 0
visited = [[P==(x,y) for x in range(W)] for y in range(H)]

while fifo :
    x, y = fifo.pop()

    if grid[y][x] == 'G' :
        res += 1
    
    # print(x, y)
    # print(res)

    if has_risk(x, y) :
        continue

    for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)} :
        nx, ny = x+dx, y+dy
        if 0 <= nx < W and 0 <= ny < H :
            if visited[ny][nx] or grid[ny][nx] == '#' :
                continue

            fifo.append((nx, ny))
            visited[ny][nx] = True

print(res)