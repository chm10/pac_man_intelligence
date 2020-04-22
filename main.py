from queue import PriorityQueue
import searches.dfs as dfs

if __name__ == "__main__":
    graph = {
        (1,1): set([(1,2), (2,1)]),
        (1,2): set([(2,2), (1,3)]),
        (1,3): set([(1,4), (1,2)]),
        (1,4): set([(1,3), (2,4)]),
        (2,1): set([(1,1), (1,3)]),
        (2,2): set([(2,3), (1,2)]),
        (2,3): set([(2,2)]),
        (2,4): set([(1,4), (3,4)]),
        (3,1): set([(2,1), (3,2)]),
        (3,2): set([(3,1), (3,3)]),
        (3,3): set([(3,2), (3,4)]),
        (3,4): set([(2,4), (3,3)]),
    }

    path = dfs.dfs(graph, (1,1), (2,2))
    print(graph)
    print("path", path) # ==> [(1,2), (2,2), (2,3)]