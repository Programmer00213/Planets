import pygame
import math

# relative mass is the ratio of mass of planet to mass of sun
# radius is in Meter
# pos_x and pos_y are corrdinates

# note relative distance is the distance between sun and planets in Astronomical units
# it is calculated by (distance between 'X planet' and sun/distance between earth and sun)

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
S_WIDTH, S_HEIGHT = pygame.display.get_surface().get_size()

# Constants
SOLAR_MASS = 1.989*pow(10,30)
ASTRONOMICAL_UNIT = 1.496*pow(10,11)
GRAVITATIONAL_CONSTANT = 6.67*pow(10,-11)
RADIUS = 4.65 * 90 # Radius of Sun
DISTANCE = 1000 * 90 # distance between earth and sun

center = [S_WIDTH/2, S_HEIGHT/2] # center of solar system Sun
revolutionspeed = 0.035
current = 0
angle = 0
orbitcolor = (100,100,100)

class planet:
    def __init__(self,name,radius,distance,color):
        self.name = name
        self.radius = radius
        self.distance = distance
        self.color = color

    def Revolution(self, orbitradius, degree, speed):
        radian = degree * math.pi/180 * speed
        x = center[0] + (orbitradius * math.cos(radian))
        y = center[1] + (orbitradius * math.sin(radian))

        return [x, y]
    
    def Velocity(self):
        velocity = pow((GRAVITATIONAL_CONSTANT * SOLAR_MASS)/(ASTRONOMICAL_UNIT*(self.distance/DISTANCE)),0.5)
        return velocity

A_Sun = planet("Sun",RADIUS,0,(255,0,0))
A_Mercury = planet("Mercury",0.003504 * RADIUS,0.38 * DISTANCE,(255, 255, 255))
A_Venus = planet("Venus",0.008691 * RADIUS,0.72 * DISTANCE,(255, 255, 0))
A_Earth = planet("Earth",0.009149 * RADIUS,1 * DISTANCE,(100,150,255))
A_Mars = planet("Mars",0.004867 * RADIUS,1.52 * DISTANCE,(255,0,0))
A_Jupiter = planet("Jupiter",0.100398 * RADIUS,5.2 * DISTANCE,(255, 165, 0))
A_Saturn = planet("Saturn",0.083625 * RADIUS,9.69 * DISTANCE,(184, 134, 11))
A_Uranus = planet("Uranus",0.036421 * RADIUS,19.19 * DISTANCE,(173, 216, 230))
A_Neptune = planet("Neptune",0.035359 * RADIUS,30.04 * DISTANCE,(0, 0, 255))

A_AsteriodBeltStart = planet("AsteriodBelt",0,2.2 * DISTANCE,(0,0,0))
A_AsteriodBeltEnd = planet("AsteriodBelt",0,3.2 * DISTANCE,orbitcolor)

A_ITERATE = (A_Sun,A_Mercury,A_Venus,A_Earth,A_Mars,A_AsteriodBeltStart,A_AsteriodBeltEnd,A_Jupiter,A_Saturn,A_Uranus,A_Neptune)

D_Sun = planet("Sun",50,0,(255,0,0))
D_Mercury = planet("Mercury", 5, 80, (128, 128, 128))
D_Venus = planet("Venus", 7, 100, (255, 255, 0))
D_Earth = planet("Earth", 10, 125,( 100,150,255))
D_Mars = planet("Mars", 9, 150, (255,0,0))
D_AsteriodBelt = planet("AsteriodBelt",4,175,(0,0,0))
D_Jupiter = planet("Jupiter", 20, 220, (255, 165, 0))
D_Saturn = planet("Saturn", 17, 280, (184, 134, 11))
D_Uranus = planet("Uranus", 12, 350, (173, 216, 230))
D_Neptune = planet("Neptune", 12, 430, (0, 0, 255))

D_ITERATE = (D_Sun,D_Mercury,D_Venus,D_Earth,D_Mars,D_AsteriodBelt,D_Jupiter,D_Saturn,D_Uranus,D_Neptune)

def RelativeVelocity(A_Planet):
    return A_Planet/A_Earth.Velocity()

def Text(text,pos,underline,size,center):
    font = pygame.font.SysFont("Montserrat",size)
    get_text = font.render(text,True,(255,255,255))
    size = get_text.get_size()
    if center == True:
        screen.blit(get_text,(pos[0] - size[0]/2, pos[1] - size[1]/2))
    else:
        screen.blit(get_text,(pos))
    if underline == True:
        if center == True:
            pygame.draw.line(screen,(255,255,255),(pos[0]-10-size[0]/2,pos[1]+size[1]/2),(pos[0]+size[0]/2+10,pos[1]+size[1]/2),5)
        else:
            pygame.draw.line(screen,(255,255,255),(pos[0]-10,pos[1]+size[1]),(pos[0]+size[0]+10,pos[1]+size[1]),5)
