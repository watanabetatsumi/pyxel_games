import pyxel

pyxel.init(200,200)

class App:
    def __init__(self):
        
        self.balls = [Ball(), Ball(), Ball()]#クラス名（）とやった瞬間にオブジェクトが作成され、それを何かの関数に入れておく
        #Appクラスにおける関数をつくったうえでそこにインスタンスを投入
        self.pad = Pad()#オブジェクトを生成
        #pad.pxに一旦0をあてがう
        self.count = detail()#オブジェクトを生成
        pyxel.mouse(True)
        pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sound(1).set(notes='A2C3', tones='NN', volumes='33', effects='NN', speed=10)
        pyxel.run(self.update, self.draw)

    def update(self):
        
        self.pad.px = pyxel.mouse_x#pad.pxの値を更新
        for i in range(0,len(self.balls)): 
            self.balls[i].move()
            if self.pad.catch(self.balls[i]):
                self.count.plus()
                pyxel.play(0,1)
                self.balls[i].restart()
        
            if self.balls[i].y >= 200:
                pyxel.play(0,0)
                self.balls[i].restart()
                self.count.miss()
    
    def draw(self):
        
        pyxel.cls(7)
        if self.count.l >= 10:
            return
        for i in range(0, len(self.balls)):
            pyxel.circ(self.balls[i].x, self.balls[i].y, 10, 6)
            pyxel.rect(self.pad.px-20, 195, 40, 5, 14)
            pyxel.text(100,30,'you got:'+str(self.count.p),1)
            pyxel.text(100,50,'you lost:'+str(self.count.l),1)


class Ball():
    def __init__(self):
        self.restart()
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

class Pad():
    def __init__(self):
        self.px = 0
        #(クラスPadのオブジェクトの).pxという関数のひな形を作る
        #クラスPadに定義されたら、（オブジェクト名）.pxという関数を持ちますよ～
    def catch(self,balls):
        if self.px - 20 < balls.x < self.px + 40 and 195 < balls.y:
            return True
        else:
            return False

class detail():
    def __init__(self):
        self.p = 0#それぞれ点数、ミスをカウントするための関数を初期に埋め込んでおく
        self.l = 0
    
    def plus(self):
        self.p += 10#関数を更新
    def miss(self):
        self.l +=1

count = detail()#オブジェクトを生成




App()