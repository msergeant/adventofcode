class Orbiter:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    def orbit_count(self):
        if self.parent:
            return 1 + self.parent.orbit_count()
        else:
            return 0

    def __str__(self):
        return f"{self.name}"


def main():
    graph = {}
    with open('./input') as file:
        for i in file.readlines():
            orbit = i.strip()
            codes = orbit.split(')')

            graph[codes[0]] = graph.get(codes[0]) or Orbiter(codes[0])
            graph[codes[1]] = graph.get(codes[1]) or Orbiter(codes[1])

            parent = graph[codes[0]]
            child = graph[codes[1]]

            parent.add_child(child)
            child.set_parent(parent)

    part1 = sum(orb.orbit_count() for (_, orb) in graph.items())

    return part1, -1

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())
