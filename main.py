# Working in Ubuntu
# Open a window and simulate a 4 circles with a point moving around them

import pygame
import sys
import math
import random   
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RADIUS = 180
CIRCLE_RADIUS = 60

POINT_RADIUS = 5

# Set up the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Simulation")
clock = pygame.time.Clock()

# Circle class
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.progress = random.randint(0, 360)
        self.speed = random.randint(1, 5)

    def draw(self, win, filled=False):
        # Draw the circle, fill if needed
        pygame.draw.circle(win, BLACK, (self.x, self.y), self.radius, 2)
        if filled:
            pygame.draw.circle(win, BLACK, (self.x, self.y), self.radius)
            
def draw_iteration(win, circles, points, iteration):
    if iteration == 0:
        return
    middle_points = []
    # Draw a line between neighboring points
    for i in range(len(circles)):
        pygame.draw.line(win, BLACK, (points[i].x, points[i].y), (points[(i + 1) % len(circles)].x, points[(i + 1) % len(circles)].y), 2)
    # Add a point in the middle of each line
    for i in range(len(circles)):
        x = (points[i].x + points[(i + 1) % len(circles)].x) // 2
        y = (points[i].y + points[(i + 1) % len(circles)].y) // 2
        middle_points.append(Circle(x, y, POINT_RADIUS))

    draw_iteration(win, circles, middle_points, iteration - 1)
        
# Main loop
def main():
    N = 6
    ITERATIONS = 7 
    # For the amount of N, create N circles which are evenly spaced from the center
    circles = []
    for i in range(N):
        x = WIDTH // 2 + int(RADIUS * math.cos(2 * math.pi * i / N))
        y = HEIGHT // 2 + int(RADIUS * math.sin(2 * math.pi * i / N))
        circles.append(Circle(x, y, CIRCLE_RADIUS))
    
    # for each circle, create a point that moves around the circle
    points = []
    for circle in circles:
        points.append(Circle(circle.x + CIRCLE_RADIUS, circle.y, POINT_RADIUS))
    run = True
    while run:
        win.fill(WHITE)
        for circle in circles:
            circle.draw(win, filled=False)
        for index, point in enumerate(points):
            point.progress += circles[index].speed
            point.x = circles[index].x + int(CIRCLE_RADIUS * math.cos(math.radians(point.progress)))
            point.y = circles[index].y + int(CIRCLE_RADIUS * math.sin(math.radians(point.progress)))
            pygame.draw.circle(win, BLACK, (point.x, point.y), POINT_RADIUS)


        # draw a line between neighboring points
        draw_iteration(win, circles, points, ITERATIONS)

        # Turn on anti aliasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    sys.exit()





if __name__ == "__main__":
    main()
