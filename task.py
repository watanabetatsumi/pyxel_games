import pyxel
import time

class App:
    def __init__(self):
        pyxel.init(200, 200)
        self.t1 = time.time()
        self.lat = 0
        self.lon = 0
        self.gokies = [Gokiburi(),Gokiburi()]
        self.spiders = [Spider(),Spider()]
        #pyxel.mouse(True)
        self.pad = Pad()#オブジェクトを生成
        # リソースファイルの読み込み
        pyxel.load("my_resource.pyxres")
        #pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.run(self.update, self.draw)
            

    def update(self):
        self.pad.px = pyxel.mouse_x#pad.pxの値を更新
        self.pad.py = pyxel.mouse_y#pad.pxの値を更新
        for i in self.gokies: 
            i.move()
            if i.y <= -51 or i.x <= -51:
                i.restart()
            if 60 <= i.x <= 148 and 90 <= i.y <= 118:
                i.restart2()
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.pad.catch(i):
                    pyxel.play(0,1,loop=False)
                    self.lat = pyxel.mouse_y
                    self.lon = pyxel.mouse_x
                    i.restart()
                    if self.pad.count == 10:
                        self.gokies.append(Gokiburi())
                        self.spiders.append(Spider())
                    if self.pad.count == 20:
                        self.gokies.append(Gokiburi()) 
                        self.spiders.append(Spider())
                    if self.pad.point == 30:
                         self.t2 = time.time()
        for s in self.spiders:
            s.move()
            if s.y <= -51 or s.x <= -51:
                s.restart()
            if 60 <= s.x <= 148 and 90 <= s.y <= 118:
                s.restart2()
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.pad.catch2(s):
                    pyxel.play(1,0,loop=False)
                    self.lat = pyxel.mouse_y
                    self.lon = pyxel.mouse_x
                    s.restart()    

    def draw(self):
        pyxel.cls(7)
        if self.lat == 0 and self.lon == 0:
            True
        else:
            pyxel.blt(self.lon,self.lat,0,0,24,16,16,0)
        pyxel.text(100,30,'you caught:'+str(self.pad.point)+"!",1)
        for i in self.gokies:
            pyxel.blt(i.x, i.y, 0, 0, 0, 15, 18, 0)
        for s in self.spiders:
            pyxel.blt(s.x, s.y, 0, 16, 0, 15, 15, 0)
        #質問点：30匹つかまえたら。クリアタイムを表示しながら終了する方法、花火の退治エフェクトの出し方
        pyxel.blt(60, 60, 1, 0, 0, 88, 88, 0)
        pyxel.blt(195, 0, 1, 0, 0, 5, 200, 0)
        pyxel.blt(0, 195, 1, 0, 0, 200, 5, 0)
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 2, 3, 0, 10, 15, 0) 
        if self.pad.point == 30:
            pyxel.cls(7)
            pyxel.text(100,50,"game clear!!",1)
            pyxel.text(100,70,"time:"+str(self.t2-self.t1),1)

    

        # イメージの描画：(x, y, img, u, v, w, h, [colkey])
        # xy:コピー先の座標、img:イメージバンクの番号
        # uv:コピー元の座標、wh:コピー範囲、colkey:透明色
       

