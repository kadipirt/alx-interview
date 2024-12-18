#!/usr/bin/python3
"""
Module for solving the Prime Game problem.

This module provides functions to simulate a game where players
remove prime numbers and their multiples from a set of integers.
"""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def count_primes_helper(n):
    """
    Count the number of primes up to n.

    Args:
        n (int): Upper limit to count primes

    Returns:
        int: Number of prime numbers up to n
    """
    if n <= 1:
        return 0
    
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime_arr[i]:
            # Update all multiples of i
            for j in range(i * i, n + 1, i):
                is_prime_arr[j] = False
    
    # Count primes
    return sum(is_prime_arr)


def play_game(n):
    """
    Simulate a single round of the prime game.

    Args:
        n (int): Upper limit of the set of integers

    Returns:
        str: Winner of the game ('Maria' or 'Ben')
    """
    # Count number of primes
    primes_count = count_primes_helper(n)
    
    # If no primes, Ben wins
    if primes_count == 0:
        return 'Ben'
    
    # Determine winner based on parity of primes
    return 'Maria' if primes_count % 2 == 1 else 'Ben'


def isWinner(x, nums):
    """
    Determine the overall winner across multiple game rounds.

    Args:
        x (int): Number of rounds to play
        nums (list): List of n values for each round

    Returns:
        str: Name of the player with most wins, or 'Maria' or 'Ben'
    """
    # Validate input
    if not isinstance(x, int) or x < 0 or not isinstance(nums, list):
        return None
    
    # Handle edge cases
    if x == 0:
        return None
    
    if x > len(nums):
        nums = nums + [0] * (x - len(nums))
    elif x < len(nums):
        nums = nums[:x]
    
    # Track wins for each player
    maria_wins = 0
    ben_wins = 0
    
    # Play each round
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    
    # If tied, return Ben by default
    return 'Ben'
