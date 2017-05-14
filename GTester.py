import pygame


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

img = pygame.image.load('myImage.jpg')



#pygame.display.flip()#like a flipbook, next frame
#updates entire surface at once

#pygame.display.update()#updates specific area, empty params forces entire surface update.


pygame.display.set_caption("Slither")

clock = pygame.time.Clock()
#game loop
gameExit = False

while not gameExit:

    gameDisplay.fill(blue)#essentially wipes bg


    #get events, mouse movement, clicks, keyboard etc
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
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



    if mouseButtons[0]:
        rectColor = (255,0,0)
        img = pygame.transform.rotate(img,90)
    if mouseButtons[1]:
        rectColor = (0,255,0)
    if mouseButtons[2]:
        rectColor = (0,0,255)


    #pygame.draw.rect(gameDisplay, black, [400,300,100,200])# where, color, [x,y,width height]

    gameDisplay.blit(img, [mouseX, mouseY])#blit is kinda like draw.anything
    #gameDisplay.fill(rectColor, rect=[mouseX,mouseY,100,20])# color, rect = [x,y,width height]




    #next frame, this should end the loop
    pygame.display.update()
    clock.tick(60)#30 fps



pygame.quit()#closes window
quit()#quits python program