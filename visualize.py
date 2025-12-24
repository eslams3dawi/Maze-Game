from pyMaze import agent, textLabel, COLOR

def fwdPath_to_list(fwdPath, start, goal):
    path = []
    cell = start
    while cell != goal:
        next_cell = fwdPath[cell]
        path.append(next_cell)
        cell = next_cell
    return path

def visualize_maze(m, searchPath, parentPath, fwdPath, title):
    
    # تحويل fwdPath لقائمة مرتبة
    start = (m.rows, m.cols)
    goal = m._goal  # << بدل (1,1)
    fwd_list = fwdPath_to_list(fwdPath, start, goal)

    if title == 'BFS':
        a = agent(m, footprints=True, color=COLOR.red, shape='square', filled=True)
        c = agent(m, 1, 1, footprints=True, color=COLOR.dark, shape='square', filled=True)

    elif title == 'DFS':
        a = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=False)
        c = agent(m, 1, 1, footprints=True, color=COLOR.green, shape='square', filled=True)

    elif title == 'A*':
        a = agent(m, footprints=True, color=COLOR.blue, shape='square', filled=True)
        c = agent(m, 1, 1, footprints=True, color=COLOR.yellow, shape='square', filled=True)

    # رسم استكشاف الماز
    m.tracePath({a: searchPath}, delay=50)

    # رسم final path
    m.tracePath({c: fwd_list}, delay=150)

    textLabel(m, f'{title} Path Length', len(fwd_list))
    textLabel(m, f'{title} Search Length', len(searchPath))
