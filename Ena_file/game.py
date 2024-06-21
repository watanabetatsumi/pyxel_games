import pyxel
import time
import random

class Money():
    def __init__(self,hand,level):
        self.dise = random.randint(1,3)
        self.name = "money"
        if level == 1:
            self.type = 0
        if level == 2:
            self.type = random.randint(0,1)
        self.flag = 0
        self.a = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(self.a)
        self.vy = pyxel.sin(self.a)
        self.start(hand.x)
    def start(self,hand_x):
        self.x = hand_x + 5
        self.y = -10
    def move(self,speed):
        self.y += 5 * speed
        if 5 > self.x:
            self.vx = self.vx * -1
        if self.x > 195:
            self.vx = self.vx * -1
        self.x += self.vx


class Trash():
    def __init__(self,hand,level):
        self.dise = random.randint(1,3)
        self.name = "trash"
        if level == 1:
            self.type = random.randint(0,1)
        if level == 2:
            self.type = random.randint(0,2)
        self.flag = 0
        self.a = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(self.a)
        self.vy = pyxel.sin(self.a)
        self.start(hand.x)
    def start(self,hand_x):
        self.x = hand_x + 5
        self.y = -10
    def move(self,speed):
        self.y += 5 * speed
        if 5 > self.x:
            self.vx = self.vx * -1
        if self.x > 195:
            self.vx = self.vx * -1
        self.x += self.vx

class Hand():
    def __init__(self):
        self.x = 100
        self.y = 0
        self.vx = 9
    def move(self):
        if 25 > self.x:
            self.vx = self.vx * -1
        if self.x > 175:
            self.vx = self.vx * -1
        self.x += self.vx

class Box():
    def __init__(self):
        self.box_x = 70
        self.box_y = 190
        self.point = 0
    def catch(self,object):
        if object.name != "trash":
            return False
        if object.flag == 1:
            return False
        if self.box_x-10 < object.x < self.box_x + 20 and object.y >= self.box_y:
            object.flag = 1
            return True
        else:
            return False
    def lost_money(self,object):
        if object.name != "money":
            return False
        if object.flag == 1:
            return False
        if self.box_x-10 < object.x < self.box_x + 20 and object.y >= self.box_y:
            object.flag = 1
            return True
        else:
            return False
class Stage():
    def __init__(self):
        self.speed = 1
        self.level = 1
        self.background = 6

class App:
    def __init__(self):
        pyxel.init(200,200)
        self.box = Box()
        self.hand = Hand()
        self.stage = Stage()
        self.dise = random.randint(1,5)
        self.object = None
        pyxel.load("my_resource.pyxres")
        self.start = int(time.time())
        # ボタン押してからスタート
        pyxel.run(self.update, self.draw)
    def update(self):
        if self.stage.level == 1:
            self.current = int(time.time())
            self.playtime = self.current - self.start
            self.box.box_x = pyxel.mouse_x
            self.hand.move()
            if self.object:
                self.object.move(self.stage.speed)
                if self.box.catch(self.object):
                    self.box.point += 1
                if self.box.lost_money(self.object):
                    self.box.point -= 1
                if self.object.flag == 1 & self.object.y > 195:
                    del self.object
                    self.object = None
                if self.object.y > 205:
                    del self.object
                    self.object = None
            else:
                self.dise = random.randint(1,5)
                if self.dise == 1:
                    self.object = Money(self.hand,self.stage.level)
                else:
                    self.object = Trash(self.hand,self.stage.level)
        if self.stage.level == 2:
            self.current = int(time.time())
            self.playtime = self.current - self.start
            self.box.box_x = pyxel.mouse_x
            self.hand.move()
            if self.object:
                self.object.move(self.stage.speed)
                if self.box.catch(self.object):
                    self.box.point += 1
                if self.box.lost_money(self.object):
                    self.box.point -= 1
                if self.object.flag == 1 & self.object.y > 195:
                    del self.object
                    self.object = None
                if self.object.y > 205:
                    del self.object
                    self.object = None
            else:
                self.dise = random.randint(1,5)
                if self.dise == 1:
                    self.object = Money(self.hand,self.stage.level)
                else:
                    self.object = Trash(self.hand,self.stage.level)

    def draw(self):
        pyxel.cls(self.stage.background)
        pyxel.text(100,10,"stage level:"+str(self.stage.level),1)
        pyxel.text(100,30,"life point:"+str(self.box.point),1)
        pyxel.text(100,50,"time limit:"+str(20-self.playtime)+"min",1)
        if self.object:
            if self.object.name == "money":
                if self.object.type == 0:
                    pyxel.blt(self.object.x,self.object.y,0,0,59,15,9,0)
                if self.object.type == 1:
                    pyxel.blt(self.object.x,self.object.y,0,0,73,13,12,0)
            if self.object.name == "trash":
                if self.object.type == 0:
                    pyxel.blt(self.object.x,self.object.y,0,0,46,15,14,0)
                if self.object.type == 1:
                    pyxel.blt(self.object.x,self.object.y,0,0,86,25,14,0)
                if self.object.type == 2:
                    pyxel.blt(self.object.x,self.object.y,0,0,105,14,14,0)
        pyxel.blt(self.box.box_x,self.box.box_y,0,0,0,21,21,0) #ゴミ箱の絵
        pyxel.blt(self.hand.x,self.hand.y,0,0,24,15,15,0) #手の絵
        if self.box.point < 0:
            if self.object:
                del self.object
                self.object = None
            pyxel.cls(self.stage.background)
            pyxel.text(50,50,"game over!!",1)
        if self.playtime > 20:
            if self.object:
                del self.object
                self.object = None
            pyxel.cls(7)
            pyxel.text(20,50,"time over!!",1)
            pyxel.text(20,70,"finish!! your points:"+str(self.box.point),1)
            pyxel.text(20,90,"Now judging...",1)
            if self.playtime > 23 and self.stage.level == 1:
                pyxel.cls(7)
                if self.box.point >= 5:
                    pyxel.text(20,50,"Clear! Good job!!",1)
                    pyxel.text(20,70,"Let's go to the Next Stage... in "+str(28-self.playtime)+"min",1)
                    if self.playtime > 28 and self.stage.level == 1:
                        self.stage.level = 2
                        self.stage.background = 8
                        self.box.point = 0
                        self.stage.speed = 2
                        self.start = int(time.time())
                if self.box.point < 5:
                    pyxel.text(20,50,"Oh... you failed",1)
                    pyxel.text(20,70,"Please try it again!",1)
            if self.playtime > 23 and self.stage.level == 2:
                pyxel.cls(7)
                if self.box.point >= 10:
                    pyxel.text(20,50,"Clear! Very good job!!",1)
                if self.box.point < 10:
                    pyxel.text(20,50,"Oh... you failed",1)
                    pyxel.text(20,70,"Please try it again!",1)

        # 終了条件はどうしようか(時間制限内に目標点数に行けるかにするか)

App()