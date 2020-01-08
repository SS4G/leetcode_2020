class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rowLength = len(board)
        colLength = len(board[0])
        rookCord = None
        for r in range(rowLength):
            for c in range(colLength):
                if board[r][c] == 'R':
                    rookCord = (r, c)
        r, c = rookCord
        cnt = 0
        for rx in range(r, -1, -1):
            #print(rx, c)
            if board[rx][c] == 'p':
                cnt+=1
                break
            elif board[rx][c] == 'B':
                break

        for rx in range(r, rowLength, 1):
            if board[rx][c] == 'p':
                cnt+=1
                break
            elif board[rx][c] == 'B':
                break

        for cx in range(c, -1, -1):
            if board[r][cx] == 'p':
                cnt+=1
                break
            elif board[r][cx] == 'B':
                break

        for cx in range(c, colLength, 1):
            if board[r][cx] == 'p':
                cnt+=1
                break
            elif board[r][cx] == 'B':
                break

        return cnt

if __name__ == "__main__":
    s = Solution()
    board = [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
    print(s.numRookCaptures(board))