#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determine the overall winner across multiple game rounds.

    Args:
        x (int): Number of rounds to play
        nums (list): List of n values for each round

    Returns:
        str or None: Name of the player with most wins, or None if tied
    """
    # Validate input
    if x != len(nums):
        return None

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
    else:
        return None
