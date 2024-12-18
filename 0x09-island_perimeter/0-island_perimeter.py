#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a 2D grid.

This module provides a function to determine the perimeter of an island
represented by a 2D grid where 1 represents land and 0 represents water.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    Args:
        grid (list): A 2D list of integers representing land and water.
                     1 represents land, 0 represents water.

    Returns:
        int: The total perimeter of the island.
    """
    # Handle empty grid case
    if not grid or not grid[0]:
        return 0

    # Initialize perimeter
    perimeter = 0

    # Iterate through each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Check if current cell is land
            if grid[row][col] == 1:
                # Check top side
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1

                # Check bottom side
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

                # Check left side
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                # Check right side
                if col == len(grid[0]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
