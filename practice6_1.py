import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.sound(1).set(notes='A2C3', tones='NN', volumes='33', effects='NN', speed=10)
padx = 100
score=0
miss=0

class Ball():
    def __init__(self):

        self.x = pyxel.rndi(0, 199) 
        #オブジェクト.xとされたら、↑を実行（ただし、初期状態でやっている）
        self.y = 0
        self.a = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(self.a)
        self.vy = pyxel.sin(self.a)
         
balls = [Ball(), Ball(), Ball()]




def update():
    global score,miss,padx
    for i in range(0,len(balls)): 
        padx = pyxel.mouse_x
        if balls[i].x >= 200 or balls[i].x <= 0:
            balls[i].vx = balls[i].vx * -1
    
        balls[i].x += balls[i].vx
        balls[i].y += balls[i].vy
    
        if balls[i].y >= 200:
            pyxel.play(0,0)
            balls[i].x = pyxel.rndi(0,199)
            balls[i].y = 0
            balls[i].a = pyxel.rndi(30, 150)
            balls[i].vx = pyxel.cos(balls[i].a)
            balls[i].vy = pyxel.sin(balls[i].a)
            miss += 1
    
        if 195< balls[i].y and padx -20 < balls[i].x < padx +40:
            
            score += 10
            pyxel.play(0,1)
            balls[i].x = pyxel.rndi(0,199)
            balls[i].y = 0
            balls[i].a = pyxel.rndi(30, 150)
            balls[i].vx = pyxel.cos(balls[i].a)
            balls[i].vy = pyxel.sin(balls[i].a)
    

def draw():
    global score,miss,padx
    pyxel.cls(7)
    if miss >= 10:
        return
    for i in range(0, len(balls)):
        pyxel.circ(balls[i].x, balls[i].y, 10, 6)
        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.text(100,30,'you got:'+str(score),1)
        pyxel.text(100,50,'you lost:'+str(miss),1)
    
pyxel.run(update, draw)   


