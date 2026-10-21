class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for cellR in range(9):
                value = board[row][cellR]
                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)
        for column in range(9):
            seen = set()
            for cellC in range(9):
                value = board[cellC][column]
                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)
        for startRow in range(0,9,3):
            for startCol in range(0,9,3):
                seen = set()
                for r in range(startRow, startRow + 3):
                    for c in range(startCol, startCol + 3):
                        value = board[r][c]
                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)
            return True