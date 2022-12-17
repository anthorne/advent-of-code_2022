# Advent of Code 2022 - day 10 --- anthorne
import pygame
import sys

DEBUG = False
program_file = open('day10_input.txt', 'r')
# program_file = open('day10_input-example.txt', 'r')
# program_file = ["noop", "addx 3", "addx -5"]       # simple test program

program = []
for r in program_file:
    program.append(r)

pygame.init()

# Initial parameters for Pygame
pixel_size = 10
size = width, height = ((pixel_size * 40) + (pixel_size * 2)), ((pixel_size * 6) + (pixel_size * 2))
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Advent of Code - Day 10", "Advent of Code")
FPS = 100
fps_clock = pygame.time.Clock()

font = pygame.font.Font(pygame.font.get_default_font(), 10)

WHITE = pygame.Color(255, 255, 255)
GRAY = pygame.Color(55, 55, 55)
BLACK = pygame.Color(0, 0, 0)
GREEN = pygame.Color(0, 200, 0)
RED = pygame.Color(200, 0, 0)
BLUE = pygame.Color(0, 0, 255)


class Device:
    def __init__(self):
        self.cycle = 1
        self.reg_x = 1
        self.signal_strength = []
        self.signal_counter = 0
        self.crt = CRT()
        if DEBUG:
            print(' CYCLE (start): ' + str(self.cycle))

    def reset(self):
        self.cycle = 1
        self.reg_x = 1
        self.signal_strength = []
        self.signal_counter = 0
        self.crt.reset()

    def __str__(self):
        self.crt.draw(self.cycle, self.reg_x)
        return ''

    def tick(self):
        self.crt.draw(self.cycle, self.reg_x)
        self.crt.pixel_fade()
        if DEBUG:
            print('\t\t\t\t\t\t\t\t\t\t\t REGISTER X: ' + str(self.reg_x))
        if self.cycle > 20:
            self.signal_counter += 1
        if self.cycle == 20 or self.signal_counter == 40:
            self.signal_strength.append(self.cycle * self.reg_x)
            if DEBUG:
                print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t SIGNAL STRENGTH: ' + str(self.signal_strength[-1]))
            self.signal_counter = 0
        if DEBUG:
            print(' CYCLE (end):   ' + str(self.cycle))
        self.cycle += 1
        if DEBUG:
            print(' CYCLE (start): ' + str(self.cycle))

    def addx(self, arg):
        self.tick()
        self.tick()
        self.reg_x += int(arg)

    def noop(self):
        self.tick()


# The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39
class CRT:
    def __init__(self):
        self.sprite_pos = '###.....................................'
        self.pixels = [['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.']]
        self.pixel_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # pygame stuff
        self.text_surface_obj = font.render("", True, WHITE)
        self.text_rect_obj = self.text_surface_obj.get_rect()

    def reset(self):
        self.sprite_pos = '###.....................................'
        self.pixels = [['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], \
                      ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.']]

    def pixel_fade(self):
        p_counter = 0
        fade_value = 1
        for p in self.pixel_values:
            if p > fade_value:
                self.pixel_values[p_counter] = p - fade_value
            else:
                self.pixel_values[p_counter] = 0
            p_counter += 1

    def draw_screen(self):
        r_idx = 0
        c_idx = 0
        for p in self.pixel_values:
            self.draw_cell(r_idx, c_idx, p)
            c_idx += 1
            if c_idx == 40:
                c_idx = 0
                r_idx += 1
        self.text_surface_obj = font.render("", True, WHITE)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (pixel_size / 2, pixel_size / 2)
        screen.blit(self.text_surface_obj, self.text_rect_obj)
        fps_clock.tick(FPS)
        pygame.display.update()

    def draw_cell(self, r_index, c_index, cell):
        pygame.draw.rect(screen, pygame.Color(0, cell, 0), (((c_index + 1) * pixel_size), ((r_index + 1) * pixel_size), pixel_size, pixel_size))
        self.text_surface_obj = font.render("", True, WHITE)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (pixel_size / 2, pixel_size / 2)

    def update_sprite_pos(self, center):
        sprite = ''
        for p in range(40):
            if center - 1 <= p <= center + 1:
                sprite += '#'
            else:
                sprite += '.'
        self.sprite_pos = sprite
        if DEBUG:
            print(' SPRITE POSITION: ' + str(self.sprite_pos))

    # the CRT draws a single pixel during each cycle
    def draw(self, cycle, sprite_center):
        self.update_sprite_pos(sprite_center)
        pos = cycle - 1
        while pos > 39:
            pos = pos - 40
        if self.sprite_pos[pos] == '#':
            self.pixels[cycle - 1] = ['#']
            self.pixel_values[cycle - 1] = 255
        self.print_screen()
        self.draw_screen()

    def print_screen(self):
        line = ''
        horizontal_counter = 0
        for p in self.pixels:
            if horizontal_counter == 40:
                if DEBUG:
                    print(line)
                line = ''
                horizontal_counter = 0
            line += str(p[0])
            horizontal_counter += 1
        if DEBUG:
            print(line)


device = Device()
for instruction in program:
    if DEBUG:
        print('\t\t\t\t\t INSTRUCTION: ' + str(instruction))
    i = instruction.split(' ')
    c = i[0].strip()
    if len(i) > 1:
        a = int(i[1].strip())
    if c == 'noop':
        device.noop()
    if c == 'addx':
        device.addx(a)

part_one = 0
for s in device.signal_strength:
    part_one += s

print('\n - Part one - Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. '
      'What is the sum of these six signal strengths?')
print('            Answer: ' + str(part_one))

# - Part two -

print(' - Part two - Render the image given by your program. What eight capital letters appear on your CRT?')

while True:
    device.reset()
    for instruction in program:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if DEBUG:
            print('\t\t\t\t\t INSTRUCTION: ' + str(instruction))
        i = instruction.split(' ')
        c = i[0].strip()
        if len(i) > 1:
            a = int(i[1].strip())
        if c == 'noop':
            device.noop()
        if c == 'addx':
            device.addx(a)
