#!/usr/bin/env python3
"""
knights_and_portals.py:
Finds the shortest path in a grid using four-directional moves and a one-time teleportation.
Teleportation can jump between any two empty cells (represented by 0) exactly once.
"""

from collections import deque

def knights_and_portals(grid):
    """
    Computes the minimum number of steps to get from the top-left to bottom-right cell in a grid.
    One teleportation move is available to jump from any empty cell to any other empty cell.
    
    Parameters:
      grid: 2D list where 0 represents an empty cell and nonzero values are obstacles.
      
    Returns:
      Minimum steps required or -1 if a path does not exist.
    """
    rows, cols = len(grid), len(grid[0])
    # visited[x][y][t] where t=0 if teleport not used, t=1 if used.
    visited = [[[False, False] for _ in range(cols)] for _ in range(rows)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Precompute empty cell positions.
    empty_cells = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 0]
    
    q = deque()
    # Start at (0, 0) without having used teleport.
    q.append((0, 0, 0, 0))  # (x, y, teleport_used, steps)
    visited[0][0][0] = True
    
    while q:
        x, y, tele_used, steps = q.popleft()
        if x == rows - 1 and y == cols - 1:
            return steps

        # Regular four-directional moves.
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if not visited[nx][ny][tele_used]:
                    visited[nx][ny][tele_used] = True
                    q.append((nx, ny, tele_used, steps + 1))
        
        # Teleport move (only if not already used).
        if tele_used == 0:
            for ex, ey in empty_cells:
                if ex == x and ey == y:
                    continue
                if not visited[ex][ey][1]:
                    visited[ex][ey][1] = True
                    q.append((ex, ey, 1, steps + 1))
            # Clear to ensure teleportation is only used once.
            empty_cells = []
    return -1


grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]
print("Shortest path steps:", knights_and_portals(grid))

