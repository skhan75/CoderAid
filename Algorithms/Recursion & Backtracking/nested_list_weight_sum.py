
def nested_list_sum(nestedList):
    depth = get_depth(nestedList)
    print "Depth", depth
    return calc_sum(nestedList, depth)

def get_depth(nestedList):

    depth = 1
    for item in nestedList:
        if type(item) is not int:
            current = get_depth(item)
            depth = max(depth, current + 1)

    return depth

def calc_sum(nestedList, depth):
    print "DEPTH", depth
    if nestedList is None or len(nestedList) == 0:
        return 0

    sum = 0
    for item in nestedList:
        if type(item) is int:
            print sum, "+", depth, "*", item
            sum += depth * item
            print "SUM", sum

        else:
            print "LIST", item
            sum += depth * calc_sum(item, depth - 1)

    return sum

if __name__ == "__main__":
    print nested_list_sum([[1,1],2,[1,1]])
