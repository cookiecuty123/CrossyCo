import pygame
import random
import math
import time
from pygame import mixer

# initiate
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")
background_2 = pygame.image.load("background2.png")

#Title and icon
pygame.display.set_caption("CrossyCo")
icon = pygame.image.load("virus.png")
pygame.display.set_icon(icon)

# fonts
font = pygame.font.Font("Perfect DOS VGA 437.ttf", 32)
font_title = pygame.font.Font("Perfect DOS VGA 437.ttf", 64)
font_question = pygame.font.Font("Perfect DOS VGA 437.ttf", 25)

# level
level = 1

levelX = 10
levelY = 10

def show_level(x, y):
	level_text = font.render("Level " + str(level), True, (255, 255, 255))
	screen.blit(level_text, (x, y))

# instructions 1
instrX = 380
instrY = 10
instr1 = "Cross the street safely."

# instructions 2
instr2X = 380
instr2Y = 10
instr2 = "Wash your hands."

# instruction 3
instr3 = "Type the correct letter."
instr3X = 380
instr3Y = 10

def show_instr(instruction, x, y):
	instr_text = font.render(instruction, True, (255, 255, 255))
	screen.blit(instr_text, (x, y))

# press space
spaceX = 400
spaceY = 50

def show_space(x, y):
	space_text = font.render("Press SPACE", True, (255, 255, 255))
	screen.blit(space_text, (x, y))

# choices
choices_a = "a. 10 seconds"
choices_b = "b. 30 seconds"
choices_c = "c. 15 seconds"
choices_d = "d. 20 seconds"

choicesX_a = 400
choicesY_a = 280
choicesX_b = 400
choicesY_b = 320
choicesX_c = 400
choicesY_c = 360
choicesX_d = 400
choicesY_d = 400

# answer
false = False

def show_choices(x_a, y_a, x_b, y_b, x_c, y_c, x_d, y_d):
    choices_text_a = font.render(choices_a, True, (255, 255, 255))
    screen.blit(choices_text_a, (x_a, y_a))
    choices_text_b = font.render(choices_b, True, (255, 255, 255))
    screen.blit(choices_text_b, (x_b, y_b))
    choices_text_c = font.render(choices_c, True, (255, 255, 255))
    screen.blit(choices_text_c, (x_c, y_c))
    choices_text_d = font.render(choices_d, True, (255, 255, 255))
    screen.blit(choices_text_d, (x_d, y_d))

# player
playerX = 380
playerY = 500
playerX_change = 5
playerY_change = 5

walk_right = [pygame.image.load("tile015.png"), pygame.image.load("tile017.png"), pygame.image.load("tile018.png")]
walk_left = [pygame.image.load("tile011.png"), pygame.image.load("tile012.png"), pygame.image.load("tile013.png")]
walk_up = [pygame.image.load("tile006.png"), pygame.image.load("tile007.png"), pygame.image.load("tile008.png")]
walk_down = [pygame.image.load("tile001.png"), pygame.image.load("tile002.png"), pygame.image.load("tile003.png")]
idle_right = pygame.image.load("tile016.png")
idle_left = pygame.image.load("tile010.png")
idle_up = pygame.image.load("tile005.png")
idle_down = pygame.image.load("tile000.png")

direction = ""

left = False
right = False
up = False
down = False
walk_count = 0

# pedestrian 1

ped_walk_right_1 = [pygame.image.load("ped000.png"), pygame.image.load("ped001.png"), pygame.image.load("ped002.png")]
ped_walk_left_1 = [pygame.image.load("ped004.png"), pygame.image.load("ped005.png"), pygame.image.load("ped006.png")]

pedX_1 = random.randint(0, 600)
pedY_1 = random.randint(50, 167)
pedX_change_1 = random.randint(7, 10)
pedY_change_1 = random.randint(7, 10)

ped_left_1 = True
ped_right_1 = False

ped_walk_count_1 = 0

ped_direction_1 = ""

# pedestrian 2
ped_walk_right_2 = [pygame.image.load("ped000.png"), pygame.image.load("ped001.png"), pygame.image.load("ped002.png")]
ped_walk_left_2 = [pygame.image.load("ped004.png"), pygame.image.load("ped005.png"), pygame.image.load("ped006.png")]

pedX_2 = random.randint(0, 600)
pedY_2 = random.randint(117, 284)
pedX_change_2 = random.randint(7, 10)
pedY_change_2 = random.randint(7, 10)

ped_left_2 = False
ped_right_2 = True

ped_walk_count_2 = 0

ped_direction_2 = ""

# pedestrian 3
ped_walk_right_3 = [pygame.image.load("ped000.png"), pygame.image.load("ped001.png"), pygame.image.load("ped002.png")]
ped_walk_left_3 = [pygame.image.load("ped004.png"), pygame.image.load("ped005.png"), pygame.image.load("ped006.png")]

