import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.sound(1).set(notes='A2C3', tones='NN', volumes='33', effects='NN', speed=10)


class Ball():
    def restart(self):

        self.x = pyxel.rndi(0, 199) 
        #オブジェクト.xとされたら、↑を実行（pyxel.rndi(0,199)を返す）（ただし、初期状態でやっている）
        self.y = 0
        self.a = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(self.a)
        self.vy = pyxel.sin(self.a)
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= 200 or self.x <= 0:
            self.vx = self.vx * -1
         
balls = [Ball(), Ball(), Ball()]#クラス名（）とやった瞬間にオブジェクトが作成され、それを何かの関数に入れておく

class Pad():
    def __init__(self):
        self.px = pyxel.mouse_x
        #(クラスPadのオブジェクトの).pxという関数のひな形を作る
        #クラスPadに定義されたら、（オブジェクト名）.pxという関数を持ちますよ～
    def catch(self,balls):
        if self.px - 20 < balls.x < self.px + 40 and 195 < balls.y:
            return True
        else:
            return False
pad = Pad()#オブジェクトを生成
#pad.pxに一旦0をあてがう

class detail():
    def __init__(self):
        self.p = 0#それぞれ点数、ミスをカウントするための関数を初期に埋め込んでおく
        self.l = 0
    
    def plus(self):
        self.p += 10#関数を更新
    def miss(self):
        self.l +=1

count = detail()#オブジェクトを生成


for c in range(0,len(balls)):
    balls[c].restart()
def update():
    #global score,miss
    #pad.px = pyxel.mouse_x#pad.pxの値を更新
    for i in range(0,len(balls)): 
        balls[i].move()
        if pad.catch(balls[i]):
            count.plus()
            pyxel.play(0,1)
            balls[i].restart()
    
        if balls[i].y >= 200:
            pyxel.play(0,0)
            balls[i].restart()
            count.miss()
    
        #if 195< balls[i].y and pad.px -20 < balls[i].x < pad.px +40:
            
            #score += 10
            #pyxel.play(0,1)
            #balls[i].restart()
        
        
    

def draw():
    #global score,miss
    pyxel.cls(7)
    if count.l >= 10:
        return
    for i in range(0, len(balls)):
        pyxel.circ(balls[i].x, balls[i].y, 10, 6)
        pyxel.rect(pad.px-20, 195, 40, 5, 14)
        pyxel.text(100,30,'you got:'+str(count.p),1)
        pyxel.text(100,50,'you lost:'+str(count.l),1)
    
pyxel.run(update, draw)   
