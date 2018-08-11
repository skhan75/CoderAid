""" INTERVIEW CAKE
You wrote a trendy new messaging app, MeshMessage,
to get around flaky cell phone coverage.

Instead of routing texts through cell towers,
your app sends messages via the phones of nearby users,
passing each message along from one phone to the next until it reaches
the intended recipient.
(Don't worry—the messages are encrypted while they're in transit.)

Some friends have been using your service,
and they're complaining that it takes a long time for messages to get delivered.
After some preliminary debugging, you suspect messages might not be taking
the most direct route from the sender to the recipient.

Given information about active users on the network,
find the shortest route for a message from one user (the sender) to another (the recipient). Return an array of users that make up this route.
"""

def reconstruct_path(path, source, target):
    reversed_shortest_path = []

    current_node = target

    while current_node is not None:
        reversed_shortest_path.append(current_node)
        current_node = path[current_node]

    print reversed_shortest_path[::-1]

    return reversed_shortest_path[::-1]

# BFS to find the target node with least hops in an Undirected Graph
def bfs(network, source, target):

    # Initialize an empty queue to keep track of all the nodes
    queue = []
    # Push source to queue
    queue.append(source)

    # Initialize already seen nodes
    visited = []
    # Append the source to visited
    visited.append(source)

    # Keeping a track of how we reached each node
    current_path = dict()
    current_path[source] = None

    while queue is not None:
        # Pop from end (since its gonna be a FIFO)
        current_node = queue.pop(0)

        # Stop when we reach our target
        # In BFS, the moment you reach a target implicitly means that you've
        # reached via the least possible hop
        if current_node == target:
            # Hence we just reconstruct the path and return it
            return reconstruct_path(current_path, source, target)

        for neighbor in network[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

                # Keep track of how we reached this node
                current_path[neighbor] = current_node


    return shortest_path

def find_optimized_route(newtork, source, target):
    return bfs(network, source, target)


if __name__ == "__main__":
    network = dict()
    network["Min"] = [ "William", "Jayden", "Omar" ]
    network["William"] = [ "Min", "Noam" ]
    network["Jayden"] = [ "Min", "Amelia", "Ren", "Noam" ]
    network["Ren"] = [ "Jayden", "Omar", "Scott", "Nathan" ]
    network["Amelia"] = [ "Jayden", "Adam", "Miguel" ]
    network["Adam"] = [ "Amelia", "Miguel", "Lucas" ]
    network["Miguel"] = [ "Amelia", "Adam", "Nathan" ]
    network["Noam"] = [ "Nathan", "Jayden", "William", "Lucas" ]
    network["Omar"] = [ "Ren", "Min", "Scott" ]
    network["Scott"] = [ "Omar", "Ren", "Nathan"]
    network["Lucas"] = [ "Adam", "Noam" ]
    network["Nathan"] = [ "Scott", "Miguel", "Ren" ]

    print find_optimized_route(network, "Min", "Nathan")
