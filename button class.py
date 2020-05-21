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


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Button class
"""
Creates a class to make buttons quickly
"""
class pgButton:

    def __init__(self,buttonX,buttonY,buttonWidth,buttonHeight,buttonColour,buttonHoverColour,buttonTextSize,buttonText,buttonTextColour,command):

        self.Width = buttonWidth
        self.Height = buttonHeight

        self.X = buttonX - self.Width//2
        self.Y = buttonY - self.Height//2
        
        self.Colour = buttonColour
        self.TextSize = buttonTextSize
        self.HoverColour = buttonHoverColour

        self.Text = buttonText
        self.TextX = (self.X + (self.Width//2) - (pygame.font.Font(None,self.TextSize).size(self.Text)[0]//1.45))
        self.TextY = (self.Y + self.Height//2 - (pygame.font.Font(None,self.TextSize).size(self.Text)[1]//2))
        self.TextColour = buttonTextColour

        self.command = command

    def display(self):
        drawRectangle(self.Colour,self.X,self.Y,self.Width,self.Height)
        textDisplay(self.TextSize,self.Text,self.TextColour,self.TextX,self.TextY)

    def hover(self):
        drawRectangle(self.HoverColour,self.X,self.Y,self.Width,self.Height)
        textDisplay(self.TextSize,self.Text,self.TextColour,self.TextX,self.TextY)

    def interaction(self):
        self.command()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
