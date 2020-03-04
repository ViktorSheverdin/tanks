import pygame
class Bullet():
    def __init__(self, x, y, direction):
        self.vel = 1
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12
        self.color = (100,100,100)
        self.direction = direction
        self.rect = (self.x,self.y,self.width,self.height)
        self.exist()

    def __str__(self):
        return "Speed: %s \n X: %s Y: %s \n Width: %s \n Height: %s \n Color: %s" %(self.vel,self.x,self.y,self.width,self.height,self.color)

    def __repr__(self):
        return "Speed: %s \n X: %s Y: %s \n Width: %s \n Height: %s \n Color: %s" %(self.vel,self.x,self.y,self.width,self.height,self.color)

    def check_for_collision(self,filed_width,filed_height):
        bullet_moves = True
        #if self.x > filed_width-self.vel:
        if self.x > filed_width-self.width:
            bullet_moves = False
        elif self.x <= 1:
            bullet_moves = False
        elif self.y > filed_height-self.height:
            bullet_moves = False
        elif self.y <= 1:
            bullet_moves = False
        # if not bullet_moves:
        #     self.color = (0,200,200)
        print("Checking for collision bullet_moves", bullet_moves)
        return bullet_moves

    def move_bullet(self):
        if self.direction == "EAST":
            self.x -= self.vel
        elif self.direction == "WEST":
            self.x += self.vel
        elif self.direction == "NORTH":
            self.y -= self.vel
        elif self.direction == "SOUTH":
            self.y += self.vel

        self.update()

    def exist(self):
        bullet_moves = True
        while bullet_moves:
            print("Start the loop")
            bullet_moves = self.check_for_collision(500,500)
            self.move_bullet()
            print("Bullet moves. X: %s Y: %s " %(self.x, self.y))
            #self.draw(pygame.display.set_mode((500,500)))

    def draw(self, win):
        pygame.draw.rect(win,self.color, self.rect)
        #pygame.display.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)