# Advent of Code 2022 - day 8 --- anthorne
from math import floor
import pygame
import sys

pygame.init()
input_file = "day8_input.txt"

# Initial parameters for Pygame
size = width, height = 1089, 1089
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Advent of Code - Day 8", "Advent of Code")
FPS = 50
fps_clock = pygame.time.Clock()

if input_file == "day8_input-example.txt":
    font = pygame.font.Font(pygame.font.get_default_font(), 100)
else:
    font = pygame.font.Font(pygame.font.get_default_font(), 10)

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
GREEN = pygame.Color(0, 200, 0)
RED = pygame.Color(200, 0, 0)


class Tree:
    def __init__(self, tree_id, height, x, y, offset_top, offset_left):
        self.tree_id = tree_id
        self.height = height
        self.x = x
        self.y = y
        self.offset_top = offset_top
        self.offset_left = offset_left
        self.is_visible = False
        self.scenic_score = 0
        self.has_max_scenic_score = False

    def draw(self):
        if self.is_visible and self.has_max_scenic_score is False:
            pygame.draw.rect(screen, get_color(self.height, "red"), (self.offset_left, self.offset_top, grid_width, grid_height))
        elif self.has_max_scenic_score:
            pygame.draw.rect(screen, get_color(self.height, "blue"), (self.offset_left, self.offset_top, grid_width, grid_height))
        else:
            pygame.draw.rect(screen, get_color(self.height, "green"), (self.offset_left, self.offset_top, grid_width, grid_height))
        self.text_surface_obj = font.render(str(self.height), True, WHITE)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (self.offset_left + (grid_width / 2), self.offset_top + (grid_height / 2))
        screen.blit(self.text_surface_obj, self.text_rect_obj)


class Grid:
    def __init__(self):
        self.trees = []

    def __str__(self):
        row = ""
        for t in self.trees:
            row += str(t.height)
        return row

    def get_max_scenic_score(self):
        max_scenic_score = 0
        tree_object = ''
        for t in self.trees:
            if t.scenic_score > max_scenic_score:
                max_scenic_score = t.scenic_score
                tree_object = t
        tree_object.has_max_scenic_score = True
        tree_object.draw()
        fps_clock.tick(FPS)
        pygame.display.update()
        return max_scenic_score

    def calc_scenic_score(self):
        for t in self.trees:
            l_dist, r_dist, u_dist, d_dist = 0, 0, 0, 0
            # check left
            blocked = False
            for i in range(t.x - 1, -1, -1):
                if blocked:
                    break
                for n in self.trees:
                    if n.x == i and n.y == t.y:
                        if n.height >= t.height:
                            l_dist += 1
                            blocked = True
                            break
                        else:
                            l_dist += 1
            # check right
            blocked = False
            for i in range(t.x + 1, col_counter + 1):
                if blocked:
                    break
                for n in self.trees:
                    if n.x == i and n.y == t.y:
                        if n.height >= t.height:
                            r_dist += 1
                            blocked = True
                            break
                        else:
                            r_dist += 1
            # check up
            blocked = False
            for i in range(t.y - 1, -1, -1):
                if blocked:
                    break
                for n in self.trees:
                    if n.y == i and n.x == t.x:
                        if n.height >= t.height:
                            u_dist += 1
                            blocked = True
                            break
                        else:
                            u_dist += 1
            # check down
            blocked = False
            for i in range(t.y + 1, row_counter + 1):
                if blocked:
                    break
                for n in self.trees:
                    if n.y == i and n.x == t.x:
                        if n.height >= t.height:
                            d_dist += 1
                            blocked = True
                            break
                        else:
                            d_dist += 1
            # set scenic value
            t.scenic_score = l_dist * r_dist * u_dist * d_dist


def get_color(height, c):
    brightness = 100 + (16 * int(height))
    if c == "green":
        color = pygame.Color(0, brightness, 0)
    elif c == "red":
        color = pygame.Color(brightness, 0, 0)
    elif c == "blue":
        color = pygame.Color(0, 0, brightness)
    return color


def count_trees(direction, count_visible):
    if direction == 'left' or direction == 'up':
        i = 0
        iteration = 0
    elif direction == 'right':
        i = col_counter - 1
        iteration = col_counter - 1
    elif direction == 'down':
        i = row_counter * col_counter - 1
        iteration = row_counter * col_counter - 1
    if direction == 'left' or direction == 'right':
        primary_loop = row_counter
        secondary_loop = col_counter
    else:
        primary_loop = col_counter
        secondary_loop = row_counter
    for p in range(primary_loop):
        tallest_tree = -1
        for s in range(secondary_loop):
            t = grid.trees[i]
            if int(t.height) > int(tallest_tree):
                tallest_tree = int(t.height)
                if not t.is_visible:
                    count_visible += 1
                    t.is_visible = True
                    t.draw()
                fps_clock.tick(FPS)
                pygame.display.update()
            if direction == 'left':
                i = i + 1
            elif direction == 'right':
                i = i - 1
            elif direction == 'up':
                i = i + col_counter
            elif direction == 'down':
                i = i - col_counter
        if direction == 'left' or direction == 'right':
            iteration += col_counter
        if direction == 'up':
            iteration += 1
        if direction == 'down':
            iteration -= 1
        i = iteration
    return count_visible


# Get the tree data and calculate stuff
grid_data = open(input_file, "r")
col_counter = 0
row_counter = 0
for line in grid_data:
    row_counter += 1
    if col_counter == 0:
        col_counter = len(line.strip())
grid_width = int(floor(size[0] / row_counter))
grid_height = int(floor(size[1] / col_counter))
cell_size = grid_width, grid_height
grid = Grid()
tree_counter = 0
grid_data = open(input_file, "r")
o_top = 0
o_left = 0
x = 0
y = 0
for row in grid_data:
    y += 1
    for col in row:
        if col.strip() != "":
            x += 1
            if x > col_counter:
                x = 1
            grid.trees.append(Tree(tree_counter, col, x, y, o_top, o_left))
            o_left += grid_width
    o_left = 0
    o_top += grid_height

# Draw the grid
for t in grid.trees:
    t.draw()
fps_clock.tick(FPS)
pygame.display.update()

# - Part one - How many trees are visible from outside the grid?
count_visible = 0
count_visible = count_trees('left', count_visible)
count_visible = count_trees('right', count_visible)
count_visible = count_trees('up', count_visible)
count_visible = count_trees('down', count_visible)

print('- Part one - How many trees are visible from outside the grid?')
print('           Answer: ' + str(count_visible))

# - Part Two -
grid.calc_scenic_score()
part_two = grid.get_max_scenic_score()

print('- Part two - What is the highest scenic score possible for any tree?')
print('           Answer: ' + str(part_two))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    fps_clock.tick(FPS)
