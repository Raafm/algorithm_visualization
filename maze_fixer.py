from graph.Maze_Dense import labirinth as maze   
from data_struct.stack import stack
from graph.color import *
S = stack()
ROWS = len(maze)
COLS = len(maze[0])
def look_around(current):
        i,j = current
        if(       (i+1 < ROWS)             and   (maze[i+1][ j ] == Black or maze[i+1][ j ] == Green) ): S.insert((i+1 ,  j ));  
        if(        (0  <  i )              and   (maze[i-1][ j ] == Black or maze[i-1][ j ] == Green) ): S.insert((i-1 ,  j ));  
        if(       (j+1 < COLS)             and   (maze[ i ][j+1] == Black or maze[ i ][j+1] == Green) ): S.insert(( i  , j+1));  
        if(        (j  > 0 )               and   (maze[ i ][j-1] == Black or maze[ i ][j-1] == Green) ): S.insert(( i  , j-1));  



S.insert((0,0))


while S.not_empty():

    current = S.pop()
    maze[current[0]][current[1]] = Cyan
    look_around(current)


for x in range(ROWS):
    for y in range(COLS):
        if maze[x][y] == Black:
            print((x,y))