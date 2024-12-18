#!/usr/bin/python3
"""
Module for solving the Coin Change problem.

This module provides a function to determine the minimum number of coins
needed to meet a specific total amount using given coin denominations.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a total amount.

    Args:
        coins (list): List of coin denominations available
        total (int): Target total amount to make change for

    Returns:
        int: Minimum number of coins needed, or -1 if impossible
    """
    # Handle edge cases
    if total <= 0:
        return 0
    
    # Initialize dp array with large value
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins needed to make 0 amount
    dp[0] = 0
    
    # Compute minimum coins for each amount from 1 to total
    for amount in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # Check if coin can be used
            if coin <= amount:
                # Update minimum coins needed
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return result, using -1 if no solution found
    return dp[total] if dp[total] != float('inf') else -1
