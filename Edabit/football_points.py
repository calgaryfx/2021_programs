def football_points(wins, draws, losses):
    win = 3
    draw = 1
    loss = 0
    return (wins * win) + (draws * draw) + (losses * loss)

points = football_points(3, 4, 2)
print(points)
