# Advent of Code 2022 - day 11 --- anthorne
from math import floor

# input_file = 'day11_input-example.txt'
input_file = 'day11_input.txt'


class Monkey:
    def __init__(self, monkey_id):
        self.monkey_id = int(monkey_id)
        self.items = []
        self.current_item = -1
        self.operation = ''
        self.test_divisible_by = -1
        self.test_true = -1
        self.test_false = -1
        self.inspect_counter = 0

    def play_item(self, mode, divisor_product):
        # inspect item
        self.inspect_item(mode)

        # worry level calculation
        calc_mode = self.operation.split(' ')[3]
        calc_value = self.operation.split(' ')[4]
        if calc_value == 'old':
            calc_value = self.current_item
        else:
            calc_value = int(calc_value)
        calc_text = ''
        if calc_mode == '*':
            calc_text = 'multiplied by ' + str(calc_value)
            self.current_item = self.current_item * calc_value
        elif calc_mode == '+':
            calc_text = 'increased by ' + str(calc_value)
            self.current_item = self.current_item + calc_value
        if mode == 'part_one':
            print('    Worry level is ' + calc_text + ' to ' + str(self.current_item) + '.')

        # relief
        self.relief(mode, divisor_product)

        # test and throw item to monkey
        if self.current_item % self.test_divisible_by == 0:
            if mode == 'part_one':
                print('    Current worry level is divisible by ' + str(self.test_divisible_by) + '.')
            to_monkey = self.test_true
        else:
            if mode == 'part_one':
                print('    Current worry level is not divisible by ' + str(self.test_divisible_by) + '.')
            to_monkey = self.test_false
        if mode == 'part_one':
            print('    Item with worry level ' + str(self.current_item) + ' is thrown to monkey ' + str(to_monkey) + '.')
        return self.current_item, to_monkey

    def inspect_item(self, mode):
        if mode == 'part_one':
            print('  Monkey inspects an item with a worry level of ' + str(self.current_item) + '.')
        self.current_item = self.items.pop(0)
        self.inspect_counter += 1

    def relief(self, mode, divisor_product):
        if mode == 'part_one':
            self.current_item = floor(self.current_item / 3)
            print('    Monkey gets bored with item. Worry level is divided by 3 to ' + str(self.current_item) + '.')
        else:
            self.current_item %= divisor_product

    def catch_item(self, item, mode):
        mode = 'not important here?'
        self.items.append(item)


class KeepAway:
    def __init__(self, part):
        self.monkeys = []
        self.round = 1
        self.part = part
        self.part_one_rounds = 20
        self.part_two_rounds = 10000
        self.part_two_logging = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
        self.divisor_product = 0

    def add_monkey(self, monkey):
        self.monkeys.append(Monkey(monkey))
        return self.monkeys[-1]

    def calc_divisor_product(self):
        for m in self.monkeys:
            if self.divisor_product <= 0:
                self.divisor_product = m.test_divisible_by
            else:
                self.divisor_product *= m.test_divisible_by

    def list_monkeys(self):
        print('\n --- Round ' + str(self.round) + ' completed - statistics ---')
        for m in self.monkeys:
            m_text = '  Monkey ' + str(m.monkey_id) + ' inspected items ' + str(m.inspect_counter) + ' times.'
            if self.part == 'part_one':
                m_text += '\t :'
                items_found = False
                for i in m.items:
                    items_found = True
                    m_text += ' ' + str(i) + ','
                if items_found:
                    m_text = m_text[0:-1]
            print(m_text)

    def part_one_result(self):
        inspections = []
        for m in self.monkeys:
            inspections.append(m.inspect_counter)
        inspections.sort(reverse=True)
        monkey_business = inspections[0] * inspections[1]
        print('\n - Part one - What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?')
        print('            Answer: ' + str(monkey_business))

    def part_two_result(self):
        inspections = []
        for m in self.monkeys:
            inspections.append(m.inspect_counter)
        inspections.sort(reverse=True)
        monkey_business = inspections[0] * inspections[1]
        print('\n - Part two - What is the level of monkey business after 10000 rounds?')
        print('            Answer: ' + str(monkey_business))

    def start_game(self):
        self.calc_divisor_product()
        if self.part == 'part_one':
            rounds = self.part_one_rounds
        else:
            rounds = self.part_two_rounds
        for n in range(rounds):
            self.start_round()
        if self.part == 'part_one':
            self.part_one_result()
        else:
            self.part_two_result()

    def start_round(self):
        if self.part == 'part_one':
            print('\n --- Round ' + str(self.round) + ' --- ')
        for m in self.monkeys:
            if self.part == 'part_one':
                print('Monkey ' + str(m.monkey_id) + ':')
            for i in range(len(m.items)):
                item, to_monkey = m.play_item(self.part, self.divisor_product)
                for m2 in self.monkeys:
                    if m2.monkey_id == to_monkey:
                        if self.part == 'part_one':
                            m2.catch_item(item, 'part_one')
                        else:
                            m2.catch_item(item, 'part_two')
        if self.part == 'part_one':
            self.list_monkeys()
        else:
            for log in self.part_two_logging:
                if self.round == log:
                    self.list_monkeys()
        self.round += 1


def create_game(part):
    # create game object
    game = KeepAway(part)

    # read input data
    monkey_obj = None
    input_data = open(input_file, 'r')
    for r in input_data:
        if r.startswith('Monkey'):
            monkey_obj = game.add_monkey(int(r.split(' ')[1].strip()[0:-1]))
        if r.strip().startswith('Starting items'):
            items = r.split(':')[1].split(',')
            for i in items:
                monkey_obj.catch_item(int(i.strip()), part)
        if r.strip().startswith('Operation'):
            monkey_obj.operation = r.split(':')[1].strip()
        if r.strip().startswith('Test'):
            monkey_obj.test_divisible_by = int(r.strip().split(':')[1].split(' ')[3].strip())
        if r.strip().startswith('If true'):
            monkey_obj.test_true = int(r.strip().split(' ')[5])
        if r.strip().startswith('If false'):
            monkey_obj.test_false = int(r.strip().split(' ')[5])
    input_data.close()
    return game


# let the game begin
game = create_game('part_one')
game.start_game()

game = create_game('part_two')
game.start_game()
