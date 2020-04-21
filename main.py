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

if __name__ == "__main__":
    ## Map with 31 x 28
    ## Considering . as path == 1 and | as wall == 0
    ## 0 == wall , 1 == path, 2 == startpoint, 3 == goal , 4 == block

    mymap = generateDefaultRandomMap()
    row = 31
    column = 28 
    np_map = conv_str2int(row,column,mymap)
    print(np_map)