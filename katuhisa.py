import pyxel

class App:
    def __init__(self):
        pyxel.init(200,200)
        self.pad = Pad()
        self.spears = [Spear(),Spear(),Spear()]
        self.sheild = Sheild()
        pyxel("#作ったドット絵のファイル名")
        #→音声はここに入力するといい
        pyxel.run(self.update,self.draw)

    def update(self):
        self.pad.px = pyxel.mouse_x
        self.pad.py = pyxel.mouse_y
        for i in self.spears:
            if.move()
            if i.y > 210:
                i.restart()
            if self.pad.catch(i):
                pyxel.play()#やりにあたったときの音
                i.restart()

        self.sheild.move()
        if self.sheild.y >210:
            self.sheild.restart()
        if self.pad.catch2(self.sheild):
            pyxel.play()#盾を獲得した時の音
            self.sheild.restart()

    def draw(self):
        pyxel.cls(7)
        pyxel.text(100,30,"life point:"+str(self.pad.point),1)
        #pyxel.blt()←作った絵を表示
        if self.pad.point == 0:
            pyxel.cls(7)
            pyxel.text(50,50,"game over!!",1)

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

App()

