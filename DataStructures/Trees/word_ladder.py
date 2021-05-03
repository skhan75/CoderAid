"""
    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.
    Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
    Example 1:

    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    Output: 5

    Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
    Example 2:

    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    Output: 0

    Explanation: The endWord "cog" is not in wordList, therefore no possible transformation

    Courtesy @ LeetCode
"""

from collections import defaultdict

"""
TIME COMPLEXITY - O(M2 x N), where M is the length of each word and N is the total no of words
in the input list.
For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it.
Since the length of each word is MM and we have NN words, the total number of iterations the algorithm takes
to create all_combo_dict is M times MxN
Additionally, forming each of the intermediate word takes O(M) time because of the substring operation used to
create the new string. This adds up to a complexity of O(M2xN).

SPACE COMPLEXITY - O(M2 x N)
Each word in the word list would have MM intermediate combinations.
To create the all_combo_dict dictionary we save an intermediate word as the key and its corresponding original
words as the value. Note, for each of MM intermediate words we save the original word of length MM.
This simply means, for every word we would need a space of M2 to save all the transformations corresponding to it.
Thus, all_combo_dict would need a total space of O(M2XN).
Visited dictionary would need a space of O(MxN) as each word is of length M
Queue for BFS in worst case would need a space for all O(N) words and this would also result
in a space complexity of O(MxN).
"""
def word_ladder_bfs(beginWord, endWord, wordList):

    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    # Since all the words are of same length
    N = len(beginWord)

    # Dictionary to hold combination of words that can be formed
    # from any given word, by changing one letter at a time.
    all_combo_dict = defaultdict(list)

    for word in wordList:
        for i in range(N):

            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        """
        {'do*': ['dot', 'dog'], 'h*t': ['hot'], '*ot': ['hot', 'dot', 'lot'], 'd*t': ['dot'], 'lo*': ['lot', 'log'],
        'ho*': ['hot'], 'c*g': ['cog'], 'l*g': ['log'], 'd*g': ['dog'], '*og': ['dog', 'log', 'cog'], 'co*': ['cog'],
        'l*t': ['lot']}
        """

    # Use BFS
    queue = []
    # Append start node and level to the queue
    queue.append((beginWord, 1))
    # Visited to avoid cycles
    visited = {beginWord: True}

    while queue:
        # Get the current word as the starting node and find all possible intermediate nodes it can jump to
        current_word, level = queue.pop(0)

        # Now find all the generic transformations of the current_word and find out if any of these transformations
        # is also a transformation of other words in the word list. This is achieved by checking all_combo_dict
        for i in range(N):
            # Intermediate words for current word -- generic transformation
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            # Next find all the words which share the same intermediate state
            # << The list of words we get from all_combo_dict are all the words which will have a common intermediate state
            # with the current_word. These new set of words will be the adjacent nodes/words to current_word and hence added
            # to the queue >>
            for word  in all_combo_dict[intermediate_word]:
                # If at any point we find the end word
                # we can reutrn the answer
                if word == endWord:
                    return level+1

                # Otherwise add it to the BFS queue. Also mark it visited
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level+1))

            all_combo_dict[intermediate_word] = []

    # Return 0 if no path found
    return 0

def word_ladder_bidirectional_bfs(beginWord, endWord, wordList):

    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    N = len(beginWord)

    # Dictionary to hold combination of words that can be formed
    # from any given word, by changing one letter at a time.
    all_combo_dict = defaultdict(list)

    for word in wordList:
        for i in range(N):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    def visit_word_node(queue, visited, others_visited):
        print visited, others_visited
        current_word, level = queue.pop(0)

        print current_word, level, N

        for i in range(N):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state
            for word in all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal that means we have found the answer
                if word in others_visited:
                    return level + others_visited[word]

                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hope
                    visited[word] = level + 1
                    queue.append((word,level + 1))

        return None

    # Create Queues bidirectional BFS
    queue_begin = [] # To start BFS from begin word
    queue_end = [] # To start BFS from end word

    queue_begin.append((beginWord, 1))
    queue_end.append((endWord, 1))

    visited_begin = {beginWord, 1}
    visited_end = {endWord, 1}
    ans = None

    # We do a bidirectional search starting one pointer from begin word
    # and one from end word. Hopping one by one.
    while queue_begin and queue_end:
        # One hop from begin word
        ans = visit_word_node(queue_begin, visited_begin, visited_end)
        if ans:
            return ans

        # One hop from end word
        ans = visit_word_node(queue_end, visited_end, visited_begin)
        if ans:
            return ans

    return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print word_ladder_bfs(beginWord, endWord, wordList)
    print word_ladder_bidirectional_bfs(beginWord, endWord, wordList)
