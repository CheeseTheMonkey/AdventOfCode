
from fractions import gcd
from functools import reduce
from itertools import permutations


class Planet(object):
    def __init__(self, x, y, z):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def apply_x(self, x):
        if isinstance(x, Planet):
            x = x.pos_x
        if self.pos_x < x:
            self.vel_x += 1
        elif self.pos_x > x:
            self.vel_x -= 1

    def apply_y(self, y):
        if isinstance(y, Planet):
            y = y.pos_y
        if self.pos_y < y:
            self.vel_y += 1
        elif self.pos_y > y:
            self.vel_y -= 1

    def apply_z(self, z):
        if isinstance(z, Planet):
            z = z.pos_z
        if self.pos_z < z:
            self.vel_z += 1
        elif self.pos_z > z:
            self.vel_z -= 1

    def apply_gravity(self, planet: 'Planet'):
        self.apply_x(planet.pos_x)
        self.apply_y(planet.pos_y)
        self.apply_z(planet.pos_z)

    def apply_velocity(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z

    def get_potential_energy(self) -> int:
        return abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)

    def get_kinetic_energy(self) -> int:
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    def get_total_energy(self) -> int:
        return self.get_potential_energy() * self.get_kinetic_energy()

def apply_gravity(planets, axis=None):
    for a,b in permutations(planets,2):
        if not axis:
            a.apply_gravity(b)
        else:
            getattr(a, f"apply_{axis}")(b)

    [planet.apply_velocity() for planet in planets]

def lcm(*numbers):
    return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)


if __name__ == '__main__':
    planets = (
        Planet(19, -10, 7),
        Planet(1, 2, -3),
        Planet(14, -4, 1),
        Planet(8, 7, -6)
    )

    for _ in range(1000):
        apply_gravity(planets)

    print("Part 1:", sum((planet.get_total_energy() for planet in planets)))

    planets = (
        Planet(19, -10, 7),
        Planet(1, 2, -3),
        Planet(14, -4, 1),
        Planet(8, 7, -6)
    )
    x_axis = tuple((planet.pos_x, planet.vel_x) for planet in planets)
    y_axis = tuple((planet.pos_y, planet.vel_y) for planet in planets)
    z_axis = tuple((planet.pos_z, planet.vel_z) for planet in planets)

    apply_gravity(planets, 'x')
    x_count = 1
    while tuple((planet.pos_x, planet.vel_x) for planet in planets) != x_axis:
        apply_gravity(planets, 'x')
        x_count += 1

    apply_gravity(planets, 'y')
    y_count = 1
    while tuple((planet.pos_y, planet.vel_y) for planet in planets) != y_axis:
        apply_gravity(planets, 'y')
        y_count += 1

    apply_gravity(planets, 'z')
    z_count = 1
    while tuple((planet.pos_z, planet.vel_z) for planet in planets) != z_axis:
        apply_gravity(planets, 'z')
        z_count += 1

    print(x_count, y_count, z_count)
    print("Part 2:", lcm(x_count, y_count, z_count))
