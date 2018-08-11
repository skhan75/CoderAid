def rotate_image(mat):
    #mat = [[None for i_ in range(int(N))] for j in range(int(N))]
    N = len(mat)
    for layer in range(N // 2):
        first, last = layer, N-layer-1
        for i in range(first, last):
            offset = i - first

            # save top
            top = mat[layer][i]
            #left --> top
            mat[layer][i] = mat[last-offset][layer]
            # bottom -> left
            mat[last-offset][layer] = mat[last][last-offset]
            # right -> bottom
            mat[last][last-offset] = mat[i][last]
            # top -> right
            mat[i][last] = top


    return mat

if __name__ == "__main__":
    N = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    print rotate_image(N)
