'''
    Recursive and slow version of breaking word problem.
    If no words can be formed it returns null. O(2^n)
'''
def break_word_recursive(word, low, dictionary):
    buff = []
    for i in range(low, len(word)):
        buff.append(word[i])
        print (buff, i, word[i])
        if ''.join(buff) in dictionary:
            print ('buff', ''.join(buff))
            result = break_word_recursive(word, i+1, dictionary)
            if result is not None:
                print (''.join(buff) + " " + result)
                return ''.join(buff) + " " + result

    if ''.join(buff) in dictionary:
        return ''.join(buff)

    return None


'''
     Dynamic programming version for breaking word problem.
     It returns null string if string cannot be broken into multipe words
     such that each word is in dictionary.
     Gives preference to longer words over splits
     e.g peanutbutter with dict{pea nut butter peanut} it would result in
     peanut butter instead of pea nut butter.
'''
def break_word_dp(word, dictionary):
    import numpy as np
    flag = True
    table = [[-1 for _ in range(len(word))] for _ in range(len(word))]

    # Fill up the matrix in bottom up fashion
    for l in range(1, len(word)+1):
        for i in range(0, len(word)-l+1):
            j = i + l-1
            print(i,j)
            string = word[i:j+1]
            print(string)
            if string in dictionary:
                table[i][j] = i
                print(np.matrix(table))
                continue

            for k in range(i+1, j+1):
                print('k', k, 'i', i, 'j', j)
                if table[i][k-1] != -1 and table[k][j] != -1:
                    table[i][j] = k
                    print(np.matrix(table))
                    break

    if table[0][len(word)-1] == -1:
        flag = False

    # Create space separated word from the string
    if flag is True:
        buff = []
        i, j = 0, len(word) - 1
        while i<j:
            k = table[i][j]
            print ('i', i, 'j', j, 'k', k)
            if i == k:
                print ('i1', i, 'j1', j, 'k1', k)
                buff.append(word[i:j+1])
                print (buff)
                break
            buff.append(word[i:k] + " ")
            print(buff)
            i = k

        return ''.join(buff)

    else:
        return False



if __name__ == "__main__":
    # s = input().strip()

    dictionary = []
    dictionary.append("i")
    dictionary.append("like")
    dictionary.append("had")
    dictionary.append("play")
    dictionary.append("to")

    print (break_word_recursive("ihadliketoplay", 0, dictionary))
    print (break_word_dp("ihadliketoplay", dictionary))
