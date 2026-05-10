class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for r in range(9):
            for c in range(9):
                value=board[r][c]
                row_key = ("row", r, value)
                col_key = ("col", c, value)
                box_key = ("box", r//3, c//3, value)
                if value==".":
                    continue
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                else:
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
        return True