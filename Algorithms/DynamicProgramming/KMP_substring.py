
# https://www.youtube.com/watch?v=KG44VoDtsAA

def has_substring(main_string, pattern):
    prefix_array = create_prefix_array(pattern)
    i,j = 0,0

    while i < len(main_string) and j < len(pattern):
        if main_string[i] == pattern[j]:
            i += 1
            j +=1
        else:
            if j != 0:
                j = prefix_array[j-1]
            else:
                i += 1
    if j == len(pattern):
        return True
    else:
        return False

def create_prefix_array(pattern):
    index = 0
    prefix_array = []*len(pattern)
    # Comparing character to itself. Hence 0
    prefix_array.insert(0,0)

    for i in range(1, len(pattern)):
        if pattern[i] == pattern[index]:
            prefix_array.insert(i, index+1)

            index += 1
        else:
            if index != 0:
                index = prefix_array[index-1]
            else:
                prefix_array.insert(i,0)

    return prefix_array


if __name__ == "__main__":
    main_string = "acacabbbccbbacacabacacabacacaccbabbacacabac"
    pattern = "acacabacacabacacac"
    print (has_substring(main_string, pattern))
    # print (create_prefix_array(pattern))
