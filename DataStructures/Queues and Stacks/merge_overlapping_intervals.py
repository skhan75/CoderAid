"""
Given a set of time intervals, merge all overlapping intervals into one and output the result
"""

def does_not_overlap_at_all(start_time_child, end_time_child, start_time_parent, end_time_parent):
    if start_time_child <= end_time_parent and end_time_child <= end_time_parent:
        return False
    elif start_time_child <= end_time_parent and end_time_child >= end_time_parent:
        return False
    else:
        return True

def either_interval_overlap(start_time_child, end_time_child, start_time_parent, end_time_parent):
    if start_time_child <= end_time_parent and end_time_child >= end_time_parent:
        return True
    else:
        return False


def get_updated_intervals(start_time_child, end_time_child, start_time_parent, end_time_parent):
    if start_time_child <= end_time_parent and end_time_child >= end_time_parent:
        return (start_time_parent, end_time_child)
    else:
        return (start_time_child, end_time_child)


def merge_intervals(intervals):
    # Sort by starting time
    intervals = sorted(intervals, key=lambda x:x[0])

    stack = []

    stack.append(intervals[0])

    for interval in intervals[1:]:
        parent_interval = stack[-1] # Stack Peek
        start_time_child, end_time_child = interval[0], interval[1]
        start_time_parent, end_time_parent = parent_interval[0], parent_interval[1]

        if does_not_overlap_at_all(start_time_child, end_time_child, start_time_parent, end_time_parent):
            stack.append(interval)

        elif either_interval_overlap(start_time_child, end_time_child, start_time_parent, end_time_parent):
            new_interval = get_updated_intervals(start_time_child, end_time_child, start_time_parent, end_time_parent)
            stack.pop()
            stack.append(new_interval)

    return stack


# Driver code
arr = [(1,5), (2,3), (4,6), (8,10), (7,8), (12,15)]
print (merge_intervals(arr))
