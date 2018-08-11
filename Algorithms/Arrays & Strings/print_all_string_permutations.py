"""
Method 1: Referenced: https://www.youtube.com/watch?v=nYFd7VHKyWQ&t=1205s
@courtesy - Tushar Roy
"""

def permute(string):
    # Initialize a count map to keep count of characters
    character_count_map = {ch: 0 for ch in string}

    # Count each character and assign it to the map
    for char in string:
        character_count_map[char] += 1

    result = [ None for _ in range(0, len(string)) ]

    permute_util(character_count_map, result, 0)

def permute_util(character_count_map, result, level):
    # Return when you reach the length of the string and print the permutation
    if level == len(result):
        # Result containing the sequencing of characters
        print_permutation(result)
        return

    for ch in character_count_map:

        if character_count_map[ch] == 0:
            continue

        result[level] = ch

        # We decrement the count of each iteration of that character
        character_count_map[ch] -= 1
        # Recursively iterate the other possible characters with count > 0
        permute_util(character_count_map, result, level+1)
        # When all the perumtations via a character as pivot is done,
        # put back its count for other possible permutations via another character as pivot
        # to take place
        character_count_map[ch] += 1


""" Method 2: Referenced: https://www.youtube.com/watch?v=78t_yHuGg-0
"""

def permute_easy(string):
    permute_helper(string, "")

def permute_helper(s, chosen):

    # Base Case
    if s is "":
        print chosen

    else:
        # Choose/Exlplore/Unchoose
        for i in range(0, len(s)):

            # 1. Choose a character as a Pivot
            c = s[i]

            # 2. Concatenate it to the chosen string
            chosen += c

            # 3. Delete it from the input string
            s = s.replace(c, "")

            # 4. Explore all other possibilities with this character as pivot
            permute_helper(s, chosen)

            # 5. Unchoose --> Put it back as it was

            # 5a. So insert back the deleted character to the string
            s = s[:i] + c + s[i:]

            # 5b. And delete last character from chosen
            chosen = chosen[:len(chosen)-1]
            print 'Chosen', chosen




def print_permutation(input):
    for ch in input:
        print ch,

    print ''


permute('ABC')
permute_easy('ABC') # Personally I found this more easy to understand, code and remember.
