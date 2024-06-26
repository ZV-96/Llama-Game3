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
    jump_y = 0
    jumping = False

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not jumping:
                    jumping = True
                    jump_y = -15

        if jumping:
            jump_y += 1
            llama_y += jump_y
            if jump_y > 50:
                jump_y = 0
            if llama_y >= 130:
                llama_y = 130
                jumping = False

        white = (255, 255, 255)
        screen.fill(white)
        screen.blit(llama, (llama_x, llama_y))
        pygame.display.update()
        clock.tick(30)


# Main Routine
main()