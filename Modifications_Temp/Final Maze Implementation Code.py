from pyMaze import maze, agent, textLabel, COLOR
from queue import PriorityQueue


# A* is an intelligent search algorithm.
# It always chooses the path with the lowest estimated total cost based on:
# f(n) = g(n) + h(n)
# g(n): actual cost from the start node to current node n
# h(n): estimated cost from node n to the goal (heuristic)
#
# A* uses a priority queue:
# - It pushes the lowest f(n) to the front
# - If costs tie: it uses lowest h(n)
# - If still tied: it may choose any cell

def h(cell1, cell2): #~~~~~cell1 the cell passed & cell2 is the goal cell whic is (1,1)?
    # Manhattan Distance Heuristic
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2) ###explain


def aStar(m):
    # Start position is the bottom-right cell
    start = (m.rows, m.cols)

    # g(n): actual movement cost
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0

    # f(n): total estimated cost (g + h)
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, (1, 1)) #~~~~~~~~~~~~~~~~~(1,1) means the goal is always in cell (1,1)

    # Priority Queue → always returns the smallest f(n)
    open = PriorityQueue()
    open.put((f_score[start], h(start, (1, 1)), start))

    aPath = {}         # Stores parent links
    searchPath = []    # Stores the search exploration order

    while not open.empty():
        currCell = open.get()[2]
        searchPath.append(currCell)

        # GOAL reached
        if currCell == (1, 1):
            break

        # Explore neighbors (East, South, North, West)
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                # Update cost values
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, (1, 1))

                # If a better path is found → update
                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, h(childCell, (1, 1)), childCell))
                    aPath[childCell] = currCell

    # Build Forward Path (final shortest path)
    fwdPath = {}
    cell = (1, 1)

    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return searchPath, aPath, fwdPath


# ------------ GUI With Documentation ------------- #

m = maze(15, 20)

# Any maze consists of a matrix:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
#
# rows = height
# cols = width

m.CreateMaze(loadMaze='maze--2025-12-23--20-00-35.csv')
# loopPercent = number of loops (0 = purely perfect maze)
# theme = background color style
# loadMaze = load maze shape from CSV (if you saved one)
# pattern='h' → horizontal bias


# Run A*
searchPath, aPath, fwdPath = aStar(m)

# Visualization agents:
a = agent(m, footprints=True, color=COLOR.blue, filled=True)      # Search path
b = agent(m, 1, 1, footprints=True, color=COLOR.yellow, filled=True,
          goal=(m.rows, m.cols))                                  # Parent path
c = agent(m, footprints=True, color=COLOR.red)                    # Final path


# Visual tracing
m.tracePath({a: searchPath}, delay=100)
m.tracePath({b: aPath}, delay=100)
m.tracePath({c: fwdPath}, delay=100)

textLabel(m, 'A Star Path Length', len(fwdPath) + 1)
textLabel(m, 'A Star Search Length', len(searchPath))

m.run()


#####################################################################################################


from pyMaze import maze, agent, textLabel, COLOR
from collections import deque

def BFS(m, start=None):
    # If no start cell is given, begin from the bottom-right corner (default in pyMaze)
    if start is None:
        start = (m.rows, m.cols)

    frontier = deque()      # BFS queue
    frontier.append(start)

    bfsPath = {}            # Stores child -> parent mapping
    explored = [start]      # List of visited cells
    bSearch = []            # List Order in which cells are explored

    # ------------------ BFS MAIN LOOP ------------------
    while len(frontier) > 0:
        currCell = frontier.popleft()

        # Stop if the goal is reached
        if currCell == m._goal:
            break

        # Explore all four directions: East, South, North, West
        for d in 'ESNW':
            # Check if movement in this direction is allowed in the maze map
            if m.maze_map[currCell][d] == True:

                # Determine the next cell based on direction
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])

                # Skip if this cell was visited before
                if childCell in explored:
                    continue

                frontier.append(childCell)        # Add to BFS queue
                explored.append(childCell)        # Mark as visited
                bfsPath[childCell] = currCell     # Store parent
                bSearch.append(childCell)         # Keep search order

    # ------------------ BUILD SHORTEST PATH ------------------
    # fwdPath will store the final shortest path from start → goal
    fwdPath = {}
    cell = m._goal

    # Trace back from goal to start using parent links
    while cell != (m.rows, m.cols):
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]

    return bSearch, bfsPath, fwdPath


# ===========================================================
#                    MAIN EXECUTION & VISUALIZATION
# ===========================================================


m=maze(15,20)
m.CreateMaze(loadMaze='maze--2025-12-23--20-00-35.csv')

# Run BFS
bSearch, bfsPath, fwdPath = BFS(m)

# Agents for visualization:
# a → shows BFS search order
a = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=True)

# b → shows the final shortest path
b = agent(m, footprints=True, color=COLOR.red, shape='square', filled=False)

# c → shows parent links discovered during BFS
c = agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape='square',
              filled=True, goal=(m.rows, m.cols))

# Visual tracing of the paths
m.tracePath({a: bSearch}, delay=100)     # BFS exploration order
m.tracePath({c: bfsPath}, delay=100)     # BFS parent relations
m.tracePath({b: fwdPath}, delay=100)     # Final shortest path

textLabel(m, 'BFS Path Length', len(fwdPath) + 1)
textLabel(m, 'BFS Search Length', len(bfsPath))

m.run()


##########################################################################################################


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
m.CreateMaze(loadMaze='maze--2025-12-23--20-00-35.csv')

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

textLabel(m, 'DFS Path Length', len(fwdPath) + 1)
textLabel(m, 'DFS Search Length', len(dfsPath))

m.run()