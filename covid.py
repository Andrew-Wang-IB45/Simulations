import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Pick size of the window
SIZE = (800, 600)

# Initialize the window
window = pygame.display.set_mode(SIZE)

# Control the frame rate
FPS = 30
clock = pygame.time.Clock()

class Person:
    def __init__(self, x=10, y=10, infected=False):
        self.infected = infected
        self.rect = pygame.Rect(x, y, 10, 10)

    def distance(self, other_person):
        # Determines the distance between people
        delta_x = self.rect.x - other_person.rect.x
        delta_y = self.rect.y - other_person.rect.y
        distance = (delta_x**2 + delta_y**2)**(1/2)
        return distance

    def infect(self, other_person):
        # Infects other people if person is infected
        if self.infected and self is not other_person:
            if self.distance(other_person) < 40:
                other_person.infected = True

    def draw(self):
        # Draws the person
        if self.infected:
            color = pygame.Color("Red")
        else:
            color = pygame.Color("Green")
        pygame.draw.rect(window, color, self.rect)

    def move(self):
        # Move the person
        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)
        
        # Bounds person to move within window
        self.rect.left = max(self.rect.left, 0)
        self.rect.top = max(self.rect.top, 0)
        self.rect.right = min(self.rect.right, SIZE[0])
        self.rect.bottom = min(self.rect.bottom, SIZE[1])

persons = []
for i in range(100):
    persons.append(Person(random.randint(100, 700), random.randint(100, 500)))

persons.append(Person(400, 300, infected=True))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Refresh the screen
    window.fill(pygame.Color("Black"))

    for person in persons:
        # Move people
        person.move()

        # Infect people
        if person.infected:
            for other_person in persons:
                person.infect(other_person)

        
        # Draw people
        person.draw()

    # Update the screen
    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)
