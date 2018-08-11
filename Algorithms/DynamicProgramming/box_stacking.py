# Strategy:
#
# 1. Get all the rotations of the boxes
# 2. Sort them in the decreasing order of their base area, because box on top needs
# to have smaller base area than box below it.

from collections import namedtuple
from itertools import permutations

dimension = namedtuple("Dimension", "height length width")

def create_all_rotations(box_dimensions):

    for current_dim in box_dimensions:
        for (height, length, width) in permutations((current_dim.height, current_dim.length, current_dim.width)):
            if length >= width:
                yield dimension(height, length, width)


# Sorting by base area i.e. length * width
def sort_by_decreasing_base_area(rotations):
    return sorted(rotations, key=lambda dim: dim.length * dim.width, reverse=True)

def can_stack(box_a, box_b):
    return box_a.length < box_b.length and box_a.width < box_b.width

def box_stack_max_height(box_dimensions):
    boxes = sort_by_decreasing_base_area(create_all_rotations(box_dimensions))
    num_of_boxes = len(boxes)

    # Fill up the Array T with all the heights in the boxes list
    T = [dim.height for dim in boxes]

    # Fill up the result array with indexes in the increasing order of no of boxes
    result = [i for i in range(num_of_boxes)]

    for i in range(1, num_of_boxes):
        for j in range(0, i):
            # can box at i be stacked above box at j
            if can_stack(boxes[i], boxes[j]):
                stacked_height = boxes[i].height + T[j]
                # if height is greater than already existing height
                if stacked_height > T[i]:
                    T[i] = stacked_height
                    # indicating i is going on top of box at j
                    result[i] = j

    max_height = max(T)
    # Get the index of max height
    start_index = T.index(max_height)

    # Now print the dimensions stored in results
    while True:
        print (boxes[start_index])
        next_index = result[start_index]
        if start_index == next_index:
            break
        start_index = next_index

    return max_height

if __name__ == '__main__':

    d1 = dimension(3, 2, 5)
    d2 = dimension(1, 2, 4)

    assert 11 == box_stack_max_height([d1, d2])
