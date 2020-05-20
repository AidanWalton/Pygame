#pygame button class
import pygame
pygame.init()
Window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

pgWidth = int(Window.get_width())
pgHeight = int(Window.get_height())

smallText = int(25)
mediumText = int(50)
leftClick = int(0)
#---------------------------------------------------------------------------------------------------------------------------------------
#Pygame colours
"""
Sets the rgb values for the colours used in pygame
"""
pgBlack,pgWhite,pgDarkGrey,pgLightGrey = (0,0,0),(255,255,255),(150,150,150),(211,211,211)
pgRed,pgDarkRed,pgLightRed,pgReallyLightRed = (255,0,0),(150,0,0),(255,100,100),(255,200,200)
pgGreen,pgDarkGreen,pgLightGreen,pgReallyLightGreen = (0,255,0),(0,150,0),(100,255,100),(200,255,200)
pgBlue,pgDarkBlue,pgLightBlue,pgReallyLightBlue = (0,0,255),(0,0,150),(100,100,255),(200,200,255)
pgYellow,pgDarkYellow,pgGold = (255,255,0),(200,200,0),(212,175,55)
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#Draw button function
def drawRectangle(Colour,X,Y,Width,Height):
    pygame.draw.rect(Window,Colour,(X,Y,Width,Height))              
    
#Draw circle function
def drawCircle(Colour,X,Y,Rad):
    pygame.draw.circle(Window,Colour,(X,Y),Rad)

#Draw centre line
def centreLine():
    Draw_Rectangle(pgRed,599,0,2,1000)
    pygame.display.update()

#Display images
def imageDisplay(Image_name,Width,Height,x,y):
    Image = pygame.image.load(f"{Image_name}")
    Image = pygame.transform.scale(Image,(Width,Height))
    ImageRect = Image.get_rect()
    ImageRect.center = (x,y)
    Window.blit(Image,ImageRect)
    return ImageRect.center,Image

#Display text
def textDisplay(Font_Size,Text,Colour,x,y):
    Display_Text = pygame.font.Font("freesansbold.ttf",Font_Size)
    Text = Display_Text.render(F"{Text}",True,Colour)
    Window.blit(Text,[x,y])
    
#---------------------------------------------------------------------------------


class pgButton:

    def __init__(self,buttonX,buttonY,buttonWidth,buttonHeight,buttonColour,buttonHoverColour,buttonTextSize,buttonText,buttonTextColour,command):

        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight

        self.buttonX = buttonX - self.buttonWidth//2
        self.buttonY = buttonY - self.buttonHeight//2
        
        self.buttonColour = buttonColour
        self.buttonTextSize = buttonTextSize
        self.buttonHoverColour = buttonHoverColour

        self.buttonText = buttonText
        self.buttonTextX = (self.buttonX + (self.buttonWidth//2) - (len(self.buttonText)//2.6) * self.buttonTextSize)
        self.buttonTextY = (self.buttonY + self.buttonHeight//2 - (self.buttonTextSize // 2)) 
        self.buttonTextColour = buttonTextColour

        self.command = command

    def displayButton(self):
        drawRectangle(self.buttonColour,self.buttonX,self.buttonY,self.buttonWidth,self.buttonHeight)
        textDisplay(self.buttonTextSize,self.buttonText,self.buttonTextColour,self.buttonTextX,self.buttonTextY)

    def buttonHover(self):
        drawRectangle(self.buttonHoverColour,self.buttonX,self.buttonY,self.buttonWidth,self.buttonHeight)
        textDisplay(self.buttonTextSize,self.buttonText,self.buttonTextColour,self.buttonTextX,self.buttonTextY)

    def buttonInteraction(self):
        self.command()

def runGame():
    print("Ran")


buttons = []

buttons.append(pgButton((pgWidth//4),(pgHeight//1.1),150,100,pgLightBlue,pgLightGreen,smallText,"Hello",pgBlack,runGame))

Window.fill(pgLightRed)

for button in buttons:
    button.displayButton()

pygame.display.update()
    
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        mouse = pygame.mouse.get_pos()
        
        for button in buttons:
            
            if button.buttonX < mouse[0] < button.buttonX + button.buttonWidth and button.buttonY < mouse[1] < button.buttonY + button.buttonHeight:
                button.buttonHover()
                pygame.display.update()

                if pygame.mouse.get_pressed()[leftClick]:
                    button.buttonInteraction()

            else:
                button.displayButton()
                pygame.display.update()
