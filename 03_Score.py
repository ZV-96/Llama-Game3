import pygame
import pygame.image

llama = pygame.image.load('Llama.png')
cactus = pygame.image.load('cactus.png')
pygame.init()

font = pygame.font.SysFont("arial", 18)
screen = pygame.display.set_mode((1000, 200))
pygame.display.set_caption("Llama Game")


def main():
    llama_x = 100
    llama_y = 130
    cactus_x = 1000
    cactus_speed = -15
    score = 0

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

        score += round(clock.tick(60) / 25)
        score_txt = font.render(f"Score {int(score)}", True, (0, 0, 0))
        screen.blit(score_txt, (450, 10))
        if score % 100 == 0 and cactus_speed <= 13:
            cactus_speed -= 1
        screen.blit(llama, (llama_x, llama_y))
        screen.blit(cactus, (cactus_x, 130))

        pygame.display.update()
        clock.tick(30)


# Main Routine
main()
