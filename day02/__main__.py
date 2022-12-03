from util import aoc_input


def problem1():
    score = 0
    for line in aoc_input("input.txt"):
        opponent_move, player_move = line.split()
        opponent_move = decode_move(opponent_move)
        player_move = decode_move(player_move)
        score += score_round(opponent_move, player_move)

    return score


def decode_move(move):
    if move == "A" or move == "X":
        return "ROCK"
    elif move == "B" or move == "Y":
        return "PAPER"
    elif move == "C" or move == "Z":
        return "SCISSORS"
    raise ValueError(f"Invalid move: {move}")


def score_move(move):
    if move == "ROCK":
        return 1
    elif move == "PAPER":
        return 2
    elif move == "SCISSORS":
        return 3


def score_round(opponent_move, player_move):
    if opponent_move == player_move:
        return 3 + score_move(player_move)
    if opponent_move == "ROCK":
        if player_move == "PAPER":
            return 6 + score_move(player_move)
    if opponent_move == "PAPER":
        if player_move == "SCISSORS":
            return 6 + score_move(player_move)
    if opponent_move == "SCISSORS":
        if player_move == "ROCK":
            return 6 + score_move(player_move)
    return 0 + score_move(player_move)


def find_move_to_lose(opponent_move):
    if opponent_move == "ROCK":
        return "SCISSORS"
    elif opponent_move == "PAPER":
        return "ROCK"
    elif opponent_move == "SCISSORS":
        return "PAPER"


def find_move_to_draw(opponent_move):
    return opponent_move


def find_move_to_win(opponent_move):
    if opponent_move == "ROCK":
        return "PAPER"
    elif opponent_move == "PAPER":
        return "SCISSORS"
    elif opponent_move == "SCISSORS":
        return "ROCK"


def problem2():
    score = 0
    for line in aoc_input("input.txt"):
        opponent_move, player_move = line.split()
        opponent_move = decode_move(opponent_move)
        if player_move == "X":
            player_move = find_move_to_lose(opponent_move)
        elif player_move == "Y":
            player_move = find_move_to_draw(opponent_move)
        elif player_move == "Z":
            player_move = find_move_to_win(opponent_move)
        score += score_round(opponent_move, player_move)

    return score



print(problem1())
print(problem2())
