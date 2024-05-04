import pygame
import time
import random

pygame.init()

display_width = 1280
display_height = 720
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (165, 42, 42)

car_width = 60

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Lets Race")
clock = pygame.time.Clock()

CarA = pygame.image.load("car1.jpeg")
CarB = pygame.image.load("car2.jpeg")

# def ai_move(x1, y1, x2, y2, thing_startx, thing_starty, thing_speed):
#     # Example AI logic: Move towards the center of the track if far from the obstacle, otherwise try to avoid collision
#     if abs(thing_starty - y1) > 200:
#         if x1 < display_width / 2:
#             return 'right'
#         else:
#             return 'left'
#     else:
#         if abs(x1 - thing_startx) < car_width:
#             if x1 < thing_startx:
#                 return 'right'
#             elif x1 > thing_startx:
#                 return 'left'
#         else:
#             if y1 < thing_starty:
#                 return 'down'
#             else:
#                 return 'up'

def ai_move(x1, y1, x2, y2, thing_startx, thing_starty, thing_speed):
    # Calculate distance between AI car and obstacle
    distance_to_obstacle = abs(x2 - thing_startx)

    # If obstacle is far away, move towards the center of the track
    if distance_to_obstacle > 200:
        if x2 < display_width / 2:
            return 'right'
        else:
            return 'left'
    else:
        # If obstacle is near, check if moving left would avoid collision
        if x2 - thing_speed >= 0:
            return 'left'
        else:
            return 'right'  # Otherwise, move right to avoid collision

# def ai_move(x1, y1, x2, y2, thing_startx, thing_starty, thing_speed):
#     # Calculate distances between AI car and obstacle, and between AI car and player's car
#     distance_to_obstacle = abs(x2 - thing_startx)
#     distance_to_player_horizontal = abs(x2 - x1)
#     distance_to_player_vertical = abs(y2 - y1)

#     # Define safety distance to maintain from the player's car
#     safety_distance = car_width * 2

#     # If the obstacle is far away and there's enough space between the AI car and the player's car, move towards the center of the track
#     if distance_to_obstacle > 200 and distance_to_player_horizontal > safety_distance:
#         if x2 < display_width / 2:
#             return 'right'
#         else:
#             return 'left'
#     else:
#         # If the obstacle is near or the player's car is too close horizontally, try to avoid collision with the player's car
#         if distance_to_player_horizontal < safety_distance:
#             if x2 < x1:  # If AI car is to the left of the player's car, move right
#                 return 'right'
#             elif x2 + car_width + thing_speed > display_width:  # If AI car is blocked from the right, move up
#                 return 'up'
#             else:  # If AI car is to the right of the player's car, move left
#                 return 'left'
#         else:
#             # If the player's car is too close vertically and is positioned above the AI's car, move horizontally away
#             if distance_to_player_vertical < safety_distance and y2 < y1:
#                 if x2 > x1:  # If AI car is to the right of the player's car, move left
#                     return 'left'
#                 else:  # If AI car is to the left of the player's car, move right
#                     return 'right'
#             else:
#                 # If the player's car is too close vertically and is positioned below the AI's car, move up to maintain a safe distance
#                 if distance_to_player_vertical < safety_distance and y2 > y1:
#                     return 'up'
#                 else:
#                     return 'down'  # Otherwise, move down



# def ai_move(x1, y1, x2, y2, thing_startx, thing_starty, thing_speed):
#     # Calculate distances between AI car and obstacle, and between AI car and player's car
#     distance_to_obstacle = abs(x2 - thing_startx)
#     distance_to_player_horizontal = abs(x2 - x1)
#     distance_to_player_vertical = abs(y2 - y1)

#     # Define safety distances to maintain from the player's car and obstacles
#     player_safety_distance = car_width * 3
#     obstacle_safety_distance = car_width * 2

