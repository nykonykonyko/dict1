import pgzrun
WIDTH = 400
HEIGHT = 400
TITLE = "Gradient"

def draw():
    screen.fill("purple") 

    a = Rect((0,0),(350,100))
    a.center = WIDTH/2,HEIGHT/2
    screen.draw.rect(a,"orange")

pgzrun.go()