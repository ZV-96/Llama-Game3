import pygame
import pygame.image

llama = pygame.image.load('Llama.png')
cactus = pygame.image.load('cactus.png')
pygame.init()

screen = pygame.display.set_mode((1000, 200))
pygame.display.set_caption("Llama Game")


def main():
    llama_x = 100
    llama_y = 130
    cactus_x = 1000
    cactus_speed = -10

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        cactus_x += cactus_speed
        if cactus_x < -cactus.get_width():
            cactus_x = 1000
        white = (255, 255, 255)
        screen.fill(white)
        screen.blit(llama, (llama_x, llama_y))
        screen.blit(cactus, (cactus_x, 130))
        pygame.display.update()
        clock.tick(30)


# Main Routine
main()
