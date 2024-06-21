import pyxel

pyxel.init(200,200)

ballx = 0
bally = 0
vx = 0.866  # cos 60 degree
vy = 0.5  # sin 60 degree
padx = 100
score=0

def update():
    global ballx, bally, vx, vy,padx,score
    padx = pyxel.mouse_x
    if ballx >= 200 or ballx < 0:
        vx = vx * -1

    ballx += vx
    bally += vy

    if bally >= 200:
        ballx = 0
        bally = 0
    
    if bally > 195 and padx-20 < ballx < padx+40:
        score += 10
        ballx = 0
        bally = 0
        

def draw():
    global ballx, bally, vx, vy, padx
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(100,30,'you got:'+str(score),1)

pyxel.run(update, draw)