def generateParens(n):
    result = []
    addParens( n, n, "")
    # return result


def addParens(openP, closedP, string):
    if openP == 0 and closedP == 0:
        print (string)

    if openP > closedP:
        return

    if openP > 0:
        addParens(openP - 1, closedP, string + "(")

    if closedP > 0:
        addParens(openP, closedP - 1, string + ")")



if __name__ == "__main__":
    n = int(input())
    print(generateParens(n))
