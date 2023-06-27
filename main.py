import pygame


class Sprite:
    image = pygame.image.load('assets/_18ad30aa-4300-440f-b75d-b576125147b2.jpg')
    speed = 5
    x = 100
    y = 100

    def move(self, side):
        if side == 'left':
            self.x -= self.speed
        elif side == 'right':
            self.x += self.speed


w = pygame.display.set_mode((1279, 700))
Player = Sprite()

game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Player.move('right')
    elif keys[pygame.K_LEFT]:
        Player.move('left')
    w.fill((0, 0, 0))
    w.blit(Player.image, (Player.x, Player.y))
    pygame.display.update()

pygame.quit()
