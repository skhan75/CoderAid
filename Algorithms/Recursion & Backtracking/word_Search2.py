class Solution(object):
    def findWords(self, board, words):
        self.result = []
        t = {}
        for word in words:
            self.insert(word,t)
            print (t)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.solve(board,t,i,j)
        return self.result
    def solve(self,board,d,i,j,s=""):
        if i<0 or j<0 or i>=len(board) or j>=(len(board[0])):
            return
        l = board[i][j]
        if l in d:
            d = d[l]
            s+=l
            if "#" in d and d['#']:
                self.result.append(s)
                d['#'] = 0
            board[i][j] = '*'
            if i+1<len(board) and board[i+1][j] in d :
                self.solve(board,d,i+1,j,s)
            if j+1 < len(board[0]) and board[i][j+1] in d:
                self.solve(board,d,i,j+1,s)
            if i-1>=0 and board[i-1][j] in d :
                self.solve(board,d,i-1,j,s)
            if j-1>=0 and board[i][j-1] in d :
                self.solve(board,d,i,j-1,s)
            board[i][j] = l
    def insert(self, word,t):
        current = t
        print ("CURRENT", current)
        for i in word:
            if i not in current:
                current[i] = {}
                current =current[i]
        current['#']=1
ob = Solution()
print(ob.findWords([["o","a","a","n"],["e","t","e","a"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","tea","rain"]))
