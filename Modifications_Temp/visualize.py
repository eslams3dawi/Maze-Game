# visualize.py
from pyMaze import agent, textLabel, COLOR

def visualize_maze(m, searchPath, parentPath, fwdPath, title):
    a = agent(m, footprints=True, color=COLOR.blue)
    b = agent(m, 1, 1, footprints=True, color=COLOR.yellow, goal=(m.rows, m.cols))
    c = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({a: searchPath}, delay=100)
    m.tracePath({b: parentPath}, delay=100)
    m.tracePath({c: fwdPath}, delay=100)
    textLabel(m, f'{title} Path Length', len(fwdPath)+1)
    textLabel(m, f'{title} Search Length', len(searchPath))
    m.run()
