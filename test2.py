import pyxel

pyxel.init(200,200)

ball1x = pyxel.rndi(0,199)
ball1y = 0
ball2x = pyxel.rndi(0,199)
ball2y = 0
ball3x = pyxel.rndi(0,199)
ball3y = 0
goalx = 100
goaly = 100
speed = 3
score = 0
time = 0
angle = pyxel.rndi(30, 150)
vx1 = pyxel.cos(angle)
vy1 = pyxel.sin(angle)
vx2 = pyxel.cos(angle)
vy2 = pyxel.sin(angle)
vx3 = pyxel.cos(angle)
vy3 = pyxel.sin(angle)

pyxel.load("b-final.pyxres")
pyxel.sound(0).set(notes='B2C3', tones='TT', volumes='33', effects='NN', speed=8)
pyxel.sound(1).set(notes='C2C4', tones='TT', volumes='33', effects='NN', speed=5)
pyxel.sound(2).set(notes='D2E4', tones='TT', volumes='66', effects='NN', speed=3)

def update():
    global ball1x, ball1y,ball2x,ball2y,ball3x,ball3y,vx1,vy1,vx2,vy2,vx3,vy3,goalx,goaly,speed,score,time

    ball1x += vx1*speed
    ball1y += vy1*speed
    ball2x += vx2*speed
    ball2y += vy2*speed
    ball3x += vx3*speed
    ball3y += vy3*speed
    time = pyxel.frame_count
    goalx = pyxel.mouse_x
    goaly = pyxel.mouse_y
    if ball1x >= 200:
        vx1 = -vx1
    elif ball1x <= 0:
        vx1 = -vx1
    elif goalx -10 <= ball1x and goalx +10 >= ball1x and goaly -10 <= ball1y and goaly + 10 >= ball1y :
        ball1y = 0
        ball1x = pyxel.rndi(0,199)
        angle = pyxel.rndi(30, 150)
        vx1 = pyxel.cos(angle)
        vy1 = pyxel.sin(angle)
        score = score + 1
        pyxel.play(0,0)
    elif ball1y >= 200:
        ball1y = 0
        ball1x = pyxel.rndi(0,199)
        angle = pyxel.rndi(30, 150)
        vx1 = pyxel.cos(angle)
        vy1 = pyxel.sin(angle)
        speed = speed*1.1 
        pyxel.play(0,1) 

    if ball2x >= 200:
        vx2 = -vx2
    elif ball2x <= 0:
        vx2 = -vx2
    elif goalx -10 <= ball2x and goalx +10 >= ball2x and goaly -10 <= ball2y and goaly + 10 >= ball2y :
        ball2y = 0
        ball2x = pyxel.rndi(0,199)
        angle = pyxel.rndi(30, 150)
        vx2 = pyxel.cos(angle)
        vy2 = pyxel.sin(angle)
        score = score + 2
        pyxel.play(0,0)
    elif ball2y >= 200:
        ball2y = 0
        ball2x = pyxel.rndi(0,199)
        angle = pyxel.rndi(30, 150)
        vx2 = pyxel.cos(angle)
        vy2 = pyxel.sin(angle)
        speed = speed*1.1  
        pyxel.play(0,1) 

    if ball3x >= 200:
        vx3 = -vx3
    elif ball3x <= 0:
        vx3 = -vx3
    elif goalx -10 <= ball3x and goalx +10 >= ball3x and goaly -10 <= ball3y and goaly + 10 >= ball3y :
        ball3y = 0
        ball3x = pyxel.rndi(0,199)
        angle = pyxel.rndi(30, 150)
        vx3 = pyxel.cos(angle)
        vy3 = pyxel.sin(angle)
        score = score - 1
        pyxel.play(0,2)
    elif ball3y >= 200:
        ball3y = 0
        ball3x = pyxel.rndi(0,199)
        angle = pyxel.rndi(30, 150)
        vx3 = pyxel.cos(angle)
        vy3 = pyxel.sin(angle) 

    if time >= 800 :
        pyxel.quit()
    
def draw():
    global ball1x, ball1y, ball2x,ball2y,ball3x,ball3y,vx1, vy1,vx2,vy2,vx3,vy3,goalx,goaly,score,time
    pyxel.cls(13)
    pyxel.blt(ball1x,ball1y,0,0,0,16,16,1)
    pyxel.blt(ball2x,ball2y,0,32,0,16,16,1)
    pyxel.blt(ball3x,ball3y,0,16,0,16,16,1)
    pyxel.blt(goalx,goaly,0,0,16,32,32,1)
    pyxel.text(10,10,"SCORE:"+str(score),10)   
    pyxel.text(120,10,"TIME:"+str(time)+" frame ",0)

pyxel.run(update, draw)