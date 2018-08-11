import numpy as np
def min_attempts_egg_drop(eggs, floors):
    num_eggs = eggs + 1
    num_floors = floors + 1

    T = [[floor if egg == 1 else 0 for floor in range(num_floors)] for egg in range(num_eggs)]

    for egg in range(2, num_eggs):
        for floor in range(1, num_floors):
            T[egg][floor] = min(1 + max(T[egg-1][k-1], T[egg][floor - k]) for k in range(1, floor + 1))

    return T[num_eggs - 1][num_floors - 1]

if __name__ == '__main__':
    eggs = 2
    floors = 100
    expected_attempts = 9

    assert expected_attempts == min_attempts_egg_drop(eggs, floors)
