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
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            pygame.display.flip()
            clock.tick(60)
            pygame.draw.line(screen, "green", (0, 0), (512, 640))
            #pygame.draw.line(screen, "black", (0, 0), (640, 640))
            #screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
