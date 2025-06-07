#!/usr/bin/env python3
"""
sudoku_validator.py:
Validates a complete 9×9 Sudoku board with custom zones.
A custom zone is defined by an accompanying 9×9 grid of integers (e.g., 0 to 8).
"""

def is_valid_sudoku(board, custom_zones):
    """
    Validates a complete 9×9 Sudoku board. In addition to verifying that 
    each row and column contains digits '1'–'9' without repetition, it checks
    that each custom zone (group of 9 cells as defined by custom_zones) also contains
    the digits '1'-'9' uniquely.

    Parameters:
      board: 9×9 list of lists with string digits '1'-'9'
      custom_zones: 9×9 list of lists with integer zone IDs (0 to 8)

    Returns:
      True if the board is valid; otherwise, False.
    """
    n = 9

    # Check each row.
    for i in range(n):
        seen = set()
        for j in range(n):
            value = board[i][j]
            if value in seen:
                return False
            seen.add(value)

    # Check each column.
    for j in range(n):
        seen = set()
        for i in range(n):
            value = board[i][j]
            if value in seen:
                return False
            seen.add(value)

    # Group cells by custom zones.
    zones = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            zone = custom_zones[i][j]
            zones[zone].append(board[i][j])
    # Validate each custom zone has exactly 9 unique digits.
    for zone_entries in zones.values():
        if len(zone_entries) != n or len(set(zone_entries)) != n:
            return False

    return True


# A valid Sudoku board sample.
valid_board = [
    ['5','3','4','6','7','8','9','1','2'],
    ['6','7','2','1','9','5','3','4','8'],
    ['1','9','8','3','4','2','5','6','7'],
    ['8','5','9','7','6','1','4','2','3'],
    ['4','2','6','8','5','3','7','9','1'],
    ['7','1','3','9','2','4','8','5','6'],
    ['9','6','1','5','3','7','2','8','4'],
    ['2','8','7','4','1','9','6','3','5'],
    ['3','4','5','2','8','6','1','7','9']
]
# Standard custom zones (3×3 blocks).
custom_zones = [
    [0,0,0,1,1,1,2,2,2],
    [0,0,0,1,1,1,2,2,2],
    [0,0,0,1,1,1,2,2,2],
    [3,3,3,4,4,4,5,5,5],
    [3,3,3,4,4,4,5,5,5],
    [3,3,3,4,4,4,5,5,5],
    [6,6,6,7,7,7,8,8,8],
    [6,6,6,7,7,7,8,8,8],
    [6,6,6,7,7,7,8,8,8]
]
print("Testing valid sudoku:", is_valid_sudoku(valid_board, custom_zones))

# Introduce a duplicate in zone 0 to create an invalid board.
invalid_board = [row[:] for row in valid_board]
invalid_board[0][0] = '9'  # Duplicate '9' in the first custom zone.
print("Testing invalid sudoku:", is_valid_sudoku(invalid_board, custom_zones))

