from pyMaze import maze, agent, COLOR

def DFS(m, start = None, goal = None):
    
    if start is None:
        start = (m.rows, m.cols)
        
    if goal is None:
        goal = (1,1)
        
    explored = [start]
    frontier = [start]
    dfsPath = {}
    dSearch = []
    
    while len(frontier) > 0:
        currCell = frontier.pop()
        dSearch.append(currCell)
        
        if currCell == goal:
            break
        
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                    
                if childCell in explored:
                    continue
                
                if childCell not in explored:    
                    explored.append(childCell)
                    frontier.append(childCell)
                    dfsPath[childCell] = currCell
                
    fwdPath = {}
    cell = goal
    
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
        
        
    return dSearch, dfsPath, fwdPath
        
                
            

m = maze(5, 5)
m.CreateMaze()

start = (5,5)
goal = (1,1)

dSearch, dfsPath, fwdPath = DFS(m, start, goal)

a = agent(m,5,5, goal = goal, footprints = True, shape = 'square', color = COLOR.green)
b = agent(m,1,1, goal = start, footprints = True, filled = True)
c = agent(m,5,5, goal = goal, footprints = True, color = COLOR.yellow)


m.tracePath({a:dSearch}, showMarked = True)
m.tracePath({b:dfsPath})
m.tracePath({c:fwdPath})

print(m.maze_map)

m.run()