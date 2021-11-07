import figure
import circle
import rectangle
import triangle
import sys

COLORS = ['красный',
          'оранжевый',
          'желтый',
          'зеленый',
          'голубой',
          'синий',
          'фиолетовый']


def read_info(filename='data.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.readlines()
        data = [line.split() for line in data]
    classes = {'figure': figure.Figure,
               'circle': circle.Circle,
               'rectangle': rectangle.Rectangle,
               'triangle': triangle.Triangle}

    output = []
    for line in data:
        if line[0] in classes:
            if line[1] in COLORS:
                temp = classes[line[0]](line[1], *[int(v) for v in line[2:]])
                output.append(temp)
            else:
                print(f"Объект класса с цветом '{line[1]}' недопустим")
        else:
            print(f"Объект класса с названием '{line[0]}' недопустим")
    return output


def write_info(info, data, filename='output.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        print(' '.join(info[1:]), file=file)
        print(f'Кол-во созданных объектов: {len(data)}\nОтсортированные по убыванию объекты:', file=file)
        for line, index in zip(data, range(len(data))):
            print(index + 1, line, file=file)
