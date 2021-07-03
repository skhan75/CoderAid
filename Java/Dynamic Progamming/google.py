

def google1(input):
    d = dict()
    d["hello"] = sorted("hello")
    d["he"] = sorted("he")
    d["to"] = sorted("to")
    d["the"] = sorted("the")
    d["word"] = sorted("word")

    start = 0
    s = ""
    for i in range(1, len(input) + 1):
        for k,v in d.items():
            if(sorted(input[start:i]) == v):
                s = s + k + " "
                start = i
    print(s)
google1("elhloothtedrowl")