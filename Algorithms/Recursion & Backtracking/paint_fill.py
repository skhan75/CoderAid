
def paint_fill(screen, x, y, newColor):
    oldColor = screen[x][y]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in screen]))
    fill(screen, x, y, oldColor, newColor)
    print('\n\n')
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in screen]))

def fill(screen, x, y, oldColor, newColor):

    if x<0 or y<0 or x>len(screen)-1 or y>len(screen[0])-1:
        return

    if screen[x][y]!= oldColor:
        return

    # Replace the color at screen(x,y) first
    screen[x][y] = newColor

    fill(screen, x+1, y, oldColor, newColor)
    fill(screen, x-1, y, oldColor, newColor)
    fill(screen, x, y+1, oldColor, newColor)
    fill(screen, x, y-1, oldColor, newColor)




if __name__ == "__main__":
    screen = [[1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 0, 1, 1],
            [1, 2, 2, 2, 2, 0, 1, 0],
            [1, 1, 1, 2, 2, 0, 1, 0],
            [1, 1, 1, 2, 2, 2, 2, 0],
            [1, 1, 1, 1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1, 2, 2, 1]]
    paint_fill(screen, 4, 4, 3)
