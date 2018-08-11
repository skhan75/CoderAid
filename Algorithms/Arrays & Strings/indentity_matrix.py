#
# Author: Sami Ahmad Khan
# File_overview: Writing a function that generates identity matrix
# **
#   An identity matrix is an NxN matrix in which all the cells on the diagonal
#   line between the upper left and bottom right are set to 1, and all other cells
#   are 0
# **
#

def identity_matrix(size):
    # Funky Pythonic way :P
    return [[1 if i == j else 0 for i in range(0,size)] for j in range(0,size)]

if __name__ == "__main__":
    print identity_matrix(5)
