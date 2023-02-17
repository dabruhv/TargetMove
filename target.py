import pygame


haha=True

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Target")

class Target:
    def __init__(self,xpos,ypos,Vx):
        self.xpos = xpos
        self.ypos = ypos
        self.Vx = Vx
    def TDraw(self):
        pygame.draw.circle(screen, (250,0,0), (self.xpos, self.ypos),50)
        pygame.draw.circle(screen, (255,255,255), (self.xpos, self.ypos),40)
        pygame.draw.circle(screen, (0,0,250), (self.xpos, self.ypos),30)
        pygame.draw.circle(screen, (255,255,255), (self.xpos, self.ypos),20)
        pygame.draw.circle(screen, (250,0,0), (self.xpos, self.ypos),10)
    def move(self):
        self.xpos += self.Vx
        if self.xpos >= 800 or self.xpos <= 0:
            self.Vx *= -1
        


def targetScore(lvl):
    if lvl ==1:
        return 50
    elif lvl == 2:
        return 40
    elif lvl == 3:
        return 30
    elif lvl == 4:
        return 20
    elif lvl == 5:
        return 10
    
    
#num = int(input("what was your level(1-5)"))

#print("your score is: ",targetScore(num))

rick = Target(500,700,2)
bob = Target(100,300,1)
lukas = Target(700,500,-3)

while haha:
    
    
    rick.move()
    bob.move()
    lukas.move()
    



#render-----------------------------------------------
    screen.fill((0,0,0))

    rick.TDraw()
    bob.TDraw()
    lukas.TDraw()

    pygame.display.flip()
