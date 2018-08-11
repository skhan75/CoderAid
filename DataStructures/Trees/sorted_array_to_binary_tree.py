class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return '('+str(self.left)+': L ' + "V:" + str(self.value) + " R :" + str(self.right)+')'

def transform_to_binary(array):
    return transformation_util(array, 0, len(array)-1)

def transformation_util(array, left, right):
    if left > right:
        return ''

    mid = (left + right) // 2
    
    root = TreeNode(array[mid])
    root.left = transformation_util(array, left, mid - 1)
    root.right = transformation_util(array, mid + 1, right)
    return root


testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(transform_to_binary(testArray))
