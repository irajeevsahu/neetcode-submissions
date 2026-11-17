class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                value = board[row][i]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for col in range(9):
            seen = set()
            for i in range(9):
                value = board[i][col]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sq // 3) * 3 + i
                    col = (sq % 3) * 3 + j
                    value = board[row][col]
                    if value == ".":
                        continue
                    if value in seen:
                        return False
                    seen.add(value)
        return True
