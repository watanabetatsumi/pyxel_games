import pyxel

pyxel.init(200,200)

ballx = pyxel.rndi(0,199)
bally = 0
a=0
angle = pyxel.rndi(30, 150)
vx = pyxel.cos(angle)
vy = pyxel.sin(angle)


def update():
    global ballx, bally,a,vx,vy
    
    if a == 0:
        ballx += vx*3
        bally += vy*3
    else:
        ballx -= vx*3
        bally += vy*3
    
    if ballx > 200:
        a=1
    if 0< ballx <1 :
        a=0

    if bally >= 200:
        ballx = pyxel.rndi(0,199)
        bally = 0
        a=0
        angle = pyxel.rndi(30, 150)
        vx = pyxel.cos(angle)
        vy = pyxel.sin(angle)

def draw():
    global ballx, bally, vx, vy
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)

pyxel.run(update, draw)