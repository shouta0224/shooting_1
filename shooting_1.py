import pygame
import sys

img_bg = pygame.image.load("bg_space.png")
img_chara = [pygame.image.load("ch_bird_1.png"),
             pygame.image.load("ch_bird_2.png"),
             pygame.image.load("ch_bird_1.png")
             ]

def main():
    pygame.init()
    pygame.display.set_caption("シューティング")
    screen = pygame.display.set_mode((1280,960))
    clock = pygame.time.Clock()
    tmr = 0
    ch_x = 565
    ch_y = 810
    speed = 10

    while True:
        tmr = tmr + 1
        pygame.event.pump()
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass
        
        if key[pygame.K_UP]:
            ch_y = ch_y - speed
            if ch_y < 0:
                while ch_y < 0:
                    ch_y = ch_y + 1
        if key[pygame.K_DOWN]:
            ch_y = ch_y + speed
            if ch_y > 810:
                while ch_y > 810:
                    ch_y = ch_y - 1
        if key[pygame.K_RIGHT]:
            ch_x = ch_x + speed
            if ch_x > 1130:
                while ch_x > 1130:
                    ch_x = ch_x - 1
        if key[pygame.K_LEFT]:
            ch_x = ch_x - speed
            if ch_x < 0:
                while ch_x < 0:
                    ch_x = ch_x + 1

        screen.blit(img_bg, [0, 0])
        if tmr%30 < 15:
            screen.blit(img_chara[0], [ch_x, ch_y])
        else:
            screen.blit(img_chara[1], [ch_x, ch_y])
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
