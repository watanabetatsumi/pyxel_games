import pyxel

class Bullet:
    def __init__(self):
        self.y = 0  # 初期化した時には弾が見えないように最上段に置く。
        self.pdx = pyxel.mouse_x

    def start(self):
        self.y = 200  # start()が呼ばれたら下端に戻すようにする。
        self.pdx = pyxel.mouse_x

    def move(self):
        self.y -= 5

    def draw(self):
        pyxel.circ(self.pdx, self.y, 2, 5)

class App:
    def __init__(self):
        pyxel.init(200,200)
        pyxel.mouse(True)
        self.bullet = Bullet()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):  
            self.bullet.start()
        self.bullet.move()

    def draw(self):
        pyxel.cls(7)
        self.bullet.draw()

App()