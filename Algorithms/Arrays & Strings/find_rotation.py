"""INTERVIEW CAKE
I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through,
looking for words I didn't know. I put each word I didn't know at increasing indices
in a huge list I created in memory. When I reached the end of the dictionary,
I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical,
except they start somewhere in the middle of the alphabet,
reach the end, and then start from the beginning of the alphabet.
In other words, this is an alphabetically ordered list that has been "rotated."
"""

# Complexity --> O(log n)
def find_rotation_index(words, left, right):

    mid = (left + right) // 2

    # If floor and ceilings have converged
    if left+1 == right:
        # Between floor and ceiling is where we flipped to the beginning
        return words[right]

    if words[mid] > words[0]:
        # Go right
        return find_rotation_index(words, mid, right)
    else:
        # Go left
        return find_rotation_index(words, left, mid)


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]



print find_rotation_index(words, 0, len(words)-1)
