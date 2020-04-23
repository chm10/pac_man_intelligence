from sample import generateDefaultRandomMap
import numpy as np


def conv_str2int(row, column, maze):
    """Function to convert string to int.

    We have big string with * | breakline caracter is very hard to see 
    how to process this format (not impossible) but more difficult to see.

    Args:
        row (int): number of line (use  number without subtract as index)
        column (int): number of column (use  number without subtract as index)
        maze (str): string with map

    Returns:
        narray: numpy array[row][column]

    """
    ## Map with 31 x 28
    ## Considering . as path == 1 and | as wall == 0
    # We have matrix 31 x 28 but last column == '\n' we use %29 to convert int 1 until 28 line subtract 1 to use numpy array index 
    str2int = np.zeros((row,column))
    line = 0
    for idx, value in enumerate(maze):
        if (idx!=0)&(value=='\n'):
            line = line + 1
        else:
            if (value == '.'):
                str2int[line][(idx%(column+1))-1] = 1
    return str2int

def conv_int2str(maze):
    """Function to convert int to string.


    Args:
        narray: numpy array[row][column]

    Returns:
        maze (str): string with map

    """
    ## Map with 31 x 28
    ## Considering . as path == 1 and | as wall == 0
    # We have matrix 31 x 28 but last column == '\n' we use %29 to convert int 1 until 28 line subtract 1 to use numpy array index 
    int2str = ""
    x,y = maze.shape
    for i in range(0,x):
        for j in range(0,y):
            if maze[i][j] == 0:
                int2str = int2str + '|'
            elif maze[i][j] == 1:
                int2str = int2str + '.'
            elif maze[i][j] == 2:
                int2str = int2str + 'I'
            elif maze[i][j] == 3:
                int2str = int2str + '*'
            elif maze[i][j] == 4:
                int2str = int2str + '#'
            elif maze[i][j] == 5:
                int2str = int2str + 'F'
        int2str = int2str + '\n'
    
    return int2str
    
    
    for idx, value in enumerate(maze):
        if (idx!=0)&(value=='\n'):
            line = line + 1
        else:
            if (value == '.'):
                str2int[line][(idx%(column+1))-1] = 1
    return str2int

def available_path(maze):
    """Identify available path.

    Considering available path equal 1 this function returno all available path as list of tupla.

    Arguments:
        maze: numpy array[row][column]

    Returns:
        suffle_path(list): List of tuple with available position e.g [(0,1),(1,1)...]  
    """
    idx_goals = np.where(maze == 1)
    sff_idx = list()
    for i in range(len(idx_goals[0])):
        sff_idx.append((idx_goals[0][i],idx_goals[1][i]))
    np.random.shuffle(sff_idx)
    return sff_idx     

def add_goal(n_goal,maze,inplace=False):
    """Add goal in the map.

    This function will add goal in random location 

    Arguments:
        n_goal (int): number of goal
        maze (narray): narray: numpy array[row][column]
        inplace(bool): overwrite maze or make copy

    Returns:
        narray: numpy array[row][column]
    """
    if inplace:
        for position in available_path(maze)[:n_goal]:
            maze[position[0]][position[1]] = 3
        return maze
    else:
        maze_copy = maze.copy()
        for position in available_path(maze_copy)[:n_goal]:
            maze_copy[position[0]][position[1]] = 3
        return maze_copy



def add_block(n_block,maze,inplace=False):
    """Add block in the map.

    This function will add 4 as a block 

    Args:
        n_block (int): number of block
        maze (narray): narray: numpy array[row][column]
        inplace(bool): overwrite maze or make copy

    Returns:
        narray: numpy array[row][column]
    """
    if inplace:
        for position in available_path(maze)[:n_block]:
            maze[position[0]][position[1]] = 4
        return maze
    else:
        maze_copy = maze.copy()
        for position in available_path(maze_copy)[:n_block]:
            maze_copy[position[0]][position[1]] = 4
        return maze_copy

step = [np.array([0,-1]),np.array([0,1]),np.array([1,0]),np.array([-1,0])] # simulate step to up,down,right,left 


if __name__ == "__main__":
    ## Map with 31 x 28
    ## Considering . as path == 1 and | as wall == 0
    ## 0 == wall , 1 == path, 2 == startpoint, 3 == goal , 4 == block ,5 == end position

    mymap = generateDefaultRandomMap()
    row = 31
    column = 28 
    np_map = conv_str2int(row,column,mymap)
    add_goal(10,np_map,inplace=True)
    add_block(3,np_map,inplace=True)
    start_position = available_path(np_map)[:1]
    end_position = available_path(np_map)[:1]
    np_map[start_position[0][0]][start_position[0][1]] = 2
    np_map[end_position[0][0]][end_position[0][1]] = 5
    print(conv_int2str(np_map))