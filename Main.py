import tkinter as tk
from pyMaze import maze
import BFS, DFS, AStar
from visualize import visualize_maze

# ================== CREATE MAZE ONCE ==================
m = maze(15, 20)
m.CreateMaze(loadMaze='maze--2025-12-23--22-44-35.csv')

def clear_paths():
    m._tracePathList.clear()

# ================== BUTTON ACTIONS ==================
def run_bfs():
    clear_paths()
    s, p, f = BFS.BFS(m)
    visualize_maze(m, s, p, f, "BFS")

def run_dfs():
    clear_paths()
    s, p, f = DFS.DFS(m)
    visualize_maze(m, s, p, f, "DFS")

def run_astar():
    clear_paths()
    s, p, f = AStar.aStar(m)
    visualize_maze(m, s, p, f, "A*")

# ================== EMBEDDED CONTROL PANEL ==================
control_frame = tk.Frame(m._win, bg="white", bd=2, relief="solid")
control_frame.place(relx=0.90, rely=0.5, anchor="center") 

tk.Label(control_frame, text="Choose Search", font=("Arial", 12)).pack(pady=5)
tk.Button(control_frame, text="BFS", width=10, command=run_bfs).pack(pady=3)
tk.Button(control_frame, text="DFS", width=10, command=run_dfs).pack(pady=3)
tk.Button(control_frame, text="A*",  width=10, command=run_astar).pack(pady=3)

# ================== RUN ==================
m.run()
