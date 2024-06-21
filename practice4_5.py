import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.sound(1).set(notes='A2C3', tones='NN', volumes='33', effects='NN', speed=10)

ballx = pyxel.rndi(0,199)
bally = 0
padx = 100
score=0
angle = pyxel.rndi(30, 150)
vx = pyxel.cos(angle)
vy = pyxel.sin(angle)

def update():
    global ballx, bally, vx, vy,padx,score
    padx = pyxel.mouse_x
    if ballx >= 200 or ballx <= 0:
        vx = vx * -1#式に－1を入れることで恒常的に負となる
    
    ballx += vx
    bally += vy
    
    if bally >= 200:
        pyxel.play(0,0)
        ballx = pyxel.rndi(0,199)
        bally = 0
        angle = pyxel.rndi(30, 150)
        vx = pyxel.cos(angle)
        vy = pyxel.sin(angle)
    
    if 195< bally and padx-20 < ballx < padx+40:
        score += 10
        pyxel.play(0,1)
        ballx = pyxel.rndi(0,199)
        bally = 0
        angle = pyxel.rndi(30, 150)
        vx = pyxel.cos(angle)
        vy = pyxel.sin(angle)
    

def draw():
    global ballx, bally, vx, vy, padx,score
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(100,30,'you got:'+str(score),1)

pyxel.run(update, draw)