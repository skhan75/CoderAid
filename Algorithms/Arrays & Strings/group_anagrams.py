def group_anagrams(string_array):
    anagrams = {}

    for i in string_array:
        word = ''.join(sorted(i.lower()))
        if word not in anagrams:
            anagrams.setdefault(word, [])
        anagrams[word].append(i)

    keys = anagrams.keys()
    index = 0

    for i in keys:
        values = anagrams.get(i)
        for j in values:
            string_array[index] = j
            index += 1

    print (string_array)



strings = [0] * 8
strings[0] = "abed"
strings[1] = "later"
strings[2] = "bead"
strings[3] = "alert"
strings[4] = "altered"
strings[5] = "bade"
strings[6] = "alter"
strings[7] = "Alerted"
group_anagrams(strings)
