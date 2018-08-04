# Exercise begins on line 87
import pygame
import sys
import random

SCREEN_SIZE = WIDTH, HEIGHT = (800, 640)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
SCORE_LIMIT = 5

pygame.init()
font = pygame.font.SysFont('arial', 100)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
paused = False
game_over = False
hit_paddle = False
hit_top_wall = False
hit_bottom_wall = False
player_scored = False
opponent_scored = False
pressed_up = False
pressed_down = False

# Store player and ball data in dicts
ball = {
        'x': 0,
        'y': 0,
        'colour': GREEN,
        'radius': 10,
        'velocity': {
            'x': 3,
            'y': 3
            },
        'original_velocity': {
            'x': 3,
            'y': 3
            }
        }

player = {
        'x': 0,
        'y': 0,
        'colour': WHITE,
        'width': 10,
        'height': 80,
        'velocity': {
            'x': 4,
            'y': 4
            },
        'score': {
            'value': 0,
            'x': 80,
            'y': 30
            }
        }

opponent = {
        'x': 0,
        'y': 0,
        'colour': WHITE,
        'width': 10,
        'height': 80,
        'velocity': {
            'x': 4,
            'y': 4
            },
        'score': {
            'value': 0,
            'x': WIDTH - 150,
            'y': 30
            }
        }

def perform_updates():
    global hit_paddle
    global hit_top_wall
    global hit_bottom_wall
    global player_scored
    global opponent_scored
    global pressed_down
    global pressed_up

    # Class exercise: code the conditions below

    # 1) The boolean variable hit_paddle tells you if the ball hit a paddle.
    #    If the ball hit a paddle, make the ball bounce by calling the 
    #    function ball_paddle_bounce() and reset hit_paddle.
 



    # 2) The boolean variabls hit_top_wall and hit_bottom_wall tells you
    #    which wall the ball hit, if it hit any.
    #    If the ball hits either wall, call the function ball_wall_bounce()
    #    and reset hit_top_wall and hit_bottom wall.




    # 3) The boolean variable player_scored tells you if the player scored.
    #    If the player scored, call the function player_score_add()
    #    and reset player_scored




    # 4) The boolean variable opponent_scored tells you if the opponent scored.
    #    If the opponent scored, call the function opponent_score_add()
    #    and reset opponent_scored




    # 5) The boolean variable pressed_up tells you if the player pressed the up key.
    #    If the player pressed the up key, call the function go_up()
    #    and reset pressed_up
    
    

    # 6) The boolean variable pressed_down tells you if the player pressed the down key.
    #    If the player pressed the down key, call the function go_down()
    #    and reset pressed_down





def ball_init():
    ball['x'] = (WIDTH // 2) - ball['radius']
    ball['y'] = (HEIGHT // 2) - ball['radius']
    ball['velocity']['x'] = ball['original_velocity']['x'] * random.choice([-1, 1])
    ball['velocity']['y'] = ball['velocity']['y'] * random.choice([-1, 1])
    pygame.time.wait(1000)


def player_init():
    player['x'] = 10
    player['y'] = (HEIGHT // 2) - (player['height'] // 2)


def opponent_init():
    opponent['x'] = WIDTH - 10 - player['width']
    opponent['y'] = (HEIGHT // 2) - (player['height'] // 2)


def init():
    ball_init()
    player_init()
    opponent_init()


def within_y_range(paddle, ball):
    return paddle['y'] <= ball['y'] <= paddle['y'] + paddle['height']

def ball_paddle_bounce():
    ball['velocity']['x'] *= -1.2

def ball_wall_bounce():
    ball['velocity']['y'] *= -1

def player_score_add():
    player['score']['value'] += 1

def opponent_score_add():
    opponent['score']['value'] += 1

def ball_update():
    # Check collision first
    # Hit a paddle?
    global hit_paddle
    global hit_top_wall
    global hit_bottom_wall
    global player_scored
    global opponent_scored
    if ((ball['x'] - ball['radius'] <= player['x'] + player['width'] 
            and within_y_range(player, ball))
            or (ball['x'] + ball['radius'] >= opponent['x'] 
                and within_y_range(opponent, ball))):
        hit_paddle = True
    # Hit the top or bottom?
    if ball['y'] - ball['radius'] <= 0:
        hit_top_wall = True
    if ball['y'] + ball['radius'] >= HEIGHT:
        hit_bottom_wall = True

    perform_updates()
    ball['x'] += int(ball['velocity']['x'])
    ball['y'] += int(ball['velocity']['y'])

    # Otherwise check for scoring
    if ball['x'] - ball['radius'] <= player['x']:
        opponent_scored = True
        ball_init()
    elif ball['x'] + ball['radius'] >= opponent['x'] + opponent['width']:
        player_scored = True
        ball_init()
    perform_updates()

def go_up():
    player['y'] -= player['velocity']['y']

def go_down():
    player['y'] += player['velocity']['y']

def player_update(key_presses):
    global pressed_down
    global pressed_up

    if player['y'] >= 0:
        if key_presses[pygame.K_w] or key_presses[pygame.K_UP]:
            pressed_up = True
    if player['y'] + player['height'] <= HEIGHT:
        if key_presses[pygame.K_s] or key_presses[pygame.K_DOWN]:
            pressed_down = True
    perform_updates()


def opponent_update():
    if ball['x'] >= WIDTH // 2:
        if ball['y'] < opponent['y'] and opponent['y'] >= 0:
            opponent['y'] -= opponent['velocity']['y']
        elif (ball['y'] > opponent['y'] 
                and (opponent['y'] + opponent['height']) <= HEIGHT):
            opponent['y'] += opponent['velocity']['y']
    else:
        if opponent['y'] < HEIGHT // 2:
            opponent['y'] += opponent['velocity']['y']
        else:
            opponent['y'] -= opponent['velocity']['y']


def update(key_presses):
    ball_update()
    player_update(key_presses)
    opponent_update()


def render():
    screen.fill(BLACK)
    # Draw score
    player_score = font.render(str(player['score']['value']), True, WHITE)
    opponent_score = font.render(str(opponent['score']['value']), True, WHITE)
    screen.blit(player_score, (player['score']['x'], player['score']['y']))
    screen.blit(opponent_score, (opponent['score']['x'], opponent['score']['y']))
    # Draw ball
    pygame.draw.circle(screen, ball['colour'], (ball['x'], ball['y']),
            ball['radius'])
    # Draw players
    pygame.draw.rect(screen, player['colour'], ((player['x'], player['y']),
        (player['width'], player['height'])))
    pygame.draw.rect(screen, opponent['colour'], ((opponent['x'], opponent['y']),
        (opponent['width'], opponent['height'])))
    if game_over:
        game_over_score = font.render('Game Over', True, BLUE)
        screen.blit(game_over_score, ((WIDTH // 2) - 275, (HEIGHT // 2) - 200))
    pygame.display.update()
    clock.tick(60)


def check_game_over():
    return (player['score']['value'] == SCORE_LIMIT or
            opponent['score']['value'] == SCORE_LIMIT)


# Setup game before loop starts
init()

# Start game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                paused = not paused

    if not paused and not game_over:
        game_over = check_game_over()
        if not game_over:
            update(pygame.key.get_pressed())
        render()
