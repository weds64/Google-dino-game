import pygame
pygame.init()

width = 1000
high = 600
window = pygame.display.set_mode((width, high))
clock = pygame.time.Clock()

def game():
    window.fill((255, 255, 255))
    is_game = True  
    while is_game:
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                is_game = False
        pygame.display.update()
        clock.tick(60)


game()