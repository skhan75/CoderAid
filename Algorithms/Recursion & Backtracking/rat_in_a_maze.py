import numpy as np

def solveMaze(maze):
    solution_matrix = [[0 for _ in range(len(maze))] for _ in range(len(maze))]
    failedPoints = []

    row = len(maze)-1
    col = len(maze[0])-1

    if maze == None or len(maze) == 0:
        return False

    if solveMaze_util(maze, row, col, solution_matrix, failedPoints) == False:
        return False

    return True, solution_matrix

def solveMaze_util(maze, row, col, solution_matrix, failedPoints):

    # If out of bounds
    if row < 0 or col < 0 or not maze[row][col]:
        return False

    point = (row, col)

    # Avoiding already faield points, to remove redundancy
    if point in failedPoints:
        return False

    isAtOrigin = row == 0 and  col == 0

    # If it has backtracked till origin successfully
    if isAtOrigin:
        solution_matrix[row][col] = 1
        return True

    # Backtracking moving left of the maze
    if solveMaze_util(maze, row, col-1, solution_matrix, failedPoints):
        solution_matrix[row][col] = 1
        return True

    # Backtracking moving down the maze
    if solveMaze_util(maze, row - 1, col, solution_matrix, failedPoints):
        solution_matrix[row][col] = 1
        return True


    failedPoints.append(point)
    return False


# Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]

    does_path_exists = solveMaze(maze)[0]
    solution_matrix = solveMaze(maze)[1]

    print(does_path_exists)
    print(np.matrix(solution_matrix))