#     # If the obstacle is far away and there's enough space between the AI car and the player's car, move towards the center of the track
#     if distance_to_obstacle > 200 and distance_to_player_horizontal > player_safety_distance:
#         if x2 < display_width / 2:
#             return 'right'
#         else:
#             return 'left'
#     else:
#         # If the player's car is too close horizontally or the obstacle is too close, move away horizontally
#         if distance_to_player_horizontal < player_safety_distance or distance_to_obstacle < obstacle_safety_distance:
#             if x2 < x1:  # If AI car is to the left of the player's car or the obstacle is on the left, move right
#                 return 'right'
#             else:  # If AI car is to the right of the player's car or the obstacle is on the right, move left
#                 return 'left'
#         else:
#             return 'down'  # Otherwise, maintain the current vertical position

def main_menu():
    # Clear the screen
    gameDisplay.fill(white)
    # Display main menu options
    message_display('GAME OVER')



def text_objects(text, font):
    textSurface = font.render(text, True, brown)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 6))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things_dodged(count):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score " + str(count), True, black)
    gameDisplay.blit(text, (20, 20))

def crash(player):
    message_display('Player ' + player + ' Crashed')

def crash3():
    message_display('Collision')

def game_loop():
    background_image = pygame.image.load("background_2.jpg")

    thing_speed = 0
    gameDisplay.fill(white)
    gameDisplay.blit(background_image, (0, 0))
    message_display('1.Easy 2.Medium 3.Hard')
    while thing_speed == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    thing_speed = 4
                elif event.key == pygame.K_2:
                    thing_speed = 9
                elif event.key == pygame.K_3:
                    thing_speed = 14

    y_change = 0
    y2_change = 0

    x = (display_width * 0.48 / 2)
    y = (display_height * 0.79)

    x2 = (display_width * 0.48 * 1.5)
    y2 = (display_height * 0.79)

    x_change = 0
    x2_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_width = 50
    thing_height = 50

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                elif event.key == pygame.K_RIGHT:
                    x_change = 8
                elif event.key == pygame.K_UP:
                    y_change = -8
                elif event.key == pygame.K_DOWN:
                    y_change = 8

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        if y + y_change >= display_height * 0.79:
            y_change = 0
        elif y + y_change <= 0:
            y_change = 0
        y += y_change

        x2 += x2_change
        if y2 + y2_change >= display_height * 0.79:
            y2_change = 0
        elif y2 + y2_change <= 0:
            y2_change = 0
        y2 += y2_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        # Render player-controlled car
        gameDisplay.blit(CarA, (x, y))

        # Render AI-controlled car
        ai_direction = ai_move(x, y, x2, y2, thing_startx, thing_starty, thing_speed)
        if ai_direction == 'left':
            x2_change = -8
        elif ai_direction == 'right':
            x2_change = 8
        elif ai_direction == 'up':
            y2_change = -8
        elif ai_direction == 'down':
            y2_change = 8
        gameDisplay.blit(CarB, (x2, y2))

        things_dodged(dodged)

        # Perform collision detection and other game logic
        # (collision detection logic not provided in the code snippet)
        if ((x + car_width > x2 and x < x2 + car_width) and (y - 125 < y2 and y > y2 - 125)):
            crash3()
            main_menu()
            game_loop()
        if x > display_width - car_width or x < 0:
            crash('1')
            main_menu()
            game_loop()
        if x2 > display_width - car_width or x2 < 0:
            crash('2')
            main_menu()
            game_loop()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            if thing_speed < 20:
                thing_speed += 0.3

        if y < thing_starty + thing_height:
            if ((x > thing_startx and x < thing_startx + thing_width) and (
                    y > thing_starty and y < thing_starty + thing_height)) or (
                    (x + car_width > thing_startx and x + car_width < thing_startx + thing_width) and (
                    y > thing_starty and y < thing_starty + thing_height)):
                crash('1')
                main_menu()
                game_loop()
        if y2 < thing_starty + thing_height:
            if ((x2 > thing_startx and x2 < thing_startx + thing_width) and (
                    y2 > thing_starty and y2 < thing_starty + thing_height)) or (
                    (x2 + car_width > thing_startx and x2 + car_width < thing_startx + thing_width) and (
                    y2 > thing_starty and y2 < thing_starty + thing_height)):
                crash('2')
                main_menu()
                game_loop()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
