import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.sound(1).set(notes='A2C3', tones='NN', volumes='33', effects='NN', speed=10)
score=0
miss=0

class Ball():
    def __init__(self):

        self.x = pyxel.rndi(0, 199) 
        #オブジェクト.xとされたら、↑を実行（pyxel.rndi(0,199)を返す）（ただし、初期状態でやっている）
        self.y = 0
        self.a = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(self.a)
        self.vy = pyxel.sin(self.a)
         
balls = [Ball(), Ball(), Ball()]#クラス名（）とやった瞬間にオブジェクトが作成され、それを何かの関数に入れておく

class Pad():
    def __init__(self):
        self.px = 0
        #(クラスPadのオブジェクトの).pxという関数のひな形を作る
        #クラスPadに定義されたら、（オブジェクト名）.pxという関数を持ちますよ～

pad = Pad()
#pad.pxに一旦0をあてがう


def update():
    global score,miss
    pad.px = pyxel.mouse_x#pad.pxの値を更新
    for i in range(0,len(balls)): 
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
    
        if 195< balls[i].y and pad.px -20 < balls[i].x < pad.px +40:
            
            score += 10
            pyxel.play(0,1)
            balls[i].x = pyxel.rndi(0,199)
            balls[i].y = 0
            balls[i].a = pyxel.rndi(30, 150)
            balls[i].vx = pyxel.cos(balls[i].a)
            balls[i].vy = pyxel.sin(balls[i].a)
    

def draw():
    global score,miss
    pyxel.cls(7)
    if miss >= 10:
        return
    for i in range(0, len(balls)):
        pyxel.circ(balls[i].x, balls[i].y, 10, 6)
        pyxel.rect(pad.px-20, 195, 40, 5, 14)
        pyxel.text(100,30,'you got:'+str(score),1)
        pyxel.text(100,50,'you lost:'+str(miss),1)
    
pyxel.run(update, draw)   
