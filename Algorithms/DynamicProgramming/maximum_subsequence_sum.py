def maximum_sum_subsequence(array):

    sum = [e for e in array]
    result_indices = [i for i in range(len(array))]

    for i in range(1, len(array)):
        for j in range(0,i):
            if array[j] < array[i]:
                sum[i] = max(sum[i], sum[j] + array[i])
                result_indices[i] = j

    max_val = max(sum)
    print max_val
    start_index = sum.index(max_val)
    print(result_indices)
    while True:
        print (array[start_index])
        next_index = result_indices[start_index]
        if next_index == start_index:
            break
        start_index = next_index

    return max_val

if __name__ == '__main__':
    sequence = [1, 101, 10, 2, 3, 100, 4]
    assert 111 == maximum_sum_subsequence(sequence)
