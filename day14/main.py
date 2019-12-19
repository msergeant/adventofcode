from math import ceil
from functools import reduce


class Day14Runner:
    def main(self):
        self.formulas = {}
        with open('./input') as file:
            for line in file.readlines():
                formula, result = line.split("=>")
                denom, key = result.strip().split(" ")
                self.formulas[key] = {'re': {}, 'denom': int(denom)}
                for reactant in formula.strip().split(", "):
                    numer, symbol = reactant.split(" ")
                    self.formulas[key]['re'][symbol] = int(numer)

        part1 = self.total_fuel(1)

        part2 = 4366186

        result = self.total_fuel(part2)

        print("Big?", result / 1000000000000)

        return part1, part2

    def total_fuel(self, units):
        total_cons = {k: v * units
                      for k, v in self.formulas['FUEL']['re'].items()}
        while not self.only_base(total_cons.keys()):
            leftover = total_cons.get('left', {})
            cons = [self.constituents(v, k, leftover)
                    for k, v in total_cons.items()]
            total_cons = reduce(self.combine_constituents, cons, {})

        return sum([self.ore_required(v, k)
                     for k, v in total_cons.items() if k != 'left'])


    def only_base(self, keys):
        return all([k == 'left' or self.is_base(k) for k in keys])

    def constituents(self, num, key, leftover):
        if self.is_base(key):
            return {key: num}

        left = leftover.get(key, 0)
        if left > num:
            leftover[key] -= num
            return {}
        else:
            num -= left
            leftover[key] = 0

        result = {}
        denom = self.formulas[key]['denom']
        batches = ceil(num / denom)
        for k, v in self.formulas[key]['re'].items():
            result[k] = batches * v

        if batches * denom - num > 0:
            result['left'] = {key: batches * denom - num}

        return result

    def combine_constituents(self, a, b):
        keys = set(list(a.keys()) + list(b.keys()))
        result = {}
        for key in keys:
            if key != 'left':
                result[key] = a.get(key, 0) + b.get(key, 0)
            else:
                result['left'] = self.combine_constituents(a.get('left', {}),
                                                           b.get('left', {}))

        return result

    def ore_required(self, num, key):
        denom = self.formulas[key]['denom']
        batches = ceil(num / denom)
        return batches * self.formulas[key]['re']['ORE']

    def is_base(self, key):
        return key == 'left' or 'ORE' in self.formulas[key]['re']


print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % Day14Runner().main())
