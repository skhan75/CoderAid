"""
A number is called happy if it leads to 1 after a sequence of steps
where in each step number is replaced by sum of squares of its digit
that is if we start with Happy Number and keep replacing it with digits
square sum, we reach 1.

Example:
    Input: n = 19
    Output: True
    19 is Happy Number,
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
    As we reached to 1, 19 is a Happy Number.

    Input: n = 20
    Output: False
"""

def verifiy_happy_number(number):

    # 1 and 7 are the only single digit happy numbers
    # So if the input is either of them, we don't wanna use compute resources,
    # rather return True directly
    if number in [1,7]:
        return True

    else:
        digits = map(int, str(number))

        # If digit is 145, its subsequent sum of square products is never gonna
        # end with 1. Hence return False directly, saving (n-4) additional operations
        if digits == [1,4,5]:
            return False

        # Similarly, if digits are among either 130 and 13, its sum of squared products
        # are always gonna be 1. Hence return True directly, saving (n-2) operations
        if digits == [1,3,0] or digits == [1,3]:
            return True

        while len(digits) > 1:
            sop = 0
            for d in digits:
                sop += (d*d)

            digits = map(int, str(sop))

        if digits[0] == True:
            return True
        else:
            return False

if __name__ == "__main__":
    happies = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82,
    86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192,
    193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302,
    310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379,
    383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496,
    536, 556, 563, 565, 566, 608, 617, 622, 623, 632, 635, 637, 638, 644, 649,
    653, 655, 656, 665, 671, 673, 680, 683, 694, 700, 709, 716, 736, 739, 748,
    761, 763, 784, 790, 793, 802, 806, 818, 820, 833, 836, 847, 860, 863, 874,
    881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937, 940,
    946, 964, 970, 973, 989, 998, 1000]

    unhappies = [2,3,4,5,6,8,9,12,65,77,92,101,555,919]

    for no in happies:
        assert verifiy_happy_number(no) == True

    for no in unhappies:
        assert verifiy_happy_number(no) == False
