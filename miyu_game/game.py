import pyxel
import random


class Player:
    def __init__(self):
        self.x = 100
        self.y = 370
        self.size = 25
        self.alive = True

    def update_player_right(self):
        if self.x < 160:
            self.x += 60

    def update_player_left(self):
        if self.x > 40:
            self.x -= 60
player = Player()

class Box:
    def __init__(self):
        self.size = 25
        self.x = random.randint(0,2) * 60 + 40
        self.y = 0 - self.size
        self.evil = random.randint(0,3)
        
    
    def update_box(self, player, i, speed,score):
        self.y += 1 * speed
        if (self.y + self.size > player.y - player.size) and (self.x == player.x):
            if self.evil > 0:    
                player.alive = False
                pyxel.playm(0)
            else:
                score += 100
                pyxel.playm(1)
                boxes.pop(i)
        if self.y > 400 + self.size:
            boxes.pop(i)
        return score

boxes = [Box()]
    
class App:
    def __init__(self):
        pyxel.init(200, 400, title="Ball Game")
        self.score = 0
        self.is_alive = True
        self.difficult = 100
        self.speed = 10
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)


    def update(self):
        if player.alive == True:
            if pyxel.btnp(pyxel.KEY_RIGHT):
                player.update_player_right()

            if pyxel.btnp(pyxel.KEY_LEFT):
                player.update_player_left()

            self.len_box = 0

            for i in reversed(range(len(boxes))):
                box = boxes[i]
                self.score = box.update_box(player, i, self.speed,self.score)
                if box.y < 70 + box.size:
                    self.len_box += 1
            if self.len_box < 2 and (pyxel.rndi(1,self.difficult) == 1 or len(boxes) == 0):
                boxes.append(Box())
            self.score += 1
            if self.score > 0 and self.score % 30 == 0:
                self.difficult -= 1
            if self.score > 0 and self.score % 60 == 0:
                self.speed += 0.1
                

    def draw(self):
        if player.alive == True:
            pyxel.cls(11)

            for box in boxes:
                if box.evil > 0:
                    pyxel.rect(box.x-box.size, box.y-box.size, box.size*2, box.size*2, 8)
                else:
                    pyxel.rect(box.x-box.size, box.y-box.size, box.size*2, box.size*2, 3)
            pyxel.circ(player.x, player.y, player.size, 10)

            # Draw score
            s = f"SCORE {self.score:>4}"
            pyxel.text(5, 4, s, 1)
            pyxel.text(4, 4, s, 7)
        else:
            pyxel.cls(11)
            s = f"SCORE {self.score:>4}"
            pyxel.text(80, 200, s, 1)
            

App()