pedX_3 = random.randint(0, 600)
pedY_3 = random.randint(284, 400)
pedX_change_3 = random.randint(7, 10)
pedY_change_3 = random.randint(7, 10)

ped_left_3 = True
ped_right_3 = False

ped_walk_count_3 = 0

ped_direction_3 = ""

# clock
clock = pygame.time.Clock()

# question
question = "How long should you minimally wash your hands?"
questX = 60
questY = 200

def show_question(x, y):
    quest_text = font_question.render(question, True, (255, 255, 255))
    screen.blit(quest_text, (x, y))

# animation 1
def redraw_game_window():
    global walk_count
    global direction
    global ped_walk_count
    global ped_direction

    screen.blit(background, (0, 0))

    show_level(levelX, levelY)

    show_instr(instr1, instrX, instrY)

    if playerY <= 50:
        show_space(spaceX, spaceY)

    if walk_count + 1 >= 9:
        walk_count = 0

    if left:
        screen.blit(walk_left[walk_count//3], (playerX, playerY))
        walk_count += 1
        direction = "left"

    elif right:
        screen.blit(walk_right[walk_count//3], (playerX, playerY))
        walk_count += 1
        direction = "right"

    elif up:
        screen.blit(walk_up[walk_count//3], (playerX, playerY))
        walk_count += 1
        direction = "up"

    elif down:
        screen.blit(walk_down[walk_count//3], (playerX, playerY))
        walk_count += 1
        direction = "down"

    else:
        if direction is "down":
            screen.blit(idle_down, (playerX, playerY))
        elif direction is "up":
            screen.blit(idle_up, (playerX, playerY))
        elif direction is "right":
            screen.blit(idle_right, (playerX, playerY))
        elif direction is "left":
            screen.blit(idle_left, (playerX, playerY))
        else:
            screen.blit(idle_down, (playerX, playerY))

    ped_walk_count = 0

    #1
    if ped_left_1:
        screen.blit(ped_walk_left_1[random.randint(0, 2)], (pedX_1, pedY_1))
        ped_walk_count += 1
        ped_direction_1 = "left"

    elif ped_right_1:
        screen.blit(ped_walk_right_1[random.randint(0, 2)], (pedX_1, pedY_1))
        ped_walk_count += 1
        ped_direction_1 = "right"

    #2
    if ped_left_2:
        screen.blit(ped_walk_left_2[random.randint(0, 2)], (pedX_2, pedY_2))
        ped_walk_count += 1
        ped_direction_2 = "left"

    elif ped_right_2:
        screen.blit(ped_walk_right_2[random.randint(0, 2)], (pedX_2, pedY_2))
        ped_walk_count += 1
        ped_direction_2 = "right"

    #3
    if ped_left_3:
        screen.blit(ped_walk_left_3[random.randint(0, 2)], (pedX_3, pedY_3))
        ped_walk_count += 1
        ped_direction_3 = "left"

    elif ped_right_3:
        screen.blit(ped_walk_right_1[random.randint(0, 2)], (pedX_3, pedY_3))
        ped_walk_count += 1
        ped_direction_3 = "right"

    pygame.display.update()

# animation 2
def redraw_game_window_2():
    global walk_count
    global direction
    global ped_walk_count
    global ped_direction

    screen.blit(background_2, (0, 0))

    show_level(levelX, levelY)

    show_instr(instr2, instrX, instrY)

    if playerY <= 50 and playerX <= 300 and playerX >= 100:
        show_space(spaceX, spaceY)

    if walk_count + 1 >= 9:
        walk_count = 0

    if left:
        screen.blit(walk_left[walk_count//3], (playerX, playerY))
        walk_count += 1
        direction = "left"

    elif right:
        screen.blit(walk_right[walk_count//3], (playerX, playerY))
        walk_count += 1
        direction = "right"

    elif up:
        screen.blit(walk_up[walk_count//3], (playerX, playerY))
        walk_count += 1
        direction = "up"

    elif down:
        screen.blit(walk_down[walk_count//3], (playerX, playerY))
        walk_count += 1
        direction = "down"

    else:
        if direction is "down":
            screen.blit(idle_down, (playerX, playerY))
        elif direction is "up":
            screen.blit(idle_up, (playerX, playerY))
        elif direction is "right":
            screen.blit(idle_right, (playerX, playerY))
        elif direction is "left":
            screen.blit(idle_left, (playerX, playerY))
        else:
            screen.blit(idle_down, (playerX, playerY))

    ped_walk_count = 0

    #1
    if ped_left_1:
        screen.blit(ped_walk_left_1[random.randint(0, 2)], (pedX_1, pedY_1))
        ped_walk_count += 1
        ped_direction_1 = "left"

    elif ped_right_1:
        screen.blit(ped_walk_right_1[random.randint(0, 2)], (pedX_1, pedY_1))
        ped_walk_count += 1
        ped_direction_1 = "right"

    #2
    if ped_left_2:
        screen.blit(ped_walk_left_2[random.randint(0, 2)], (pedX_2, pedY_2))
        ped_walk_count += 1
        ped_direction_2 = "left"

    elif ped_right_2:
        screen.blit(ped_walk_right_2[random.randint(0, 2)], (pedX_2, pedY_2))
        ped_walk_count += 1
        ped_direction_2 = "right"

    #3
    if ped_left_3:
        screen.blit(ped_walk_left_3[random.randint(0, 2)], (pedX_3, pedY_3))
        ped_walk_count += 1
        ped_direction_3 = "left"

    elif ped_right_3:
        screen.blit(ped_walk_right_1[random.randint(0, 2)], (pedX_3, pedY_3))
        ped_walk_count += 1
        ped_direction_3 = "right"

    pygame.display.update()

def isCollision(pedX, pedY, playerX, playerY):
    distance = math.sqrt((math.pow(pedX + 40 - playerX, 2)) + (math.pow(pedY + 30 - playerY, 2)))
    if distance < 70:
        return True

# game loop
start = True
running = False
running2 = False
running3 = False

while start:
    screen.fill((0, 0, 0))

    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

        # keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = False
                running = True

    start_text = font_title.render("CrossyCo", True, (255, 255, 255))
    screen.blit(start_text, (250, 100))

    start_text = font.render("Press SPACE to start", True, (255, 255, 255))
    screen.blit(start_text, (240, 270))

    pygame.display.update()

while running:
    clock.tick(18)

    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -5
                left = False
                right = False
                up = True
                down = False
            elif event.key == pygame.K_DOWN:
                playerY_change = 5
                left = False
                right = False
                up = False
                down = True
            elif event.key == pygame.K_LEFT:
                playerX_change = -5
                left = True
                right = False
                up = False
                down = False
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5
                left = False
                right = True
                up = False
                down = False
            elif event.key == pygame.K_SPACE:
                if playerY <= 50:
                    level = 2
                    playerX = 380
                    playerY = 500
                    running = False
                    running2 = True
        else:
            playerX_change = 0
            playerY_change = 0
            left = False
            right = False
            up = False
            down = False
            walk_count = 0

    # player movement
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 535:
        playerY = 536

    # pedestrian movement 1
    pedX_1 += pedX_change_1

    if ped_direction_1 is "left":
        pedX_change_1 = -random.randint(7,10)
    if ped_direction_1 is "right":
        pedX_change_1 = random.randint(7,10)

    if pedX_1 <= 0:
        pedX_1 = 0
        pedX_change_1 = random.randint(7,10)
        pedX_change_1 += pedX_change_1
        ped_direction_1 = "right"
        ped_right_1 = True
        ped_left_1 = False
    elif pedX_1 >= 736:
        pedX_change_1 = -random.randint(7,10)
        pedX_1 = 736
        pedX_1 += pedX_change_1
        ped_direction_1 = "left"
        ped_left_1 = True
        ped_right_1 = False

    # pedestrian movement 2
    pedX_2 += pedX_change_2

    if ped_direction_2 is "left":
        pedX_change_2 = -random.randint(7,10)
    if ped_direction_2 is "right":
        pedX_change_2 = random.randint(7,10)

    if pedX_2 <= 0:
        pedX_2 = 0
        pedX_change_2 = random.randint(7,10)
        pedX_change_2 += pedX_change_2
        ped_direction_2 = "right"
        ped_right_2 = True
        ped_left_2 = False
    elif pedX_2 >= 736:
        pedX_change_2 = -random.randint(7,10)
        pedX_2 = 736
        pedX_2 += pedX_change_2
        ped_direction_2 = "left"
        ped_left_2 = True
        ped_right_2 = False

    # pedestrian movement 3
    pedX_3 += pedX_change_3

    if ped_direction_3 is "left":
        pedX_change_3 = -random.randint(7,10)
    if ped_direction_3 is "right":
        pedX_change_3 = random.randint(7,10)

    if pedX_3 <= 0:
        pedX_3 = 0
        pedX_change_3 = random.randint(7,10)
        pedX_change_3 += pedX_change_3
        ped_direction_3 = "right"
        ped_right_3 = True
        ped_left_3 = False
    elif pedX_3 >= 736:
        pedX_change_3 = -random.randint(7,10)
        pedX_3 = 736
        pedX_3 += pedX_change_3
        ped_direction_3 = "left"
        ped_left_3 = True
        ped_right_3 = False

    # collision 1
    collision = isCollision(pedX_1, pedY_1, playerX, playerY)
    if collision:
        playerY = 480

    # collision 2
    collision = isCollision(pedX_2, pedY_2, playerX, playerY)
    if collision:
        playerY = 480

    # collision 3
    collision = isCollision(pedX_3, pedY_3, playerX, playerY)
    if collision:
        playerY = 480


    redraw_game_window()

while running2:
    screen.fill((138, 55, 55))

    show_level(levelX, levelY)

    show_instr(instr3, instr3X, instr3Y)

    show_question(questX, questY)

    show_choices(choicesX_a, choicesY_a, choicesX_b, choicesY_b, choicesX_c, choicesY_c, choicesX_d, choicesY_d)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False

        #keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                level = 3
                screen.blit(pygame.image.load("tick.png"), (380, 50))
                running2 = False
                running3 = True

            elif event.key == pygame.K_b:
                screen.blit(pygame.image.load("wrong.png"), (380, 50))

            elif event.key == pygame.K_c:
                screen.blit(pygame.image.load("wrong.png"), (380, 50))

            elif event.key == pygame.K_a:
                screen.blit(pygame.image.load("wrong.png"), (380, 50))

    pygame.display.update()

while running3:
    clock.tick(18)

    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running3 = False

        # keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -5
                left = False
                right = False
                up = True
                down = False
            elif event.key == pygame.K_DOWN:
                playerY_change = 5
                left = False
                right = False
                up = False
                down = True
            elif event.key == pygame.K_LEFT:
                playerX_change = -5
                left = True
                right = False
                up = False
                down = False
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5
                left = False
                right = True
                up = False
                down = False
            elif event.key == pygame.K_SPACE:
                if playerY <= 50 and playerX <= 300 and playerX >= 100:
                    level = 4
                    running = False
                    running2 = True
                    running3 = False
        else:
            playerX_change = 0
            playerY_change = 0
            left = False
            right = False
            up = False
            down = False
            walk_count = 0

    # player movement
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 535:
        playerY = 536

    # pedestrian movement 1
    pedX_1 += pedX_change_1

    if ped_direction_1 is "left":
        pedX_change_1 = -random.randint(7, 10)
    if ped_direction_1 is "right":
        pedX_change_1 = random.randint(7, 10)

    if pedX_1 <= 0:
        pedX_1 = 0
        pedX_change_1 = random.randint(7, 10)
        pedX_change_1 += pedX_change_1
        ped_direction_1 = "right"
        ped_right_1 = True
        ped_left_1 = False
    elif pedX_1 >= 736:
        pedX_change_1 = -random.randint(7, 10)
        pedX_1 = 736
        pedX_1 += pedX_change_1
        ped_direction_1 = "left"
        ped_left_1 = True
        ped_right_1 = False

    # pedestrian movement 2
    pedX_2 += pedX_change_2

    if ped_direction_2 is "left":
        pedX_change_2 = -random.randint(7, 10)
    if ped_direction_2 is "right":
        pedX_change_2 = random.randint(7, 10)

    if pedX_2 <= 0:
        pedX_2 = 0
        pedX_change_2 = random.randint(7, 10)
        pedX_change_2 += pedX_change_2
        ped_direction_2 = "right"
        ped_right_2 = True
        ped_left_2 = False
    elif pedX_2 >= 736:
        pedX_change_2 = -random.randint(7, 10)
        pedX_2 = 736
        pedX_2 += pedX_change_2
        ped_direction_2 = "left"
        ped_left_2 = True
        ped_right_2 = False

    # pedestrian movement 3
    pedX_3 += pedX_change_3

    if ped_direction_3 is "left":
        pedX_change_3 = -random.randint(7, 10)
    if ped_direction_3 is "right":
        pedX_change_3 = random.randint(7, 10)

    if pedX_3 <= 0:
        pedX_3 = 0
        pedX_change_3 = random.randint(7, 10)
        pedX_change_3 += pedX_change_3
        ped_direction_3 = "right"
        ped_right_3 = True
        ped_left_3 = False
    elif pedX_3 >= 736:
        pedX_change_3 = -random.randint(7, 10)
        pedX_3 = 736
        pedX_3 += pedX_change_3
        ped_direction_3 = "left"
        ped_left_3 = True
        ped_right_3 = False

    # collision 1
    collision = isCollision(pedX_1, pedY_1, playerX, playerY)
    if collision:
        playerY = 480

    # collision 2
    collision = isCollision(pedX_2, pedY_2, playerX, playerY)
    if collision:
        playerY = 480

    # collision 3
    collision = isCollision(pedX_3, pedY_3, playerX, playerY)
    if collision:
        playerY = 480

    redraw_game_window_2()

pygame.quit()