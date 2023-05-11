import pygame , sys , os , math
from pygame.locals import*

# Displaying the constants #

DISPLAY_WIDTH = 750 
DISPLAY_HEIGHT = 500
FPS = 30
TEXT_HEIGHT = 25

# CHOOSING COLORS #

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
COMBLUE  = (233, 232, 255)

BGCOLOR = WHITE
TEXTCOLOR = BLACK


def main():
    global FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    
    windowWidth  = 640
    windowHeight = 480 
    lineNumber   = 0
    newChar      = ''
    typeChar     = False
    textString   = ''
    mainList     = []
    mainList.append(textString)
    deleteKey    = False
    returnKey    = False
    insertPoint  = 0
    camerax      = 0
    cameray      = 0
    mouseClicked = False
    mouseX       = 0
    mouseY       = 0
    
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)    
    displaySurf.fill(BGCOLOR)
    displaySurf.convert()
    pygame.display.update()
    
    pygame.display.set_caption('Notepad')
    mainFont = pygame.font.SysFont('Helvetica', TEXTHEIGHT)
    
    cursorRect = getCursorRect(STARTX, STARTY + (TEXTHEIGHT + (TEXTHEIGHT/4)), mainFont, camerax, cameray)
    
    ## The main loop detects user input, displays the text on the screen, displays the cursor on the screen, and adjusts the camera view as per as the necessity...
    
    while True:
                camerax, cameray = adjustCamera(mainList, lineNumber, insertPoint, cursorRect, mainFont, camerax, cameray, windowWidth, windowHeight)
                 newChar, typeChar, deleteKey, returnKey, directionKey, windowWidth, windowHeight, mouseX, mouseY, mouseClicked= getInput(windowWidth, windowHeight)
                
                  if newChar == 'escape':
                         mainList = saveAndLoadScreen(mainList, windowWidth, windowHeight, displaySurf, mainFont)
                         newChar = False
                         insertPoint = 0
                         lineNumber = 0
            mainList,lineNumber, insertPoint, cursorRect = displayText(mainFont, newChar, typeChar, mainList, deleteKey, returnKey, lineNumber, insertPoint, directionKey, camerax, cameray, cursorRect, windowWidth, windowHeight, displaySurf, mouseClicked, mouseX, mouseY)
            displayInfo(insertPoint, mainFont, cursorRect, camerax, windowWidth, windowHeight, displaySurf)

            pygame.display.update()
            FPSCLOCK.tick(FPS)
            
            # Interprets user input and changes mainList, lineNumber, insertPoint and cursorRect accordingly.  There is a function called blitAll() which blits all strings to the main surface. #
            
            def displayText(mainFont , newChar , typeChar , mainList , deleteKey , returnKey , lineNumber , insertPoint , directionKey , camerax , cameray , cursorRect , windowwidth , windowHeight , displaySurf , mouseClicked , mouseX , mouseY ):
                if returnKey:
                    firstString = getStringAtInsertPoint( mainList , lineNumber , insertPoint)
                    secondString = getStringAfterInsertPoint( mainList , lineNumber , insertPoint)
                    mainList[lineNumber] +=1
                    returnKey = False
                    insertPoint = 0
                    cursorRect.x = STARTX
                    stringRect = getStringAtInsertPoint(mainList , lineNumber , insertPoint , mainFont , camerax , cameray )
                    cursorRect.y = stringRect.top    
                    
                 elif mouseClicked:
                    insertPoint , lineNumber , cursorRect = setCursorToClick(mainList , cursorRect , mainFont ,  camerax , cameray , mouseX , mouseY)
                  
                 elif directionKey:
                        if directionKey == LEFT 
                            if directionKey == 0:
                                if insertPoint > 0:
                                    insertPoint -= 1
                                    stringRect = getStringRectAtInsertPoint( mainList , linenumber , insertPoint , mainFont , camerax  , cameray)
                                    cursorRect.x = stringRect.right
                                    cursorRect.y = STARTY
                                    
                           
                        
                        elif lineNumber > 0:
                            if insertPoint == 0:
                                lineNumber -= 1
                                insertPoint = len(mainList[LineNumber])
                                stringReact = getStringReactAtInsertPoint(mainList , lineNumber , insertPoint , mainFont , camerax , cameray)
                                cursorRect.x = stringRect.right
                                cursorRecr.y = STARTY
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                    
                    



    

    
