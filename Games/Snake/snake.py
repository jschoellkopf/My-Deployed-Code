import pygame
import time
import random

pygame.init()

# define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (255,165,0)

width, height = 300,300

game_display = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu',20)

# def print_score(score):
#     text = score_font.render("Score: " + str(score),True,orange)
#     game_display.blit(text,[0,0])


def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display,white,[pixel[0],pixel[1], snake_size, snake_size])

def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1
    pygame.display.set_caption(f"Jonas' First Snake Game - Score: {snake_length-1}")

    target_x = round(random.randrange(0,width-snake_size)/10.0)*10
    target_y = round(random.randrange(0,height-snake_size)/10.0)*10

    last_key = ''
    player_name = ''
    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over", True, red)
            game_display.blit(game_over_message,[width/3, height/3])
            
            # Render the score and ask for the player's name
            score_message = score_font.render("Your score: " + str(snake_length-1), True, white)
            game_display.blit(score_message, [5, height/2])
            
            # Loop until the player enters their name
            name_entered = False
            while not name_entered:
                name_message = message_font.render("Enter your name: " + player_name, True, white)
                game_display.blit(name_message, [5, height/2 + 50])
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            player_name += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            player_name = player_name[:-1]
                        elif event.key == pygame.K_RETURN:
                            name_entered = True
            
                # Update the display to show the changes
                pygame.display.update()
            
            # Show the player's name
            name_message = message_font.render("Your name is: " + player_name, True, white)
            game_display.blit(name_message, [5, height/2 + 50])
            pygame.display.update()

            # print_score(snake_length-1)
            # pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_key != 'right':
                    x_speed = -snake_size
                    y_speed = 0
                    last_key = 'left'
                if event.key == pygame.K_RIGHT and last_key != 'left':
                    x_speed = snake_size
                    y_speed = 0
                    last_key = 'right'
                if event.key == pygame.K_UP and last_key != 'down':
                    x_speed = 0
                    y_speed = -snake_size
                    last_key = 'up'
                if event.key == pygame.K_DOWN and last_key != 'up':
                    x_speed = 0
                    y_speed = snake_size
                    last_key = 'down'
        # if x >= width or x < 0 or y >= height or y < 0:
        # allowing the snake to go through walls
        if x >= width and y > 100 and y < 200:
            x = 0
        elif x >= width and y < 100 or x >= width and y > 200:
            game_close = True
        if x < 0:
            x = width
        if y >= height:
            y = 0
        if y < 0:
            y = height
        

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display,orange, [target_x,target_y,snake_size,snake_size])

        snake_pixels.append([x,y])
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        # print_score(snake_length - 1)
        pygame.display.set_caption(f"Jonas' First Snake Game - Score: {snake_length-1}")

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0,width-snake_size)/10.0)*10
            target_y = round(random.randrange(0,height-snake_size)/10.0)*10
            snake_length += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()