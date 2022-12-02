# Advent of Code 2022 - day 2 --- anthorne

game_rounds = open("day2_input.txt", "r")

player_total_score = 0
points_win = 6
points_draw = 3
points_lose = 0

shapes = [["a", "rock", 1], ["b", "paper", 2], ["c", "scissors", 3],
          ["x", "rock", 1], ["y", "paper", 2], ["z", "scissors", 3]]


def get_shape(sign, shapes):
    shape = ""
    points = 0
    for s in shapes:
        if s[0] == sign:
            shape = s[1]
            points = s[2]
    return shape, points


def check_win(o, p):
    if p[0] == o[0]:
        return "draw", 3
    if (p[0] == "rock" and o[0] == "paper") or \
            (p[0] == "scissors" and o[0] == "rock") or \
            (p[0] == "paper" and o[0] == "scissors"):
        return "lose", 0

    if (p[0] == "rock" and o[0] == "scissors") or \
            (p[0] == "paper" and o[0] == "rock") or \
            (p[0] == "scissors" and o[0] == "paper"):
        return "win", 6


for r in game_rounds:
    opponent = r.split(" ")[0].lower().strip()
    player = r.split(" ")[1].lower().strip()
    o = get_shape(opponent, shapes)
    p = get_shape(player, shapes)
    player_total_score += p[1]
    game, points = check_win(o, p)
    player_total_score += points
    # print("Round - opponent plays " + o[0] + " and you play " + p[0] + " - Game: " +
    #      game + " - Total score: " + str(player_total_score))
print("\n - Part one - What would your total score be if everything goes exactly according to your strategy guide?")
print("            Answer: " + str(player_total_score) + "\n")
game_rounds.close()


# - Part Two -

game_rounds = open("day2_input.txt", "r")
player_total_score = 0


def get_strategy(s):
    if s == "x":
        return "lose", 0
    if s == "y":
        return "draw", 3
    if s == "z":
        return "win", 6


def get_play(o, s):
    if s[0] == "draw":
        return o[0]
    if s[0] == "lose":
        if o[0] == "rock":
            return "scissors"
        if o[0] == "paper":
            return "rock"
        if o[0] == "scissors":
            return "paper"
    if s[0] == "win":
        if o[0] == "rock":
            return "paper"
        if o[0] == "paper":
            return "scissors"
        if o[0] == "scissors":
            return "rock"


def get_score(p):
    if p == "rock":
        return 1
    if p == "paper":
        return 2
    if p == "scissors":
        return 3


for r in game_rounds:
    opponent = r.split(" ")[0].lower().strip()
    strategy = r.split(" ")[1].lower().strip()
    o = get_shape(opponent, shapes)
    s = get_strategy(strategy)
    p = get_play(o, s)
    player_total_score += s[1]
    player_total_score += get_score(p)
    #print("Your opponent plays " + o[0] + " and your strategy is: " + s[0] + " you play: " +
    #      str(p) + " \t- total score: " + str(player_total_score))
print(" - Part two - What would your total score be if everything goes exactly according to your strategy guide?")
print("            Answer: " + str(player_total_score))
