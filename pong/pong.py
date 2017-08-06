import ugfx
import appglue
from random import randint
from time import sleep

min_width = 5
min_height = 5
max_width = 285
max_height = 100

player_height = 30
player_part_top = 10
player_part_bottom = 20
player_part_middle = 30
player_scored = None  # None, "one", "two"
player_scores = [0, 0]  # Player one score, Player two score
poo = randint(20, 50)   # Player one Y offset
pto = randint(20, 50)  # Player two Y offset

game_clock = 10
game_center = 140

ball_x, ball_y = game_center, 55
ball_direction = ["left", "middle"]  # "left", "right" : "up", "middle", "down"
ball_height = 4

ugfx.init()
ugfx.input_init()


def draw():
    draw_field()
    draw_players()
    draw_info()
    ugfx.flush()


def draw_field():
    ugfx.clear(ugfx.WHITE)
    ugfx.box(min_width, min_height, max_width, max_height, ugfx.BLACK)
    if not player_scored:
        ugfx.line(game_center, min_height, game_center, max_height + 4, ugfx.BLACK)


def draw_info():
    score = "{} : {}".format(*player_scores)
    score_length = ugfx.get_string_width(score, "Roboto_Regular12")
    ugfx.string(game_center - int(score_length / 2), 110, score, "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(5, 110, "[UP/DOWN]", "Roboto_Regular12", ugfx.BLACK)
    ugfx.string(265, 110, "[A/B]", "Roboto_Regular12", ugfx.BLACK)

    if player_scored:
        title = "SCORE!"
        subtitle = "Player {} scored".format(player_scored)
        title_length = ugfx.get_string_width(title, "PermanentMarker36")
        subtitle_length = ugfx.get_string_width(subtitle, "Roboto_BlackItalic24")
        ugfx.string(game_center - int(title_length / 2), 22, title, "PermanentMarker36", ugfx.BLACK)
        ugfx.string(game_center - int(subtitle_length / 2), 62, subtitle, "Roboto_BlackItalic24", ugfx.BLACK)


def draw_players():
    if not player_scored:
        ugfx.thickline(min_width + 10, poo, min_width + 10, poo + player_height, ugfx.BLACK, 3, False)
        ugfx.thickline(max_width - 5, pto, max_width - 5, pto + player_height, ugfx.BLACK, 3, False)
        ugfx.fill_circle(ball_x, ball_y, ball_height, ugfx.BLACK)


def constrain_player(player_location):
    return min(75, max(5, player_location))


def constrain_ball_x(ball_location):
    return min(max_width, max(min_width, ball_location))


def constrain_ball_y(ball_location):
    return min(max_height, max(min_height, ball_location))


def handle_score(player):
    global player_scored, player_scores, ball_direction, ball_x, ball_y, pto, poo
    player_scored = player
    player_scores[["one", "two"].index(player)] += 1

    draw()
    sleep(3)

    player_scored = None
    pto = randint(20, 50)
    poo = randint(20, 50)
    ball_x, ball_y = game_center, randint(45, 55)
    invert_ball_direction()
    ball_direction[1] = "middle"


def invert_ball_direction():
    global ball_direction
    ball_direction[0] = "right" if ball_direction[0] == "left" else "left"


def determine_ball_vertical_direction(player):
    if player <= 14:
        ball_direction[1] = "up"
    elif player in range(14, 17):
        ball_direction[1] = "middle"
    elif player >= 17:
        ball_direction[1] = "down"


def ai_move_players():
    global poo, pto, player_scores
    poo = constrain_player((poo - 5) if bool(randint(0, 1)) else (poo + 5))
    pto = constrain_player((pto - 5) if bool(randint(0, 1)) else (pto + 5))


def ai_move_ball():
    global ball_x, ball_y, ball_direction, player_scored

    # Handle score
    if ball_x <= min_width:
        return handle_score("two")
    elif ball_x >= max_width:
        return handle_score("one")

    # Invert ball on bar hit
    if ball_x in range(max_width - 15, max_width - 5) or ball_x in range(min_width + 15, min_width + 30):
        if ball_direction[0] == "left" and ball_y in range(poo, poo + player_height + 4):
            determine_ball_vertical_direction((ball_y - 2) - poo)
            invert_ball_direction()

        elif ball_direction[0] == "right" and ball_y in range(pto, pto + player_height + 4):
            determine_ball_vertical_direction((ball_y - 2) - pto)
            invert_ball_direction()

    # Bounce ball
    if ball_y <= min_height:
        ball_direction[1] = "down"
    elif ball_y >= max_height:
        ball_direction[1] = "up"

    # Move ball left/right
    if ball_direction[0] == "left":
        ball_x = constrain_ball_x(ball_x - 15)
    else:
        ball_x = constrain_ball_x(ball_x + 15)

    # Move ball up/down/middle
    if ball_direction[1] == "up":
        ball_y = constrain_ball_y(ball_y - 10)

    elif ball_direction[1] == "down":
        ball_y = constrain_ball_y(ball_y + 10)


def player_one_up(pressed):
    global poo
    poo = constrain_player(poo - 5)


def player_one_down(pressed):
    global poo
    poo = constrain_player(poo + 5)


def player_two_up(pressed):
    global pto
    pto = constrain_player(pto - 5)


def player_two_down(pressed):
    global pto
    pto = constrain_player(pto + 5)


ugfx.input_attach(ugfx.BTN_START, lambda p: appglue.home())
ugfx.input_attach(ugfx.JOY_UP, player_one_up)
ugfx.input_attach(ugfx.JOY_DOWN, player_one_down)
ugfx.input_attach(ugfx.BTN_A, player_two_up)
ugfx.input_attach(ugfx.BTN_B, player_two_down)


# Main game loop
# Draws the entire game field & handles I/O
while True:
    draw()
    ai_move_ball()
