def decompress(s, i):
    res = ""
    while i < len(s):
        if s[i] == '(':
            i += 1
            word, i, r = decompress(s, i) # word is the decompressed string in (), r is the number of repetitions
            res += word * r
        elif s[i] == ')':
            if i == len(s) - 1 or s[i + 1] != '{': # in case of strings like "(a(b))" where {} is omitted
                return res, i + 1, 1
            else:
                close = s.find("}", i)
                return res, close + 1, int(s[i + 2: close])
        else:
            res += s[i]
            i += 1
    return res

print (decompress("((x){3}(y){2}z){2}", 0))
