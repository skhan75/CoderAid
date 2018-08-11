def replace_silly(s):
    s = s.split(' ')
    s = '%20'.join(s)
    return s

if __name__ == "__main__":
    input = raw_input().strip()
    print replace_silly(input)
