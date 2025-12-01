from pyMaze import maze, COLOR, agent, textLabel

#A Star is intellegent algorithm, it only move to the cheapest cost from the result of the funtion f(n) = g(n) + h(n)
#g(n) is the actual cost of the path from the start node to n
#h(n) is the heuristic function that estimates the cost of the cheapest path from n to the goal

#with A star search algorithm, it chooses the lowest cost, if all neighbors have the same cost, it chooses the lowest h(n), if also have the same h(n), it chooses any cell
#A star uses priority queue, that works by giving the priority to the cheapest value by putting it at the first of the queue that available in python in a moduel:queue






#------------GUI With Documentation-------------#

Maze = maze(2,2)
#any maze is consists of matrix 
    #(rows and columns:
        #(1,1)(1,2)(1,3)
        #(2,1)(2,2))(2,3))
#set the number of rows, columns

Maze.CreateMaze(theme=COLOR.light)
    #set the goal position, default is 0,0 
    #pattern= 'h' means the maze is horizontal ,=none is default
    #loopPercent=0 means the number of loop paths is 0
    #saveMaze → with every run the maze shape is changed, to save specific maze shape just save it in csv file and then you can modify any path in that maze and use it by loadMaze='shapeName'
    #theme=COLOR.red , set the background color 

Agent = agent(Maze, filled=True, footprints=True, color='red')#Maze is the parentMaze & the coordinates of the agent is 
#footprints to track the agent while search the goal

Maze.tracePath({Agent:Maze.path}, delay=150) #delay → less value = fast agent speed

#Maze.enableArrowKey(Agent) #To enable you to play

#print(Maze.grid) #print all maze grid (good for agent's tracking)

print(Maze.maze_map)
#print a list of dictionary that indicates the state of each direction, 1 means the direction is open, 0 means the direction is closed 
#         North
#West                East
#         South

labelTotalCells = textLabel(Maze, 'Total Cells', Maze.rows * Maze.cols)
Maze.run()

