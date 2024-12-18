def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    
    Args:
    grid (List[List[int]]): A 2D grid where 0 represents water and 1 represents land
    
    Returns:
    int: The perimeter of the island
    """
    # If the grid is empty, return 0
    if not grid or not grid[0]:
        return 0
    
    # Get grid dimensions
    rows = len(grid)
    cols = len(grid[0])
    
    # Variable to store total perimeter
    perimeter = 0
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If current cell is land
            if grid[r][c] == 1:
                # Check adjacent cells (up, down, left, right)
                # Add 1 to perimeter for each water or out-of-bounds side
                
                # Up side
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                
                # Down side
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                
                # Left side
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                
                # Right side
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1
    
    return perimeter
