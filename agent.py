from constants import TILESIZE

# Agents follow a set path given in route and act as lightsources. The light 
# seen in-game is the tiles in range and in LoS of the agent.
class Agent:
    def __init__(self, route, color, speed=1, range=1):
        self.route = route
        self.speed = int(speed)
        self.color = color
        self.currInstr = 1
        self.range = int(range)

        # Spawn agent at first coordinate
        self.x = route[0][0] * TILESIZE
        self.y = route[0][1] * TILESIZE

        # Mode towards second coordinate
        self.goalX = route[1][0] * TILESIZE
        self.goalY = route[1][1] * TILESIZE

    # Track the goa coordinate and get a new one once reached.
    def move(self):
        if self.x < self.goalX:
            self.x += self.speed
        elif self.x > self.goalX:
            self.x -= self.speed

        if self.y < self.goalY:
            self.y += self.speed
        elif self.y > self.goalY:
            self.y -= self.speed

        if abs(self.x - self.goalX) < self.speed:
            self.x = self.goalX

        if abs(self.y - self.goalY) < self.speed:
            self.y = self.goalY

        if self.x == self.goalX and self.y == self.goalY:
            self.currInstr = (self.currInstr + 1) % len(self.route)
            self.goalX = self.route[self.currInstr][0] * TILESIZE
            self.goalY = self.route[self.currInstr][1] * TILESIZE
