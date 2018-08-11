pofrom Priority_Queue import *
from Graph import *
import sys

def djikstra_shortest_path(graph, sourceVertex):

    min_heap = PriorityQueue(True)
    # Distance Map
    distance = {}
    # Parent Map, where is the vertex coming from
    parent = {}

    inifinite = sys.maxsize

    # Assing all the vertices maximum weigtage
    for vertex in graph.all_vertices.values():
        min_heap.add_task(inifinite, vertex)

    # Now put weight on sourceVertex as 0, since it points to itself
    min_heap.change_task_priority(0, sourceVertex)
    distance[sourceVertex] = 0
    parent[sourceVertex] = None

    while min_heap.is_empty() is False:
        # peek the topmost element of the minheap
        task = min_heap.peek_task()
        weight = min_heap.get_task_priority(task)
        # Extract min
        current = min_heap.pop_task()
        # Assign weight on the current vertex
        distance[current] = weight

        # Explore all the neighbors of current
        for edge in current.edges:
            # get the adjacent_vertex
            adjacent = get_other_vertex_for_edge(current, edge)

            # If minheap contains this adjacent_vertex
            if min_heap.contains_task(adjacent) is False:
                continue

            # Add distance of current vertex to the edge weight to get the distance of adjacent vertex from source vertex
            # when it goes through current vertex
            new_distance = distance[current] + edge.w
            if min_heap.get_task_priority(adjacent) > new_distance:
                # decrease the value in the minheap to the new value
                min_heap.change_task_priority(new_distance, adjacent)
                parent[adjacent] = current

    return distance




def get_other_vertex_for_edge(vertex, edge):
    if edge.u_vertex.key == vertex.key:
        return edge.v_vertex
    else:
        return edge.u_vertex


if __name__ == '__main__':
    graph = Graph(False)
    graph.add_edge(1,2,5)
    graph.add_edge(2,3,2)
    graph.add_edge(1,4,9)
    graph.add_edge(1,5,3)
    graph.add_edge(5,6,2)
    graph.add_edge(6,4,2)
    graph.add_edge(3,4,3)

    distance = djikstra_shortest_path(graph, graph.all_vertices[1])
    print(distance)
