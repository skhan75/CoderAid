from queue import Queue
import sys
import numpy as np


def max_flow(capacity, source, sink):
    # We initialy initialize residual capacity to be same as capacity since there is no flow in the network
    residual_capacity = capacity
    augmented_paths = []
    max_flow = 0

    # While there exists an augmented path between source and sink
    while True:
        found_augmented_path, parent = bfs(residual_capacity, source, sink)

        if not found_augmented_path:
            break

        augmented_path = []
        v = sink
        flowable = sys.maxsize

        # Appending vertices to augmented path list with the maximum flowable qty
        # through that set of vertices
        # Maximum flowable qty is the value of the vertex with least flowable qty
        while not v == source:
            augmented_path.append(v)
            u = parent[v]
            if flowable > residual_capacity[u][v]:
                flowable = residual_capacity[u][v]
            v = u
        # Now add the source
        augmented_path.append(source)
        # Now add this list of augmented_path to main augmented_paths list.
        # But reverse the list before adding in the order of parent first
        augmented_paths.append(augmented_path[::-1])

        max_flow += flowable

        print (augmented_paths)

        # Again iterate the vertices and subtract from the to-edge and add it
        # to the from-edge
        v = sink
        while not v == source:
            u = parent[v]
            residual_capacity[u][v] -= flowable
            residual_capacity[v][u] += flowable
            v = u

    return max_flow


def bfs(residual_capacity, source, sink):
    visited = set()
    queue = []
    parent = {}
    queue.append(source)
    visited.add(source)
    found_augmented_path = False

    while queue:
        u = queue.pop()
        # Exploring all the other neighbors
        for v in range(len(residual_capacity)):
            # we are only looking for neighbors with residual capacity greater than 0
            if v not in visited and residual_capacity[u][v] > 0:
                parent[v] = u
                visited.add(v)
                queue.append(v)

                # If sink found then break
                if v == sink:
                    found_augmented_path = True
                    break

    return found_augmented_path, parent



if __name__ == '__main__':
    capacity = [[0, 3, 0, 3, 0, 0, 0],
                [0, 0, 4, 0, 0, 0, 0],
                [3, 0, 0, 1, 2, 0, 0],
                [0, 0, 0, 0, 2, 6, 0],
                [0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 9],
                [0, 0, 0, 0, 0, 0, 0]]

    max_val = max_flow(capacity, 0, 6)
    print(max_val)
