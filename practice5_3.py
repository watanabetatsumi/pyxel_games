import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.sound(1).set(notes='A2C3', tones='NN', volumes='33', effects='NN', speed=10)

ballx = [pyxel.rndi(0, 199)]  #初期設定
bally = [0]
padx = 100
score=0
angle = [pyxel.rndi(30, 150)]
vx = [pyxel.cos(angle[0])]
vy = [pyxel.sin(angle[0])]
num=0　#成功した回数を数える関数
speed=5　#球の球速の初期設定

def update():
    global ballx, bally, vx, vy,padx,score,num,angle,speed
    for i in range(0, len(ballx)):
        padx = pyxel.mouse_x
        if ballx[i] >= 200 or ballx[i] <= 0:
            vx[i] = vx[i] * -1
    
        ballx[i] += vx[i]*speed
        bally[i] += vy[i]*speed
    
        if bally[i] >= 200:
            pyxel.play(0,0)
            ballx[i] = pyxel.rndi(0,199)
            bally[i] = 0
            angle[i] = pyxel.rndi(30, 150)
            vx[i] = pyxel.cos(angle[i])
            vy[i] = pyxel.sin(angle[i])
    
        if 195< bally[i] and padx -20 < ballx[i] < padx +40:
            score += 10
            pyxel.play(0,1)
            ballx[i] = pyxel.rndi(0,199)
            bally[i] = 0
            angle[i] = pyxel.rndi(30, 150)
            vx[i] = pyxel.cos(angle[i])
            vy[i] = pyxel.sin(angle[i])
            speed += 0.4　#成功したらスピードが上がる
            if score//100 > num:#10回ずつ成功すると。。。
                num +=1
                ballx.append(pyxel.rndi(0, 199))#球の数が増える
                bally.append(0)
                angle.append(pyxel.rndi(30, 150))
                vx.append(pyxel.cos(angle[num]))
                vy.append(pyxel.sin(angle[num]))
                speed=5#球の速度は戻る
                

    

def draw():
    global ballx, bally, vx, vy, padx,score
    pyxel.cls(7)
    for i in range(0, len(ballx)):
        pyxel.circ(ballx[i], bally[i], 10, 6)
        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.text(100,30,'you got:'+str(score),1)

pyxel.run(update, draw)