class Gokiburi():
    def __init__(self):
        self.restart()
        self.dise = 1
        self.dise2 = 1
        self.switch = 1
    def restart(self):
        
        self.dise = pyxel.rndi(1,2)
        if self.dise == 1:
            self.x = pyxel.rndi(0, 199) 
            self.y = -50
            self.a = pyxel.rndi(30, 150)
            self.vx = pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)
        #オブジェクト.xとされたら、↑を実行（pyxel.rndi(0,199)を返す）（ただし、初期状態でやっている）
        if self.dise == 2:
            self.y = pyxel.rndi(0, 199)
            self.x = -50
            self.a = pyxel.rndi(30, 150)
            self.vx = pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)

    def restart2(self):
        self.dise = pyxel.rndi(1,4)
        if self.dise == 1: 
            self.x = 104
            self.y = 90
            self.a = pyxel.rndi(30, 150)
            self.vx = -pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)

        if self.dise == 2: 
            self.x = 104
            self.y = 90
            self.a = pyxel.rndi(30, 150)
            self.vx = -pyxel.cos(self.a)
            self.vy = -pyxel.sin(self.a)
        
        if self.dise == 3: 
            self.x = 104
            self.y = 118
            self.a = pyxel.rndi(30, 150)
            self.vx = -pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)
        
        if self.dise == 4: 
            self.x = 104 
            self.y = 118 
            self.a = pyxel.rndi(30, 150)
            self.vx = pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)
        
        #オブジェクト.xとされたら、↑を実行（pyxel.rndi(0,199)を返す）（ただし、初期状態でやっている）
        
    def move(self):
        self.switch = pyxel.rndi(1,4)
        if self.switch == 1:
            return
        else:
            self.dise2 = pyxel.rndi(31,35)
            self.rnspeed=self.dise2/32
            self.vx = self.vx*self.rnspeed
            self.vy = self.vy*self.rnspeed
            self.x += self.vx
            self.y += self.vy
            if self.x >= 200: 
                self.vx = self.vx * -1
                #self.vy = self.vy * (pyxel.rndi(-8, 15)/10)
            if self.y >= 200:
                #self.vx = self.vx * (pyxel.rndi(-8, 15)/10)
                self.vy = self.vy * -1

class Spider():
    def __init__(self):
        self.restart()
        self.dise = 1
        self.dise2 = 1
        self.switch = 1
    def restart(self):
        self.dise = pyxel.rndi(1,2)
        if self.dise == 1:
            self.x = pyxel.rndi(0, 199) 
            self.y = -50
            self.a = pyxel.rndi(30, 150)
            self.vx = pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)
        #オブジェクト.xとされたら、↑を実行（pyxel.rndi(0,199)を返す）（ただし、初期状態でやっている）
        if self.dise == 2:
            self.y = pyxel.rndi(0, 199)
            self.x = -50
            self.a = pyxel.rndi(30, 150)
            self.vx = pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)

    def restart2(self):
        self.dise = pyxel.rndi(1,4)
        if self.dise == 1: 
            self.x = 104
            self.y = 90
            self.a = pyxel.rndi(30, 150)
            self.vx = -pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)

        if self.dise == 2: 
            self.x = 104
            self.y = 90
            self.a = pyxel.rndi(30, 150)
            self.vx = -pyxel.cos(self.a)
            self.vy = -pyxel.sin(self.a)
        
        if self.dise == 3: 
            self.x = 104
            self.y = 118
            self.a = pyxel.rndi(30, 150)
            self.vx = -pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)
        
        if self.dise == 4: 
            self.x = 104 
            self.y = 118 
            self.a = pyxel.rndi(30, 150)
            self.vx = pyxel.cos(self.a)
            self.vy = pyxel.sin(self.a)
        
        #オブジェクト.xとされたら、↑を実行（pyxel.rndi(0,199)を返す）（ただし、初期状態でやっている）
        
    def move(self):
        self.switch = pyxel.rndi(1,4)
        if self.switch == 1:
            return
        else:
            self.dise2 = pyxel.rndi(30,35)
            self.rnspeed=self.dise2/32
            self.vx = self.vx*self.rnspeed
            self.vy = self.vy*self.rnspeed
            self.x += self.vx
            self.y += self.vy
            if self.x >= 200: 
                self.vx = self.vx * -1
                #self.vy = self.vy * (pyxel.rndi(-8, 15)/10)
            if self.y >= 200:
                #self.vx = self.vx * (pyxel.rndi(-8, 15)/10)
                self.vy = self.vy * -1

            
class Pad():
    def __init__(self):
        self.px = 0
        self.py = 0
        self.point=0
        self.count=0
    def catch(self,gokies):
        if gokies.x-10 < self.px < gokies.x+25 and gokies.y-10 < self.py < gokies.y+28:
            self.point+=1
            self.count+=1
            return True
        else:
            return False
    def catch2(self,spiders):
        if spiders.x-10 < self.px < spiders.x+25 and spiders.y-10 < self.py < spiders.y+25:
            self.point-=2
            return True
        else:
            return False
        #(クラスPadのオブジェクトの).pxという関数のひな形を作る
        #クラスPadに定義されたら、（オブジェクト名）.pxという関数を持ちますよ～

App()