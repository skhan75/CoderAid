from Graph import *
from Priority_Queue import *
import sys

def minimum_spanning_tree(graph):

    # This min heap is used to store the key-value pair of vertex and its
    # priority respectively in a Priority Queue fashion
    min_heap = PriorityQueue(True)

    # This map is going to store the vertex-edge pair that is contributing to
    # the minimum value in ourt PQ
    vertex_to_edge_map = {}

    # Store the final result
    result = []

    infinite = sys.maxsize

    # Marking all the vertices in the heap with priority as infinite
    for vertex in graph.all_vertices.values():
        min_heap.add_task(infinite, vertex)

    # Pick the first vertex
    start_vertex = graph.all_vertices.values()[0]

    # Mark it as 0
    min_heap.change_task_priority(0, start_vertex)

    # And start exploring its neighbors
    while min_heap.is_empty is False:

        # Get the current minimum weight(priority) vertex
        current = min_heap.pop_task()

        # We check which edge contributed to the minimum value  of priority
        if current in vertex_to_edge_map:
            spanning_tree_edge = vertex_to_edge_map[current]
            result.append(spanning_tree_edge)

        # Exploring all the edges and putting them in V-E map with the minimum priority
        for edge in current.edges:
            adjacent_vertex = get_other_vertex_for_edge(current, edge)
            if min_heap.contains_task(adjacent_vertex) is True and min_heap.get_task_priority(adjacent_vertex) > edge.weight:
                min_heap.change_task_priority(edge.weight, adjacent_vertex) # priority, task
                vertex_to_edge_map[adjacent_vertex] = edge

        return result



def get_other_vertex_for_edge(vertex, edge):
    if edge.u.key == vertex.key:
        return edge.v
    else:
        return edge.u

if __name__ == '__main__':
    graph = Graph(False)
    graph.add_edge(1,2,3)
    graph.add_edge(2,3,1)
    graph.add_edge(3,1,1)
    graph.add_edge(1,4,1)
    graph.add_edge(2,4,3)
    graph.add_edge(4,5,6)
    graph.add_edge(5,6,2)
    graph.add_edge(3,5,5)
    graph.add_edge(3,6,4)

    result = minimum_spanning_tree(graph)
    print(result)
