import random

COLORS = ['красный',
          'оранжевый',
          'желтый',
          'зеленый',
          'голубой',
          'синий',
          'фиолетовый']

CLASSES = {'figure': 0,
           'circle': 3,
           'rectangle': 4,
           'triangle': 6}

filename = 'big_case'

for i in range(10):
    curr_file = filename + str(i) + '.txt'
    with open(curr_file, 'w', encoding='utf-8') as file:
        for j in range(10000):
            curr_color = random.choice(COLORS)
            curr_class = random.choice(list(CLASSES.keys()))
            curr_values = [random.randint(-100, 100) for _ in range(CLASSES[curr_class])]
            data = [curr_class, curr_color, *list(map(str, curr_values))]
            print(' '.join(data), file=file)
