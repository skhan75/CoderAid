# This code assumes the directed graph has no cycles
def topological_sort(node):
    compile_order = []
    topological_sort_helper(node, compile_order)
    return compile_order
def topological_sort_helper(node, compile_order):
    if not node.visited:
        node.visited = True
        for child in node.children:
            topological_sort_helper(child, compile_order)
        compile_order.append(node.name)
