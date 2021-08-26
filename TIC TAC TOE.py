import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
RED = (255, 0, 0)
BG_COLOR = (28,170,156)
BOARD_ROWS = 3
BOARD_COLS =3
SQUARE_SIZE = WIDTH//BOARD_COLS
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #length and width of game
pygame.display.set_caption ('TIC TAC TOE')
screen.fill ( BG_COLOR )
LINE_COLOR = (23,145,135)
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (239,231,SQUARE_SIZE)
CROSS_WIDTH = 20
SPACE = 45
CROSS_COLOR = (66,66,66)

#board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
print(board)

def draw_lines():
    #1 horizontal
    pygame.draw.line ( screen,LINE_COLOR, (0,SQUARE_SIZE),(600,SQUARE_SIZE), LINE_WIDTH)
    #2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    #1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, 600), LINE_WIDTH)
    #2 vertical
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_COLOR, ( int( col * SQUARE_SIZE + 100 ), int( row * SQUARE_SIZE + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE ), ( col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE ), CROSS_WIDTH )
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)


def mark_square(row,col,player): #marcar quadrado
    board[row][col] = player

def available_square(row,col): #descobrir se um quadrado esta livre
    if board [row][col] ==0:
        return True
    else:
        return False

def is_board_full():
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row][col] ==0:
                return False
    return True

def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True
    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)

    #desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board [2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col,player):
    posX = col * SQUARE_SIZE + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player ==2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (posX, 15), ( posX, HEIGHT - 15), 15 )

def draw_horizontal_winning_line(row,player):
    posY = row * SQUARE_SIZE + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, posY), (WIDTH -15, posY), 15)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT), (WIDTH - 15, 15 ), 15)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15 ), 15)

def restart():
    screen.fill ( BG_COLOR )
    draw_lines()
    player = 1
    for row in range ( BOARD_ROWS ):
        for col in range ( BOARD_COLS ):
            board[row][col] = 0

draw_lines()
player = 1
game_over = False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            print(clicked_col)
            print(clicked_row)

            if available_square( clicked_row, clicked_col ):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win ( player ):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_square( clicked_row,clicked_col, 2 )
                    if check_win( player ):
                        game_over = True
                    player = 1

                draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()

    pygame.display.update()
             # Basicamente dizendo para fechar somente se clicar no X