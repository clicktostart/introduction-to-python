import pygame
import sys
import os

# Class Exercise: Variables

# Create and assign variables as required below. Experiment with the values to see how the results change.

#  1. Declare a variable called SCREEN_WIDTH and give it an integer value of 800.
SCREEN_WIDTH = 800

#  2. Declare a variable called SCREEN_HEIGHT and give it an integer value of 640.
SCREEN_HEIGHT = 640

#  3. Declare a variable called TITLE and give it a string value of your choice. The window name will be what you choose.
TITLE = 'Tic Tac Toe'

#  4. Declare a variable called P1 and assign the character that you would like to see as player 1.
P1 = 'X'

#  5. Declare a variable called P2 and assign the character that you would like to see as player 2.
P2 = 'O'

#  6. Declare a variable called C1 and assign a list of 3 integers between 0 and 255 inclusive to choose colour 1 for the game.
C1 = [0, 0, 0]

#  7. Declare a variable called C2 and assign a list of 3 integers between 0 and 255 inclusive to choose colour 2 for the game.
C2 = [255, 255, 255]

#  8. Declare a variable called C3 and assign a list of 3 integers between 0 and 255 inclusive to choose colour 3 for the game.
C3 = [50, 255, 50]

#  9. Declare a variable called C4 and assign a list of 3 integers between 0 and 255 inclusive to choose colour 4 for the game.
C4 = [50, 50, 255]

# 10. Declare a variable called C5 and assign a list of 3 integers between 0 and 255 inclusive to choose colour 5 for the game.
C5 = [255, 50, 50]


# SDL is the library which Pygame uses
# We use SDL to put the game window at the screen's centre
os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)
BLACK = C1  #(0, 0, 0)
WHITE = C2  #(255, 255, 255)
GREEN = C3  #(50, 255, 50)
BLUE  = C4  #(50, 50, 255)
RED   = C5  #(255, 50, 50)
REPLAY_MESSAGE = 'Press space to play again'

pygame.init()
board_font = pygame.font.SysFont('arial', 80)
game_over_font = pygame.font.SysFont('monospace', 80, bold=True)
replay_font = pygame.font.SysFont('monospace', 50)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

def draw_lines(screen, screen_size):
    # Draw vertical lines
    # Lines go from top of screen to bottom of screen
    vertical_line_1 = int(screen_size[0] / 3) # lines mark 1/3 of the board
    pygame.draw.line(screen, BLACK, (vertical_line_1, 0), (vertical_line_1, screen_size[0]), 4)
    vertical_line_2 = vertical_line_1 * 2
    pygame.draw.line(screen, BLACK, (vertical_line_2, 0), (vertical_line_2, screen_size[0]), 4)
    # Draw horizontal lines
    horizontal_line_1 = int(screen_size[1] / 3)
    pygame.draw.line(screen, BLACK, (0, horizontal_line_1), (screen_size[0], horizontal_line_1), 4)
    horizontal_line_2 = horizontal_line_1 * 2
    pygame.draw.line(screen, BLACK, (0, horizontal_line_2), (screen_size[0], horizontal_line_2), 4)


def draw_letter(screen, letter, colour, position_rect):
    player_choice = board_font.render(letter, False, colour)
    # Fonts are draw to the top left of a Pygame rectangle
    # This game would look better if they're drawn to the centre
    # So after we generate a font image, create a special rectangle
    # that's the center of the cell's rectangle. So the image will
    # appear in the centre
    choice_rect = player_choice.get_rect(center=position_rect.center)
    # Blit is Pygame's way of drawing an image to a rectangle
    screen.blit(player_choice, choice_rect)


def initialise_board(screen_size):
    board = []
    counter = 1
    # First add 3 lists
    for i in range(3):
        board.append([])

    # Then we calculate the width and height of each cell
    # We want each cell to have an even amount of space
    rect_width = int(screen_size[0] / 3)
    rect_height = int(screen_size[1] / 3)
    # Now we have a list of lists, each list item will have a place to play
    # Outer list with contains each row
    top = 0
    for i in range(3):
        left = 0
        # Inner list which has 3 cells per row
        for j in range(3):
            board[i].append({
                'played': False,
                'player': str(counter), # Could be X or O, shows numbers by default
                'rect': pygame.Rect(left, top, rect_width, rect_height)
            })
            # Add more to the left values so cells don't overlap
            left += rect_width
            # Increment counter so that it goes up to 9
            counter += 1
        # Ensure that the top values are increased for every row
        top += rect_height
    return board


