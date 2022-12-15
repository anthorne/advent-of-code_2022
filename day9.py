# Advent of Code 2022 - day 9 --- anthorne
from math import floor
import pygame
import sys

pygame.init()

DEBUG_MODE = False
SKIP_FIRST_PART = True

# PARAMETERS
if DEBUG_MODE:
    base_grid_size = 30
    base_grid_scale = 40
    expand_grid_before_start = 1       # starts with 5x5 use parameter to further expand before starting
else:
    base_grid_size = 350                # 493
    base_grid_scale = 3
    expand_grid_before_start = 10       # starts with 5x5 use parameter to further expand before starting

# Initial parameters for Pygame
size = width, height = (base_grid_size * base_grid_scale), (base_grid_size * base_grid_scale)
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Advent of Code - Day 9", "Advent of Code")
if DEBUG_MODE:
    FPS = 3
else:
    FPS = 30
fps_clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 10)

grid_width = int(floor(size[0] / base_grid_size))
grid_height = int(floor(size[1] / base_grid_size))
cell_size = grid_width, grid_height

WHITE = pygame.Color(255, 255, 255)
GRAY = pygame.Color(55, 55, 55)
BLACK = pygame.Color(0, 0, 0)
GREEN = pygame.Color(0, 200, 0)
RED = pygame.Color(200, 0, 0)
BLUE = pygame.Color(0, 0, 255)


def get_color(height, c):
    brightness = 100 + (16 * int(height))
    if c == "green":
        color = pygame.Color(0, brightness, 0)
    elif c == "red":
        color = pygame.Color(brightness, 0, 0)
    elif c == "blue":
        color = pygame.Color(0, 0, brightness)
    return color


