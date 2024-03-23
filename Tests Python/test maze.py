import sys
import math

w, h = [int(i) for i in input().split()]
maze = []
start = []
for i in range(h): #create list of each node dist and type and define starting node
    row = input()
    row_list = list(row)
    if 'S' in row_list:
        start = [row_list.index('S'), i]
    maze.append([{'dist': 0, 'type' : char} if char == 'S' else {'dist': math.inf, 'type' : char} for char in row_list])


queue = [start]
while queue: #type of BFS but instead of checking if visited we check if dist == math.inf (initial dist)
    current = queue.pop(0)
    x,y = current
    neighbor_check = 4
    for neighbor in range(neighbor_check):
        if maze[y][x-1]['type'] != '#' and maze[y][x-1]['dist'] == math.inf:
            queue.append([x-1, y])
            maze[y][x-1]['dist'] = maze[y][x]['dist'] + 1
        if x == w-1:
            if maze[y][0]['type'] != '#' and maze[y][0]['dist'] == math.inf:
                queue.append([0, y])
                maze[y][0]['dist'] = maze[y][x]['dist'] + 1
        else:
            if maze[y][x+1]['type'] != '#' and maze[y][x+1]['dist'] == math.inf:
                queue.append([x+1, y])
                maze[y][x+1]['dist'] = maze[y][x]['dist'] + 1
        if maze[y-1][x]['type'] != '#' and maze[y-1][x]['dist'] == math.inf:
            queue.append([x, y-1])
            maze[y-1][x]['dist'] = maze[y][x]['dist'] + 1
        if y == h-1:
            if maze[0][x]['type'] != '#' and maze[0][x]['dist'] == math.inf:
                queue.append([x, 0])
                maze[0][x]['dist'] = maze[y][x]['dist'] + 1
        else:
            if maze[y+1][x]['type'] != '#' and maze[y+1][x]['dist'] == math.inf:
                queue.append([x, y+1])
                maze[y+1][x]['dist'] = maze[y][x]['dist'] + 1
    print(maze, current, file=sys.stderr, flush=True)

alphabet = [i for i in range (10)] #define a list 0-9 A-Z
for i in range(65, 91): 
    alphabet.append(chr(i))

for j in range(h): #replace each dist >= 10 and print each row
    line = []
    for i in range(w):
        if maze[j][i]['dist'] != math.inf:
            if maze[j][i]['dist'] >= 10:
                line.append(alphabet[maze[j][i]['dist']])
            else:
                line.append(str(maze[j][i]['dist']))
        else:
            line.append(maze[j][i]['type'])
    print(''.join(line))
10 