from pyMaze import maze, agent, COLOR, textLabel

def DFS(m, start=None, goal=None):
    
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
                
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
                
    fwdPath = {}
    cell = goal
    
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
        
    return dSearch, dfsPath, fwdPath


# ---------------- RUN ---------------- #
m=maze(15,20)
m.CreateMaze(loopPercent=10, theme='dark')

# Run DFS
dSearch, dfsPath, fwdPath = DFS(m)

# Agents for visualization:
# a → shows BFS search order
a = agent(m, footprints=True, color=COLOR.red, shape='square', filled=True)

# b → shows the final shortest path
b = agent(m, footprints=True, color=COLOR.light, shape='square', filled=False)

# c → shows parent links discovered during BFS
c = agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape='square',
              filled=True, goal=(m.rows, m.cols))

# Visual tracing of the paths
m.tracePath({a: dSearch}, delay=100)     # BFS exploration order
m.tracePath({c: dfsPath}, delay=100)     # BFS parent relations
m.tracePath({b: fwdPath}, delay=100)     # Final shortest path

textLabel(m,'DFS Path Length',len(fwdPath)+1)

m.run()