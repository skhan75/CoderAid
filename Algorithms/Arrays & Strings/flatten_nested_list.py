def flatten_list(arr, res):
    stack = enumerate(arr)

    for i,e in stack:
        if type(e) is list:
            flatten_list(e, res)

        else:
            res.append(e)

# Driver Code
arr = [1, 2, [ 3, 4, 5, [6,7]], [[[8,9],10]] ]
res = []
flatten_list(arr, res)
print (res)
