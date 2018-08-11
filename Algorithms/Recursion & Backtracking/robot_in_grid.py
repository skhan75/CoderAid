# Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can
# only move in two directions: right and down. How many possible paths are there for
# the robot?
# FOLLOW UP
# Imagine certain squares are “off limits”, such that the robot can not step on them.
# Design an algorithm to get all possible paths for the robot.

def get_path(maze):
    if maze == None or len(maze) == 0:
        return False

    path = []
    failedPoints = []

    row = len(maze) - 1
    column = len(maze[0]) - 1

    if is_path(maze, row, column, path, failedPoints, offLimits):
        return path

    return None


def is_path(maze, row, column, path, failedPoints, offLimits):
    #If out of bounds or not availabe, return
    if row < 0 or column < 0 or not maze[row][column]:
        return False

    # Current podition of robot
    point = (row, column)

    # memoizing points that fails in creating a path
    if point in failedPoints:
        return False

    # off-limits
    if point in offLimits:
        return False

    isAtOrigin = (row == 0) and (column == 0)

    if isAtOrigin or is_path(maze, row, column-1, path, failedPoints) or is_path(maze, row-1, column, path, failedPoints):
        path.append(point)
        return True

    failedPoints.append(point)
    return False



if __name__ == "__main__":
    #maze is a matrix
    get_path(maze, offLimits)
