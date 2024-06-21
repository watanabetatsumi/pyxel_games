import pyxel
import time


class Spear():
    def __init__(self):
        self.dise = rndi(1,3)
        self.restart()
    
    def restart(self):
        self.x = pyxel.rndi(20,180)
        if self.dise == 1:
            self.y = 0
        elif self.dise == 2:
            self.y = -15
        elif self.dise == 3:
            self.y = -30
    
    def move(self):
        self.y += 3

class Shield():
    def __init__(self):
        self.restart()
    
    def restart(self):
        self.x = pyxel.rndi(20,180)
        self.y = -150
    
    def move(self):
        self.y += 5

class Pad():
    def __init__(self):
        self.px = 0
        self.py = 0
        self.point = 0
    
    def catch(self,spears):
        if spears.x-10 < self.px < spears.x:
            self.point -= 1
            return True
        else:
            retrun False
    
    def catch2(self,sheild)    
        if shield.x:
            self.point +=1
            return True
        else:
            return False
class App:
    def __init__(self):
        pyxel.init(200,200)
        self.pad = Pad()
        self.spears = [Spear(),Spear(),Spear(),Spear(),Spear(),Spear()]
        self.sheild = Shield()
        pyxel.load("my_resource.pyxres")
        self.start = int(time.time())
        pyxel.run(self.update, self.draw)

    def update(self):
        self.current = int(time.time())
        self.playtime = self.current - self.start
        self.pad.px = pyxel.mouse_x
        for i in self.spears:
            i.move()
            if i.y > 210:
                i.restart()
            if self.pad.catch(i):
                #pyxel.play()#やりにあたったときの音
                i.restart()

        self.sheild.move()
        if self.sheild.y >210:
            self.sheild.restart()
        if self.pad.catch2(self.sheild):
            #pyxel.play()#盾を獲得した時の音
            self.sheild.restart()
    def draw(self):
        pyxel.cls(7)
        pyxel.blt(self.pad.px,195,0,0,24,15,15,0)
        pyxel.text(100,30,"life point:"+str(self.pad.point),1)
        pyxel.text(100,60,"time limit:"+str(self.playtime)+"min",1)
        for s in self.spears:
            pyxel.blt(s.x,s.y,0,0,0,15,15,0)
        pyxel.blt(self.sheild.x,self.sheild.y,0,16,0,15,15,0)
        #pyxel.blt()←作った絵を表示
        if self.pad.point < 0:
            pyxel.cls(7)
            pyxel.text(50,50,"game over!!",1)
            
        if self.playtime > 5:
            self.sheild.restart()
            for i in self.spears:
                i.restart()#オブジェクトを消去
            pyxel.cls(7)
            pyxel.text(50,50,"finish!! your points:"+str(self.pad.point),1)

App()