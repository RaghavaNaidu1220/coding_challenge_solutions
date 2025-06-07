#!/usr/bin/env python3
"""
matrix_islands.py:
Counts the number of islands in a matrix.
An island is composed of adjacent 1s (vertical, horizontal, or diagonal).
"""

def count_islands(matrix):
    """
    Counts the number of islands in a matrix where islands are regions of adjacent 1s 
    (including diagonally adjacent).

    Parameters:
      matrix: 2D list of integers (0s and 1s).

    Returns:
      Integer count of islands.
    """
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(r, c):
        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                           (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and 0 <= ny < cols and
                        not visited[nx][ny] and matrix[nx][ny] == 1):
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                count += 1
    return count


matrix = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1]
]
print("Island count:", count_islands(matrix))

