import pygame
import planet_defination
import sys

pygame.init()

pygame.display.set_caption("Planets")

click = False

def MainMenu():
    run = True

    while run:
                
        mousex, mousey = pygame.mouse.get_pos()

        planet_defination.screen.fill((0,0,0)) # clears screen

        buttonrect1 = pygame.Rect(100,planet_defination.S_HEIGHT/2-100,170,50)
        buttonrect2 = pygame.Rect(100,planet_defination.S_HEIGHT/2,170,50)
        buttonrect3 = pygame.Rect(100,planet_defination.S_HEIGHT/2+100,170,50)

        pygame.draw.rect(planet_defination.screen,(100,120,255),buttonrect1) 
        pygame.draw.rect(planet_defination.screen,(100,120,255),buttonrect2)
        pygame.draw.rect(planet_defination.screen,(100,120,255),buttonrect3)

        planet_defination.Text("Accurate Model",(buttonrect1[0] + buttonrect1[2]/2,buttonrect1[1] + buttonrect1[3]/2),False,30,True)
        planet_defination.Text("Display Model",(buttonrect2[0] + buttonrect2[2]/2,buttonrect2[1] + buttonrect2[3]/2),False,30,True)
        planet_defination.Text("Exit",(buttonrect3[0] + buttonrect3[2]/2,buttonrect3[1] + buttonrect3[3]/2),False,30,True)

        if buttonrect1.collidepoint((mousex,mousey)):
            pygame.draw.rect(planet_defination.screen,(255,255,255),buttonrect1,3) 
            if click:
                PlanetAccurate()
        if buttonrect2.collidepoint((mousex,mousey)):
            pygame.draw.rect(planet_defination.screen,(255,255,255),buttonrect2,3)
            if click:
                PlanetDisplay()
        if buttonrect3.collidepoint((mousex,mousey)):
            pygame.draw.rect(planet_defination.screen,(255,255,255),buttonrect3,3)
            if click:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update() # update screen

        pygame.time.Clock().tick(60) # restrict framerate

def PlanetAccurate():
    
    run = True
    planet_defination.current = 0
    planet = planet_defination.A_ITERATE[planet_defination.current]
    planet_defination.center = [planet_defination.S_WIDTH/2,planet_defination.S_HEIGHT/2]

    while run:

        planet_defination.screen.fill((0,0,0)) # clears screen
        
        # Draws Different Planets
        if planet.name == "AsteriodBelt":
            if planet.distance == 2.2 * planet_defination.DISTANCE:
                pygame.draw.circle(planet_defination.screen, planet_defination.A_ITERATE[planet_defination.current+1].color, planet_defination.center, planet_defination.A_ITERATE[planet_defination.current+1].distance)
            pygame.draw.circle(planet_defination.screen, planet.color, planet_defination.center, planet.distance)
        else:
            pygame.draw.circle(planet_defination.screen, planet_defination.orbitcolor, planet_defination.center, planet.distance,1)
        if planet.name != "AsteriodBelt":
            pygame.draw.circle(planet_defination.screen, planet.color, planet.Revolution(planet.distance, 0, 0), planet.radius)

        # Display name of planets
        planet_defination.Text(planet.name,(planet_defination.S_WIDTH-200,planet_defination.S_HEIGHT-100),True,35,False)
        # Display distance travelled
        planet_defination.Text(f"Distance Of From Sun: {round(planet.distance)}",(50,planet_defination.S_HEIGHT-100),True,35,False)
        planet_defination.Text(f"Volume of Planet: {round(3.14159*pow(planet.radius,3)*4/3,2)}",(planet_defination.S_WIDTH/2-180,planet_defination.S_HEIGHT-100),True,35,False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_RIGHT:
                    planet_defination.current += 1
                    if planet_defination.current > 10:
                        planet_defination.current = 0
                    planet = planet_defination.A_ITERATE[planet_defination.current]
                    if planet_defination.current == 0:
                        planet_defination.center[0] = planet_defination.S_WIDTH/2
                    else:
                        planet_defination.center[0] = -planet.distance + 1000
                if event.key == pygame.K_LEFT:
                    planet_defination.current -= 1
                    if planet_defination.current < 0:
                        planet_defination.current = 10
                    planet = planet_defination.A_ITERATE[planet_defination.current]
                    if planet_defination.current == 0:
                        planet_defination.center[0] = planet_defination.S_WIDTH/2
                    else:
                        planet_defination.center[0] = -planet.distance + 1000


        pygame.display.update() # update screen

        pygame.time.Clock().tick(60) # restrict framerate

def PlanetDisplay():
    run = True
    planet_defination.center = [planet_defination.S_WIDTH/2,planet_defination.S_HEIGHT/2]

    while run:
        planet_defination.screen.fill((0,0,0)) # clears screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        planet_defination.angle += 1

        for planet in planet_defination.D_ITERATE:
            velocity = 0
            if planet.name != "Sun":
                velocity = planet_defination.RelativeVelocity(planet.Velocity()) * planet_defination.revolutionspeed
            
            if planet.name != "AsteriodBelt":
                pygame.draw.circle(planet_defination.screen,planet_defination.orbitcolor,planet_defination.center,planet.distance,1)
                pygame.draw.circle(planet_defination.screen,planet.color,planet.Revolution(planet.distance,planet_defination.angle,velocity),planet.radius)

            else:
                pygame.draw.circle(planet_defination.screen,planet_defination.orbitcolor,planet_defination.center,planet.distance,planet.radius)

        pygame.display.update() # update screen

        pygame.time.Clock().tick(60) # restrict framerate

MainMenu()


