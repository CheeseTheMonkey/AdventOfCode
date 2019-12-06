


def build_map(orbits):
    smap = {}
    for orbit in orbits:
        p,s = orbit.split(')')
        smap[s] = p
    return smap


def count_all_orbits(smap):
    orbits = 0
    for v in smap.values():
        orbits += 1
        while v in smap:
            v = smap[v]
            orbits += 1

    return orbits

def get_path_to_COM(smap, start):
    path = []
    while start in smap:
        start = smap[start]
        path.append(start)

    return path

if __name__ == '__main__':
    orbits = [a.strip() for a in open("day6.input").readlines()]
    smap = build_map(orbits)
    print("Part 1:", count_all_orbits(smap))

    santa = get_path_to_COM(smap, "SAN")
    you = get_path_to_COM(smap, "YOU")

    for i, planet in enumerate(you):
        if planet in santa:
            break

    print("Part 2:", i + santa.index(planet))
