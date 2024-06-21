import pyxel
import math

class Ring:
    def __init__(self):
        self.x = 100
        self.y = 230
        self.size = 20#ここ
        self.power = 0
        self.power_up = True
        self.angle = 0
        self.angle_up = True
        self.throw_count = 0
        self.radian = 0

    def select_power(self):
        if self.power_up:
            self.power += 1
        else:
            self.power -= 1
        if self.power == 30 or self.power == 0:
            self.power_up = not self.power_up
        if pyxel.btnp(pyxel.KEY_J):
            return 1
        else:
            return 0

    def select_angle(self):
        if self.angle_up:
            self.angle += 5
        else:
            self.angle -= 5
        self.radian = math.radians(self.angle)
        if self.angle == 0 or self.angle == 180:
            self.angle_up = not self.angle_up
        if pyxel.btnp(pyxel.KEY_J):
            return 2
        else:
            return 1
        
    def throw(self):
        if self.power*10 > self.throw_count:
            self.y -= math.sin(self.radian)
            self.x -= math.cos(self.radian)
            self.throw_count += 1
        else:
            for rod in rods:
                if self.x-self.size < rod.x < self.x+self.size and self.y-self.size < rod.y < self.y+self.size:
                    score.score += 10
            score.num_rings += 1
            return 0

rings = [Ring(),Ring(),Ring(),Ring(),Ring(),Ring(),Ring(),Ring(),Ring(),Ring()]


class Rod:
    def __init__(self):
        self.height = 20
        self.wide = 10

rods = []
for i in range(3):
    for j in range(3):
        rod = Rod()
        rod.x = 40 + 60*j
        rod.y = 40 + 60*i
        rods.append(rod)
    
class Score:
    def __init__(self):
        self.score = 0
        self.num_rings = 0

score = Score()
        
    

class App:
    def __init__(self):
        pyxel.init(200, 250, title="Wanage")
        self.scene = 0
        pyxel.run(self.update, self.draw)


    def update(self):
        if score.num_rings < 10:
            if self.scene == 0:
                self.scene = rings[score.num_rings].select_power()
            elif self.scene == 1:
                self.scene = rings[score.num_rings].select_angle()
            else:
                self.scene = rings[score.num_rings].throw()
                

    def draw(self):
        if score.num_rings < 10:
            pyxel.cls(7)

            for rod in rods:
                pyxel.rect(rod.x-(rod.wide/2), rod.y, rod.wide, rod.height, 9)
            for ring in rings:
                pyxel.circb(ring.x, ring.y, ring.size, 0)

            # Draw score
            s = f"score: {score.score}"
            pyxel.text(5, 4, s, 0)
            r = f"rings: {10-score.num_rings}"
            pyxel.text(5, 14, r, 0)


            pyxel.rect(170, 200, 20, 30, 8)
            pyxel.rect(170, 200, 20, 30-rings[score.num_rings].power, 7)
            pyxel.rectb(170, 200, 20, 30, 0)
            pyxel.text(170, 190, "Power", 0)
            pyxel.text(130, 190, "Angle", 0)
            pyxel.line(140, 230, 140-20*math.cos(rings[score.num_rings].radian), 230-20*math.sin(rings[score.num_rings].radian), 0)
            if self.scene == 0:
                pyxel.text(167, 233, "press J", 0)  
                
            elif self.scene == 1:
                pyxel.text(127, 233, "press J", 0)

        else:
            pyxel.cls(7)
            s = f"score: {score.score}"
            pyxel.text(80, 125, s, 0)

App()
