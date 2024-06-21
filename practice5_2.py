import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.sound(1).set(notes='A2C3', tones='NN', volumes='33', effects='NN', speed=10)

ballx = [pyxel.rndi(0, 199), pyxel.rndi(0, 199), pyxel.rndi(0, 199)]  
bally = [0, 0, 0]
padx = 100
score=0
angle = [pyxel.rndi(30, 150), pyxel.rndi(30, 150),pyxel.rndi(30, 150)]
vx = [pyxel.cos(angle[0]), pyxel.cos(angle[1]), pyxel.cos(angle[2])]
vy = [pyxel.sin(angle[0]), pyxel.sin(angle[1]), pyxel.sin(angle[2])]
miss=0

def update():
    global ballx, bally, vx, vy,padx,score,miss
    for i in range(0, len(ballx)):
        padx = pyxel.mouse_x
        if ballx[i] >= 200 or ballx[i] <= 0:
            vx[i] = vx[i] * -1
    
        ballx[i] += vx[i]
        bally[i] += vy[i]
    
        if bally[i] >= 200:
            pyxel.play(0,0)
            ballx[i] = pyxel.rndi(0,199)
            bally[i] = 0
            angle[i] = pyxel.rndi(30, 150)
            vx[i] = pyxel.cos(angle[i])
            vy[i] = pyxel.sin(angle[i])
            miss += 1　#ミスした時、カウントされる
    
        if 195< bally[i] and padx -20 < ballx[i] < padx +40:
            score += 10
            pyxel.play(0,1)
            ballx[i] = pyxel.rndi(0,199)
            bally[i] = 0
            angle[i] = pyxel.rndi(30, 150)
            vx[i] = pyxel.cos(angle[i])
            vy[i] = pyxel.sin(angle[i])
    

def draw():
    global ballx, bally, vx, vy, padx,score,miss
    pyxel.cls(7)
    if miss >= 10:　ミスが十回以上だと終了
        return
    for i in range(0, len(ballx)):
        pyxel.circ(ballx[i], bally[i], 10, 6)
        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.text(100,30,'you got:'+str(score),1)
        pyxel.text(100,50,'you lost:'+str(miss),1)#ミスの回数を表示
    
pyxel.run(update, draw)