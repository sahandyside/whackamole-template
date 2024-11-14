import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_location = (0,0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] // 32 == mole_location[0] and event.pos[1] // 32 == mole_location[1]:
                        mole_location = (random.randrange(0,20), random.randrange(0,16))
                    # mole_location = (event.pos[0], event.pos[1])

            screen.fill("light green")
            for i in range(0,21):
                pygame.draw.line(screen, "black", (i*32, 0), (i*32, 512), 1)
            for j in range(0,17):
                pygame.draw.line(screen, "black", (0, j*32), (640, j*32), 1)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_location[0] *32, mole_location[1]*32)))


            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
