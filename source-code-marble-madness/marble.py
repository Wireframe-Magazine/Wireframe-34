# Marble Madness
from pygame import image

HEIGHT = 570
WIDTH = 600
gameState = 0
marble = Actor('marble', center=(300, 45))
marbleh = Actor('marble', center=(300, 60))
marble.dir = marble.speed = 0
heightmap = image.load('images/height45.png')
debug = False

def draw():
    if(debug):
        screen.blit("height45", (0, 0))
        marbleh.draw()
    else:
        screen.blit("map", (0, 0))
        if gameState == 0:
            marble.draw()
        else:
            if gameState == 2:
                screen.draw.text("YOU WIN!", center = (300, 300), owidth=0.5, ocolor=(255,255,255), color=(0,0,255) , fontsize=80)
                marble.draw()
            else:
                screen.draw.text("GAME OVER!", center = (300, 300), owidth=0.5, ocolor=(255,255,255), color=(0,0,255) , fontsize=80)
        screen.blit("overlay", (0, 0))

def update():
    if gameState == 0:
        if keyboard.left:
            marble.dir = max(marble.dir-0.1,-1)
            marble.speed = min(1,marble.speed + 0.1)
        if keyboard.right:
            marble.dir = min(marble.dir+0.1,1)
            marble.speed = min(1,marble.speed + 0.1)
        moveMarble()
        marble.speed = max(0,marble.speed - 0.01)
    
def moveMarble():
    global gameState
    ccol = getHeight(marbleh.x,marbleh.y)
    lcol = getHeight(marbleh.x-10,marbleh.y+10)
    rcol = getHeight(marbleh.x+10,marbleh.y+10)
    if ccol.r == 0:
        gameState = 1
    if (lcol.r < ccol.r or rcol.r < ccol.r):
        marble.y += marble.speed
        marble.speed += 0.03
    marbleh.x += marble.speed*marble.dir
    marbleh.y += marble.speed
    marble.x = marbleh.x
    marble.y = (marbleh.y*0.6)+((255-ccol.r)*1.25)
    marble.angle = marble.angle + marble.speed*marble.dir*-10
    if marble.angle > 0 : marble.angle = -50
    if marble.angle < -50 : marble.angle = 0
    if marbleh.y > 610: gameState = 2

def getHeight(x,y):
    return heightmap.get_at((int(x),int(y)))


