import tkinter as tk
from tkinter import messagebox
from pyMaze import maze
from visualize import visualize_maze
import AStar
import BFS
import DFS

def run_selected_search():
    selection = algo_var.get()
    if not selection:
        messagebox.showwarning("اختيار", "اختر خوارزمية أولًا!")
        return
    
    m = maze(15, 20)
    m.CreateMaze(loopPercent=10, theme='dark')
    
    if selection == "A*":
        searchPath, parentPath, fwdPath = AStar.aStar(m)
    elif selection == "BFS":
        searchPath, parentPath, fwdPath = BFS.BFS(m)
    elif selection == "DFS":
        searchPath, parentPath, fwdPath = DFS.DFS(m)
    
    visualize_maze(m, searchPath, parentPath, fwdPath, selection)

# ---------- GUI ----------
root = tk.Tk()
root.title("Maze Search Runner")

algo_var = tk.StringVar()

tk.Label(root, text="اختر خوارزمية:").pack(pady=5)
tk.Radiobutton(root, text="A*", variable=algo_var, value="A*").pack()
tk.Radiobutton(root, text="BFS", variable=algo_var, value="BFS").pack()
tk.Radiobutton(root, text="DFS", variable=algo_var, value="DFS").pack()

tk.Button(root, text="Run Search", command=run_selected_search).pack(pady=10)

root.mainloop()
