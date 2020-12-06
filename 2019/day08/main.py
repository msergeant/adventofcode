import re
from collections import Counter

def main():
    with open('./input') as file:
        raw = file.read()
        layers = re.findall(r'\d{150}', raw)

    min = 26
    min_counter = None
    for layer in layers:
        counts = Counter(layer)
        if counts.get('0') and counts['0'] < min:
            min = counts['0']
            min_counter = counts

    image = layers[-1]
    index = len(layers) - 1
    while index > 0:
        index -= 1
        image = overlay(layers[index], image)

    output_image = '\n'.join(re.findall(r'\d{25}', image))
    output_image = re.sub("0", " ", output_image)

    part1 = min_counter['2'] * min_counter['1']
    return part1, output_image

def overlay(layer1, layer2):
    output = []
    for i in range(len(layer1)):
        if layer1[i] == '2':
            output.append(layer2[i])
        else:
            output.append(layer1[i])

    return ''.join(output)


print("The answer to part 1 is %d\n"
      "The answer to part 2 is \n%s" % main())
