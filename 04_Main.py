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
    cactus_x = 1000
    cactus_speed = -10

    run = True
    clock = pygame.time.Clock()
    jumping = False

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

        llama_image = pygame.Rect(llama_x, llama_y, 22, 22)
        cactus_image = pygame.Rect(cactus_x, 130, 22, 22)
        collide = pygame.Rect.colliderect(cactus_image, llama_image)

        if collide:
            quit()

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
