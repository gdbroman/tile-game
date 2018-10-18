import pygame
import random

pygame.init()

screenWidth = 1080
screenHeight = 720
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tile Game")

clock = pygame.time.Clock()


class Tile(object):
    w = 30
    h = 30

    grass_img = pygame.image.load('Images/Tiles/grass.png')
    stone_img = pygame.image.load('Images/stone.png')
    tree_img = pygame.image.load('Images/tree.png')

    def __init__(self, x_n, y_n, off_x, off_y):
        self.x_n = x_n
        self.y_n = y_n
        self.x = x_n * self.w + off_x
        self.y = y_n * self.h + off_y
        self.objects = {"stone":False, "tree":False}

    def draw(self):
        if self.x < screenWidth and (self.x + self.w) > 0 and self.y < screenHeight and (self.y + self.h) > 0:
            win.blit(self.grass_img, (self.x, self.y))
            #pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.w, self.h), 1)

    def draw_object(self):
        img = self.stone_img
        if self.objects["stone"]:
            pass
        elif self.objects["tree"]:
            img = self.tree_img
        else:
            return
        win.blit(img, (self.x - img.get_size()[0] + 30, self.y- int(img.get_size()[1]) + 30))

    def move(self, off_x, off_y):
        self.x += off_x
        self.y += off_y



class World(object):
    x = 200
    y = 200
    n_tiles_x = 20
    n_tiles_y = 15
    tiles = []

    def __init__(self):
        for n in range(self.n_tiles_x):
            for m in range(self.n_tiles_y):
                t = Tile(n, m, self.x, self.y)
                self.tiles.append(t)
        for t in self.tiles:
            p = random.randint(1, 100)
            if p < 5:
                t.objects["stone"] = True
            elif p < 8:
                t.objects["tree"] = True


    def draw(self):
        for t in self.tiles:
            t.draw()
        for t in self.tiles:
            t.draw_object()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        for t in self.tiles:
            t.move(dx, dy)


def redraw_game_window(the_world):
    win.fill((0, 0, 0))
    the_world.draw()
    pygame.display.flip()
    pygame.display.update()


def game_loop(the_world):
    run = True
    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        mouse_keys = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if mouse_keys[0]:   #Left
            pass
        elif mouse_keys[1]: #Middle
            pass
        elif mouse_keys[2]: #Right
            pass

        if keys[pygame.K_SPACE]:
            pass
        if keys[pygame.K_w]:
            the_world.move(0, -5)
        elif keys[pygame.K_a]:
            the_world.move(-5, 0)
        elif keys[pygame.K_s]:
            the_world.move(0, 5)
        elif keys[pygame.K_d]:
            the_world.move(5, 0)

        redraw_game_window(the_world)

    pygame.quit()


if __name__ == "__main__":
    world = World()
    game_loop(world)