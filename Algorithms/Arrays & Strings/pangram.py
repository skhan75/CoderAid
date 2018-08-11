# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPangram(sen):
    chars = list(sen)
    if len(set(chars)) == 27:
        print "pangram"
    else:
        print "not pangram"


if __name__ == "__main__":
    sen = raw_input().strip().lower()
    isPangram(sen)
