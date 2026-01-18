# others
def weak_point(matrix):
    n = len(matrix)
    row = min(range(n), key=lambda r:sum(matrix[r][c] for c in range(n)))
    col = min(range(n), key=lambda c:sum(matrix[r][c] for r in range(n)))
    return row, col

def weak_point(matrix):
    rows, cols = map(sum, matrix), map(sum, zip(*matrix))
    return rows.index(min(rows)), cols.index(min(cols))
