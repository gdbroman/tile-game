import pygame
import random
import math

pygame.init()

screenWidth = 1080
screenHeight = 720
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tile Game")

clock = pygame.time.Clock()


class Tile(object):
    w = 30
    h = 30

    grass_img = pygame.image.load('images/Tiles/grass.png')
    stone_img = pygame.image.load('images/stone.png')
    tree_img = pygame.image.load('images/tree.png')

    def __init__(self, x_n, y_n, off_x, off_y):
        self.x_n = x_n
        self.y_n = y_n
        self.x = x_n * self.w + off_x
        self.y = y_n * self.h + off_y
        self.type = "grass"
        self.objects = {"stone":False, "tree":False}

    def draw(self):
        if self.x < screenWidth and (self.x + self.w) > 0 and self.y < screenHeight and (self.y + self.h) > 0:
            if self.type == "grass":
                win.blit(self.grass_img, (self.x, self.y))

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

    def set_type(self, type):
        self.type = type


class World(object):
    n_tiles_x = 100
    n_tiles_y = 80
    x = n_tiles_x/2*-30
    y = n_tiles_y/2*-30
    tiles = []

    def __init__(self):
        forests = random.randint(5, 10)
        for n in range(self.n_tiles_x):
            for m in range(self.n_tiles_y):
                t = Tile(n, m, self.x, self.y)
                self.tiles.append(t)
                sp = random.randint(1, 100)
                if sp > 98:
                    t.objects["stone"] = True

        for f in range(forests):
            trees = random.randint(20, 30)
            tile_n = random.randint(0, len(self.tiles))
            print(tile_n)
            width = height = int(math.sqrt(trees))
            if tile_n + width > len(self.tiles):
                tile_n -= width
            if tile_n + width * self.n_tiles_x > len(self.tiles):
                tile_n -= width * self.n_tiles_x
            for x in range(width):
                for y in range(height):
                    p = random.randint(0, 10)
                    if p > 8:
                        self.tiles[tile_n+width+width*height].objects["tree"] = True

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

    def zoom(self, scroll_y):
        print(scroll_y)


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
        scroll_y = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4: scroll_y = min(scroll_y + 15, 0)
            if event.button == 5: scroll_y = max(scroll_y - 15, -300)
            the_world.zoom(scroll_y)

        redraw_game_window(the_world)

    pygame.quit()


if __name__ == "__main__":
    world = World()
    game_loop(world)