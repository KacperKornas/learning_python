import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

WHITE = (255, 255, 255)
YELLOW = (255, 210, 0)
GREEN = (34, 139, 34)
RED = (190, 30, 3)
GREY = (80, 80, 80)
CREAM = (247, 229, 148)
BEIGE = (214, 166, 125)
ORANGE = (201, 87, 17, 255)
THE_COLOR_OF_OLD_CRACOW_PIGEON = (128, 163, 169)
BLUE = (52, 76, 201)

FONT = pygame.font.SysFont("Comicsans", 20)


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 12 / AU  # 1AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun / 1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x + distance_text.get_width() / 4, y + distance_text.get_height() / 4))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


def zoom_in(scale_factor):
    Planet.SCALE *= scale_factor


def zoom_out(scale_factor):
    Planet.SCALE /= scale_factor


def main():
    run = True
    clock = pygame.time.Clock()
    fps = 60
    scale_factor = 1.1

    sun = Planet(0, 0, 7.5, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    mercury = Planet(-0.387 * Planet.AU, 0, 2, GREY, 3.30 * 10 ** 23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(-0.723 * Planet.AU, 0, 3.5, CREAM, 4.8685 * 10 ** 24)
    venus.y_vel = -35.02 * 1000

    earth = Planet(-1 * Planet.AU, 0, 4, GREEN, 5.9742 * 10 ** 24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 3, RED, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    jupiter = Planet(5.2 * Planet.AU, 0, 44, BEIGE, 1.898 * 10 ** 27)
    jupiter.y_vel = 13.06 * 1000

    saturn = Planet(9.5 * Planet.AU, 0, 36, ORANGE, 5.683 * 10 ** 26)
    saturn.y_vel = 9.65 * 1000

    uranus = Planet(19.2 * Planet.AU, 0, 15, THE_COLOR_OF_OLD_CRACOW_PIGEON, 8.681 * 10 ** 25)
    uranus.y_vel = 6.8 * 1000

    neptune = Planet(30 * Planet.AU, 0, 15, BLUE, 1.024 * 10 ** 26)
    neptune.y_vel = 5.4 * 1000

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    while run:
        clock.tick(fps)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll Up
                    zoom_in(scale_factor)
                elif event.button == 5:  # Scroll Down
                    zoom_out(scale_factor)

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()
