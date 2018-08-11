def count_a_recursive(N):
    # The optimal string length is N
    # when N is smaller than 7
    if N < 7:
        return N

    # Initialize result as max negative infinity
    max = float('-inf')

    # It is observed that we will always have 3 A's in the begining
    # TRY ALL POSSIBLE BREAK-POINTS
    # For any keystroke N, we need to
    # loop from N-3 keystrokes back to
    # 1 keystroke to find a breakpoint
    # 'b' after which we will have Ctrl-A,
    # Ctrl-C and then only Ctrl-V all the way.
    for b in range(N-3, 0, -1):

         # If the breakpoint is s at b'th
         # keystroke then the optimal string
         # would have length
         # (n-b-1)*screen[b-1];
        current = (N-b-1) * count_a_recursive(b)

        if current > max:
            max = current

    return max



def count_a_dp(N):
    # The optimal string length is N
    # when N is smaller than 7
    if N < 7:
        return N

    # Initialize a memoization list
    T = [0 for _ in range(N+1)]

    # Fill up the list till N = 7 with the same numbers in order till 7
    # because we know till less than 7 we return the same number of count
    for num in range(7):
        T[num] = num

    for n in range(7, N+1):
        for b in range(N-3, 0 ,-1):
            T[n] = max(T[n], T[b] * (n - b -1))

    return T[N]



if __name__ == '__main__':
    expected = 9
    assert expected == count_a_recursive(7)
    assert expected == count_a_dp(7)
