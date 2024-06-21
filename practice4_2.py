import pyxel

pyxel.init(200,200)

ballx = 0
bally = 0
vx = 0.866  # cos 60 degree
vy = 0.5  # sin 60 degree
a=0
speed=1

def update():
    global ballx, bally, vx, vy,a,speed
    if a == 0:
        ballx += vx*speed*1.1
        bally += vy*speed*1.1
    else:
        ballx -= vx*speed*1.1
        bally += vy*speed*1.1
    
    if ballx > 200:
        a=1
    if ballx < -1:
        a=0

    if bally >= 200:
        ballx = 0
        bally = 0
        a=0
        speed += 1

def draw():
    global ballx, bally, vx, vy
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)

pyxel.run(update, draw)