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
m.CreateMaze(loopPercent=10, theme='dark')

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

textLabel(m,'BFS Path Length',len(fwdPath)+1)

m.run()
