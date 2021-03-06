import pygame
import qolFunctions

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))   #use tuple (width,height)


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,100)
rectColor = green
mouseButtons = [0,0,0]

#text stuff
font = pygame.font.SysFont(None, 25)
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [300, 300])
    #print("in message function")



#pygame.display.update()#updates specific area, empty params forces entire surface update.


pygame.display.set_caption("Space Game")
clock = pygame.time.Clock()
#game loop
gameExit = False

map = qolFunctions.levelCreator("Level1.txt")




def checkEvents(mouseX, mouseY):
    rectColor = (255,255,255)

    #get events, mouse movement, clicks, keyboard etc
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            (mouseX, mouseY) = event.pos
            #print(mouseX,mouseY)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtons[event.button -1] = 1
            print(mouseButtons)
        if event.type == pygame.MOUSEBUTTONUP:
            mouseButtons[event.button -1] = 0
            print(mouseButtons)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:#left arrow key
                message_to_screen("LEFT--ARROW", white)
            if event.key == pygame.K_UP:#left arrow key
                message_to_screen("UP----ARROW", white)
            if event.key == pygame.K_DOWN:#left arrow key
                message_to_screen("DOWN--ARROW", white)
            if event.key == pygame.K_RIGHT:#left arrow key
                message_to_screen("RIGHT-ARROW", white)
            if event.key == pygame.K_q:
                pygame.quit()#closes window

    if mouseButtons[0]:
        rectColor = (255,0,0)
    if mouseButtons[1]:
        rectColor = (0,255,0)
    if mouseButtons[2]:
        rectColor = (0,0,255)

    gameDisplay.fill(rectColor, rect=[mouseX-10,mouseY-10,20,20])# color, rect = [x,y,width height]

    return (mouseX,mouseY)

def loadImage(image):  #######Use this like so: loadImage(picture.png)
    img = pygame.image.load(str(image))
    return img

def drawMap(mymap):
    rectColor = (255,255,255)
    for row in mymap:
        for tile in row:
            if tile.terrain == "path":
                rectColor = (200,200,0)
            if tile.terrain == "wall":
                rectColor = (100,100,120)
            if tile.terrain == "water":
                rectColor = (0,0,120)
            if tile.terrain == "spawn":
                rectColor = green

            gameDisplay.fill(rectColor, rect=[tile.coordinates[0]*65,tile.coordinates[1]*65,64,64])

            if (tile.entity != " "):
                print("tile ",tile.coordinates," contains ", tile.entity)
                ###TODO --- Make this display an image given by the name of the entity eg: NAME.png
                #this might help
                #  https://www.youtube.com/watch?v=P4HGZthhkpg&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=29



x=0
y=0
while not gameExit:

    gameDisplay.fill(black)#essentially wipes bg


    #TODO -- menu, choose to display a menu or the game, drawMap or ?drawStore? or something
    drawMap(map)


    x,y = checkEvents(x,y)
    #TODO -- Use x,y to check for mouse selecting something on the screen, like a square of the map, or some option

    #next frame, this should end the loop
    pygame.display.update()
    clock.tick(60)#30 fps



pygame.quit()#closes window
quit()#quits python program