def winner(board, player):
    # Check win by row
    for row in board:
        if (row[0]['player'] == player and row[1]['player'] == player and
                row[2]['player'] == player):
            return True

    # Check win by column
    for i in range(3):
        if (board[0][i]['player'] == player and board[1][i]['player'] == player and
                board[2][i]['player'] == player):
            return True

    # Check diagonals
    if (board[0][0]['player'] == player and board[1][1]['player'] == player and
        board[2][2]['player'] == player):
        return True

    if (board[0][2]['player'] == player and board[1][1]['player'] == player and
        board[2][0]['player'] == player):
        return True

    return False


def is_stalemate(board):
    return all([all([r['played'] for r in row]) for row in board])


def update(game, keys_pressed):
    someone_played = False
    if ((keys_pressed[pygame.K_1] or keys_pressed[pygame.K_KP1])
            and not game['board'][0][0]['played']):
        game['board'][0][0]['played'] = True
        game['board'][0][0]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pygame.K_2] or keys_pressed[pygame.K_KP2])
            and not game['board'][0][1]['played']):
        game['board'][0][1]['played'] = True
        game['board'][0][1]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pygame.K_3] or keys_pressed[pygame.K_KP3])
            and not game['board'][0][2]['played']):
        game['board'][0][2]['played'] = True
        game['board'][0][2]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pygame.K_4] or keys_pressed[pygame.K_KP4])
            and not game['board'][1][0]['played']):
        game['board'][1][0]['played'] = True
        game['board'][1][0]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pygame.K_5] or keys_pressed[pygame.K_KP5])
            and not game['board'][1][1]['played']):
        game['board'][1][1]['played'] = True
        game['board'][1][1]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pygame.K_6] or keys_pressed[pygame.K_KP6])
            and not game['board'][1][2]['played']):
        game['board'][1][2]['played'] = True
        game['board'][1][2]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pygame.K_7] or keys_pressed[pygame.K_KP7])
            and not game['board'][2][0]['played']):
        game['board'][2][0]['played'] = True
        game['board'][2][0]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pygame.K_8] or keys_pressed[pygame.K_KP8])
            and not game['board'][2][1]['played']):
        game['board'][2][1]['played'] = True
        game['board'][2][1]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pygame.K_9] or keys_pressed[pygame.K_KP9])
            and not game['board'][2][2]['played']):
        game['board'][2][2]['played'] = True
        game['board'][2][2]['player'] = game['player']
        someone_played = True

    return someone_played


def end_game_message(screen, screen_size, main_message, main_font,
        replay_message, replay_font, colour):
    main_text = main_font.render(main_message, False, colour)
    main_rect = main_text.get_rect(center=(screen_size[0]/2, screen_size[1]/2))
    screen.blit(main_text, main_rect)
    replay_text = replay_font.render(replay_message, False, colour)
    replay_rect = replay_text.get_rect(center=(screen_size[0]/2,
        main_rect.bottom + 30))
    screen.blit(replay_text, replay_rect)


def render(screen, screen_size, game, clock):
    screen.fill(WHITE)
    draw_lines(screen, screen_size)

    # Draw the letters if they're played
    for row in game['board']:
        for cell in row:
            if cell['player'] == P1:
                draw_letter(screen, P1, BLUE, cell['rect'])
            elif cell['player'] == P2:
                draw_letter(screen, P2, GREEN, cell['rect'])
            else:
                draw_letter(screen, cell['player'], BLACK, cell['rect'])

    if game['win']:
        win_message = 'Player ' + game['player'] + ' won!'
        end_game_message(screen, SCREEN_SIZE, win_message, game_over_font,
                REPLAY_MESSAGE, replay_font, RED)
    elif not game['win'] and game['stalemate']:
        stale_message = 'Stalemate!'
        end_game_message(screen, SCREEN_SIZE, stale_message, game_over_font,
                REPLAY_MESSAGE, replay_font, RED)

    pygame.display.update()
    clock.tick(60)


def main():
    def initialise():
        return {
                'board': initialise_board(SCREEN_SIZE),
                'player':  P1,
                'win': False,
                'stalemate': False,
                'change_player': False
                }

    game = initialise()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()
        if not (game['win'] or game['stalemate']):
            game['change_player'] = update(game, keys_pressed)
        else:
            # Reset the game by pressing space bar
            if keys_pressed[pygame.K_SPACE]:
                game = initialise()

        game['win'] = winner(game['board'], game['player'])
        game['stalemate'] = is_stalemate(game['board'])

        render(screen, SCREEN_SIZE, game, clock)

        # Well if the last move didn't win/end the game, switch to the other player
        if game['change_player'] and not (game['win'] or game['stalemate']):
            if game['player'] == P1:
                game['player'] = P2
            else:
                game['player'] = P1

if __name__ == '__main__':
    main()