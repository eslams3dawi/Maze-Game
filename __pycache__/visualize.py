from pyMaze import agent, textLabel, COLOR

def visualize_maze(m, searchPath, parentPath, fwdPath, title):

    if title == 'BFS':
        a = agent(m, footprints=True, color=COLOR.red, shape='square', filled=True)
        b = agent(m, footprints=True, color=COLOR.light, shape='square', filled=False)
        c = agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape='square', goal=(m.rows, m.cols))

    elif title == 'DFS':
        a = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=False)
        b = agent(m, footprints=True, color=COLOR.red, shape='square', filled=False)
        c = agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape='square', goal=(m.rows, m.cols))

    elif title == 'A*':
        a = agent(m, footprints=True, color=COLOR.blue, shape='arrow', filled=False)
        b = agent(m, footprints=True, color=COLOR.light, shape='square', filled=False)
        c = agent(m, 1, 1, footprints=True, color=COLOR.green, shape='square')

    m.tracePath({a: searchPath}, delay=100)
    m.tracePath({b: parentPath}, delay=100)
    m.tracePath({c: fwdPath}, delay=100)

    textLabel(m, f'{title} Path Length', len(fwdPath))
    textLabel(m, f'{title} Search Length', len(searchPath)) 