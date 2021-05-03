"""
PROBLEM: Word Break
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung"
or "i like sam sung".
"""

"""
Brute Force - Recursive Solution:
---------------------------------
We consider each prefix and search it recursively in the dictionary.

Complexity:
-----------
    - Each call, we are calling the recursive function from 1,2,...n-1 (worst case)
    - To compute work n, we are recursively chceking the prefixes of length n-1,...,1
    - So Time complexity of current call is:
        T(n) = T(n-1) + T(n-2) + .... + T(1)
        T(1) = T(2) = 1
        T(3) = T(1) + T(2) = 1+1 =2; // 2^1
        T(4) = T(1)+ T(2) + T(3) = 1+1+2 =4; //2^2
        T(5) = T(1) + T(2) +T(3) +T(4) = 1+1+2+4 =8; //2^3

        Hence if you substitute first few values, the Time complexity is 2^(n-2)
"""
def word_break(str):
    size = len(str)

    if size == 0:
        return True

    # Check for all the prefixes recursively
    for i in range(1, size+1):
        if dictionaryContains(str[0:i]) and word_break(str[i:size]):
            return True

    return False


def dictionaryContains(word):
    if word in dictionary:
        return True

    return False


dictionary = [
    "mobile","samsung","sam","sung",
    "man","mango","icecream","and",
    "go","i","like","ice","cream"
]
assert word_break("ilikesamsung") == True
assert word_break("iiiiiiii") == True
assert word_break("") == True
assert word_break("samsungandmango") == True
assert word_break("samsungandmangok") == False
