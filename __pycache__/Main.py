import tkinter as tk
from pyMaze import maze, agent, textLabel, COLOR
import BFS, DFS, AStar

# ================== CREATE MAZE ==================
m = maze(15, 20)
m.CreateMaze(loadMaze='maze--2025-12-23--22-44-35.csv')

# ================== HELPER ==================
def fwdPath_to_list(fwdPath, start, goal):
    path = []
    cell = start
    while cell != goal:
        next_cell = fwdPath.get(cell)
        if not next_cell:  # safety check
            break
        path.append(next_cell)
        cell = next_cell
    return path

def clear_paths():
    m._tracePathList.clear()

# ================== VISUALIZATION ==================
def visualize_maze(searchPath, parentPath, fwdPath, title):
    start = (m.rows, m.cols)
    goal = m._goal
    fwd_list = fwdPath_to_list(fwdPath, start, goal)

    if title == 'BFS':
        a = agent(m, footprints=True, color=COLOR.red, shape='square', filled=True)
        c = agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape='square', filled=True)

    elif title == 'DFS':
        a = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=False)
        c = agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape='square', filled=True)

    elif title == 'A*':
        a = agent(m, footprints=True, color=COLOR.blue, shape='arrow', filled=True)
        c = agent(m, 1, 1, footprints=True, color=COLOR.green, shape='square', filled=True)

    # رسم search path
    m.tracePath({a: searchPath}, delay=50)

    # رسم final path
    m.tracePath({c: fwd_list}, delay=150)

    # عرض الإحصائيات
    textLabel(m, f'{title} Path Length', len(fwd_list))
    textLabel(m, f'{title} Search Length', len(searchPath))

# ================== BUTTON ACTIONS ==================
def run_bfs():
    clear_paths()
    s, p, f = BFS.BFS(m)
    visualize_maze(s, p, f, "BFS")

def run_dfs():
    clear_paths()
    s, p, f = DFS.DFS(m)
    visualize_maze(s, p, f, "DFS")

def run_astar():
    clear_paths()
    s, p, f = AStar.aStar(m)
    visualize_maze(s, p, f, "A*")

# ================== CONTROL PANEL ==================
control_frame = tk.Frame(m._win, bg="white", bd=2, relief="solid")
control_frame.place(relx=0.90, rely=0.5, anchor="center")

tk.Label(control_frame, text="Choose Algorithm", font=("Arial", 12)).pack(pady=5)
tk.Button(control_frame, text="BFS", width=10, command=run_bfs).pack(pady=3)
tk.Button(control_frame, text="DFS", width=10, command=run_dfs).pack(pady=3)
tk.Button(control_frame, text="A*", width=10, command=run_astar).pack(pady=3)

# ================== RUN ==================
m.run()
