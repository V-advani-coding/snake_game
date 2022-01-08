import pygame
import sys,random

pygame.init()

width = 800
height = 800

fps = 10

game_clock =  pygame.time.Clock()

snake_position = [[100,50], [80,50], [60,50]]
snake_head = [100,50] # (x,y)


# food_position = [random.randint(10,width), random.randint(10,height)]
food_position = [random.randrange(0,width,10), random.randrange(0,height,10)]

game_window = pygame.display.set_mode(size = (height,width))

img = pygame.image.load("download.jpeg")

new_img = pygame.transform.scale(img, (height,width))
blue = pygame.Color(0,0,255)
red = pygame.Color(255,0,0)

current_position = 'RIGHT'
change_position = current_position

# Oppoite movement not possible.

score = 0

while True:
    game_window.blit(new_img,(0,0))

    font = pygame.font.SysFont('times new roman', 30)
    surface = font.render(f'Score: {score}',True,red)
    rect = surface.get_rect()
    rect.midtop = (50,20) # Position
    game_window.blit(surface,rect)


    for block in snake_position:
        pygame.draw.rect(game_window,blue,[block[0],block[1],10,10])
    
    pygame.draw.rect(game_window,red,[food_position[0], food_position[1], 10, 10])



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                change_position = 'UP'
            if event.key == ord('a'):
                change_position = 'LEFT'
            if event.key == ord('s'):
                change_position = 'DOWN'
            if event.key == ord('d'):
                change_position = 'RIGHT'

    if change_position == 'UP':
        snake_head[1] -= 10
    elif change_position == 'DOWN':
        snake_head[1] += 10
    elif change_position == 'RIGHT':
        snake_head[0] += 10
    elif change_position == 'LEFT':
        snake_head[0] -= 10
    
    snake_position.append(list(snake_head))


    if snake_head[0] == food_position[0] and snake_head[1] == food_position[1]:
        food_position = [random.randrange(0,width,10), random.randrange(0,height,10)]
        score += 1
        print(score)
    else:
        snake_position.pop(0)

    if snake_head[0] < 0 or snake_head[0] > width:
        pygame.quit()
        sys.exit()

    if snake_head[1] < 0 or snake_head[1] > height:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    game_clock.tick(fps)


