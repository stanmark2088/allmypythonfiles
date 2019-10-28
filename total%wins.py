def win_percentage(wins, losses):
    total_percentage_wins = (wins / (wins + losses)) * 100
    return total_percentage_wins


print(win_percentage(5, 5))
print(win_percentage(10, 0))