class Grid:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.grid = self.create_starting_grid()

    def __str__(self):
        for r in self.grid:
            row = ''
            for c in r:
                row += c[0]
            print(row)
        return ''

    def draw_cell(self, r_index, c_index, cell, refresh):
        if DEBUG_MODE:
            print('debug --- r_index: ' + str(r_index) + '   -- c_index: ' + str(c_index) + '   -- cell: ' + str(cell))
            print('debug --- cellsize: ' + str(cell_size))
        if cell[0] == 'H':
            pygame.draw.rect(screen, GREEN,
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T':
            pygame.draw.rect(screen, RED,
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T1':
            pygame.draw.rect(screen, pygame.Color(24, 176, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T2':
            pygame.draw.rect(screen, pygame.Color(46, 154, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T3':
            pygame.draw.rect(screen, pygame.Color(68, 132, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T4':
            pygame.draw.rect(screen, pygame.Color(90, 110, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T5':
            pygame.draw.rect(screen, pygame.Color(112, 88, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T6':
            pygame.draw.rect(screen, pygame.Color(134, 66, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T7':
            pygame.draw.rect(screen, pygame.Color(156, 44, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T8':
            pygame.draw.rect(screen, pygame.Color(178, 22, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 'T9':
            pygame.draw.rect(screen, pygame.Color(200, 0, 0),
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        elif cell[0] == 's':
            pygame.draw.rect(screen, BLUE,
                             (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
        else:
            visited = 0
            for c in cell:
                if type(c) == int:
                    visited = c
            if visited >= 1:
                base_color = 55
                if base_color + (visited * 2) > 255:
                    v_color = pygame.Color(255, 255, 255)
                else:
                    v_color = pygame.Color(base_color + (visited * 2), base_color + (visited * 2), base_color + (visited * 2))
                pygame.draw.rect(screen, v_color,
                                 (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))
            else:
                pygame.draw.rect(screen, GRAY, (((c_index + 1) * cell_size[1]), ((r_index + 1) * cell_size[0]), grid_width, grid_height))

        self.text_surface_obj = font.render("", True, WHITE)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (grid_width / 2, grid_height / 2)
        if refresh:
            screen.blit(self.text_surface_obj, self.text_rect_obj)
            fps_clock.tick(FPS)
            pygame.display.update()

    def draw_full_grid(self):
        r_idx = 0
        c_idx = 0
        for r in self.grid:
            for c in r:
                self.draw_cell(r_idx, c_idx, c, False)
                c_idx += 1
            c_idx = 0
            r_idx += 1
        self.text_surface_obj = font.render("", True, WHITE)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (grid_width / 2, grid_height / 2)
        screen.blit(self.text_surface_obj, self.text_rect_obj)
        fps_clock.tick(FPS)
        pygame.display.update()

    def print_details(self):
        for r in self.grid:
            row = ''
            for c in r:
                col = str(c) + '                '
                row += col[0:18]
            print(row)
        return ''

    def create_starting_grid(self):
        space = [[['.'], ['.'], ['.'], ['.'], ['.']],
                [['.'], ['.'], ['.'], ['.'], ['.']],
                [['.'], ['.'], ['.'], ['.'], ['.']],
                [['.'], ['.'], ['.'], ['.'], ['.']],
                [['.'], ['.'], ['.'], ['.'], ['.']], ]
        if self.puzzle == 'part_one':
            # H: Head   T: Tail  s: Starting point  n: Num of visitations
            space[2][2] = ['H', 'T', 's', 1]
        if self.puzzle == 'part_two':
            # H: Head   Tx: Tail-parts  s: Starting point  n: Num of visitations
            space[2][2] = ['H', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 's', 1]
        return space

    def expand(self, redraw, direction):
        # get grid size (width & height)
        grid_size = len(self.grid[0])
        if DEBUG_MODE:
            print('the grid_size is: ' + str(grid_size))

        # up and down
        new_row = []
        if direction == 'U' or direction == 'D':
            for i in range(grid_size):
                new_row.append(['.'])

        # expand upwards
        if direction == 'U':
            self.grid.insert(0, new_row)

        # expand below
        if direction == 'D':
            self.grid.append(new_row)

        # expand left
        if direction == 'L':
            for row in self.grid:
                row.insert(0, ['.'])

        # expand right
        if direction == 'R':
            for row in self.grid:
                row.append(['.'])

        # redraw grid
        if redraw:
            self.draw_full_grid()

    def get_part(self, part, pop):
        # find the current position and pop the part
        # print(' -- looking for the ' + str(part))
        r_index, c_index = 0, 0
        part_r_index, part_c_index = 0, 0
        found = False
        for r in self.grid:
            for c in r:
                i_index = 0
                for i in range(len(c)):
                    if c[i] == part:
                        part_r_index = r_index
                        part_c_index = c_index
                        if pop:
                            if len(self.grid[r_index][c_index]) > 1:
                                self.grid[r_index][c_index].pop(i_index)
                        # else:
                        #     self.grid[r_index].pop(c_index)
                        # print('popped: ' + str(self.grid[r_index][c_index]))
                        found = True
                        break
                    i_index += 1
                if found:
                    break
                c_index += 1
            if found:
                break
            c_index = 0
            r_index += 1
        return part_r_index, part_c_index

    def move_part(self, part, direction):
        # find the current position and pop the part
        part_r_index, part_c_index = self.get_part(part, pop=True)

        # redraw the popped-part
        self.draw_cell(part_r_index, part_c_index, self.grid[part_r_index][part_c_index], False)

        new_r, new_c = part_r_index, part_c_index

        # add the part to the new position based on direction
        if direction == 'R':
            if len(self.grid[part_r_index]) <= (part_c_index + 1):
                if DEBUG_MODE:
                    print(' EXPANDING THE GRID!')
                self.expand(True, direction)
                # part_r_index += 1
                # part_c_index += 1
            self.grid[part_r_index][part_c_index + 1].insert(0, part)
            new_c += 1

        if direction == 'L':
            if (part_c_index - 1) < 0:
                if DEBUG_MODE:
                    print(' EXPANDING THE GRID!')
                self.expand(True, direction)
                # part_r_index += 1
                part_c_index += 1
            self.grid[part_r_index][part_c_index - 1].insert(0, part)
            new_c -= 1

        if direction == 'D':
            if len(self.grid) <= (part_r_index + 1):
                if DEBUG_MODE:
                    print(' EXPANDING THE GRID!')
                self.expand(True, direction)
                # part_r_index += 1
                # part_c_index += 1
            self.grid[part_r_index + 1][part_c_index].insert(0, part)
            new_r += 1

        if direction == 'U':
            if (part_r_index - 1) < 0:
                if DEBUG_MODE:
                    print(' EXPANDING THE GRID!')
                self.expand(True, direction)
                part_r_index += 1
                # part_c_index += 1
            self.grid[part_r_index - 1][part_c_index].insert(0, part)
            new_r -= 1

        # redraw new position
        self.draw_cell(new_r, new_c, self.grid[new_r][new_c], False)

    def move_tail_parts(self):
        if self.puzzle == 'part_one':
            self.move_tails('H', 'T')
        if self.puzzle == 'part_two':
            self.move_tails('H', 'T1')
            self.move_tails('T1', 'T2')
            self.move_tails('T2', 'T3')
            self.move_tails('T3', 'T4')
            self.move_tails('T4', 'T5')
            self.move_tails('T5', 'T6')
            self.move_tails('T6', 'T7')
            self.move_tails('T7', 'T8')
            self.move_tails('T8', 'T9')

        self.text_surface_obj = font.render("", True, WHITE)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (grid_width / 2, grid_height / 2)
        screen.blit(self.text_surface_obj, self.text_rect_obj)
        fps_clock.tick(FPS)
        pygame.display.update()

    def move_tails(self, h, t):
        head_position = self.get_part(h, pop=False)
        tail_position = self.get_part(t, pop=False)

        # print(' -- head is located: ' + str(head_position) + '  -- tails is located: ' + str(tail_position))
        if (tail_position[0] + 1) < head_position[0] or (tail_position[0] - 1) > head_position[0] or \
                (tail_position[1] + 1) < head_position[1] or (tail_position[1] - 1) > head_position[1]:
            # print(' --- heads too far away..')
            if head_position[0] > tail_position[0]:
                self.move_part(t, 'D')
            if head_position[0] < tail_position[0]:
                self.move_part(t, 'U')
            if head_position[1] > tail_position[1]:
                self.move_part(t, 'R')
            if head_position[1] < tail_position[1]:
                self.move_part(t, 'L')

        new_tails_position = self.get_part(t, pop=False)

        # mark tails visits in the grid - only last part of the snake
        # print(' -- new tails pos: ' + str(new_tails_position))
        # print(' -- grid         : ' + str(self.grid[new_tails_position[0]][new_tails_position[1]]))
        if t == 'T' or t == 'T9':
            found_visited_flag = False
            counter = 0
            for i in self.grid[new_tails_position[0]][new_tails_position[1]]:
                if type(i) == int:
                    found_visited_flag = True
                    self.grid[new_tails_position[0]][new_tails_position[1]][counter] += 1
                counter += 1
            if not found_visited_flag:
                self.grid[new_tails_position[0]][new_tails_position[1]].append(1)

    def count_tails_positions(self):
        tails_visitation_counter = 0
        for r in self.grid:
            for c in r:
                for i in c:
                    if type(i) == int:
                        tails_visitation_counter += 1
        return tails_visitation_counter

    def move(self, direction, distance):
        if DEBUG_MODE:
            print('== ' + str(direction) + ' ' + str(distance) + ' ==')
        for step in range(distance):
            # print('\ndirection: ' + str(direction) + '  step: ' + str(step))

            # Move Head
            self.move_part('H', direction)

            # Move Tails - check if move is needed - more than two steps from the head
            self.move_tail_parts()
            if DEBUG_MODE:
                print(self)
            # self.print_details()


# Count instruction set
if DEBUG_MODE:
    input_file = open('day9_input-example.txt', 'r')
else:
    input_file = open('day9_input.txt', 'r')
num_instructions = 0
for i in input_file:
    num_instructions += 1
input_file.close()
print('Found ' + str(num_instructions) + ' instructions!')



# - Part one -
if not SKIP_FIRST_PART:
    # Set up initial grid
    grid = Grid("part_one")
    if DEBUG_MODE:
        print('== Initial State ==\n')
        print(grid)
    for i in range(expand_grid_before_start):
        grid.expand(False)
    grid.draw_full_grid()

    # Follow instructions
    if DEBUG_MODE:
        puzzle_input = open('day9_input-example.txt', 'r')
    else:
        puzzle_input = open('day9_input.txt', 'r')
    motions = []
    for i in puzzle_input:
        direction = i.split(' ')[0]
        distance = int(i.split(' ')[1].strip())
        motions.append([direction, distance])
    if DEBUG_MODE:
        print(motions)
    current_instruction = 0
    for m in motions:
        grid.move(m[0], m[1])
        progress = (current_instruction / num_instructions) * 100
        current_instruction += 1
        print(' ------- Instruction ' + str(current_instruction) + '/' + str(num_instructions) + '  (' + str(progress)[0:4] + '%) ------- ')


    # Get the answer
    part_one = grid.count_tails_positions()

    print(' - Part one - How many positions does the tail of the rope visit at least once?')
    print('            Answer: ' + str(part_one))


# - Part two -

# Set up initial grid
grid = Grid("part_two")
if DEBUG_MODE:
    print('== Initial State ==\n')
    print(grid)
for i in range(expand_grid_before_start):
    grid.expand(False, 'L')
    grid.expand(False, 'R')
    grid.expand(False, 'U')
    grid.expand(False, 'D')
grid.draw_full_grid()

# Follow instructions
if DEBUG_MODE:
    puzzle_input = open('day9_input-example.txt', 'r')
else:
    puzzle_input = open('day9_input.txt', 'r')
motions = []
for i in puzzle_input:
    direction = i.split(' ')[0]
    distance = int(i.split(' ')[1].strip())
    motions.append([direction, distance])
if DEBUG_MODE:
    print(motions)
current_instruction = 0
for m in motions:
    grid.move(m[0], m[1])
    progress = (current_instruction / num_instructions) * 100
    current_instruction += 1
    print(' ------- Instruction ' + str(current_instruction) + '/' + str(num_instructions) + '  (' + str(
        progress)[0:4] + '%) ------- ')

# Get the answer
part_two = grid.count_tails_positions()

print(' - Part two - How many positions does the tail of the rope visit at least once?')
print('            Answer: ' + str(part_two))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    fps_clock.tick(FPS)

