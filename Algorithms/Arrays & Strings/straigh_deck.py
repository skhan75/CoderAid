import collections

class Solution(object):
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        print count
        while count:
            m = min(count)
            print "m",m, "m+w", m+W
            for k in xrange(m, m+W):
                print 'k',k
                v = count[k]
                print 'V',v
                if not v:
                    print 'here'
                    return False
                if v == 1:
                    print 'ccc',count[k]
                    del count[k]
                    print count
                else:
                    print "reducing", k
                    count[k] = v - 1
            print "\n"

        return True

{
    # 2: 1,
    # 3: 1,
    # 4: 1,
    # 1: 1,
    # 5: 1,
    # 6: 1
}

if __name__ == "__main__":
    hand = [5, 1, 2, 2, 3, 3, 4, 4, 5, 6]
    s = Solution()
    print s.isNStraightHand(hand, 2)
