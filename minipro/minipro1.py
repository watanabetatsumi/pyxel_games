import pyxel

# 画面のサイズ, padのサイズを設定
field_size = 150
class Cloud:
    speed = 0.4
    def __init__(self):
        self.x = 20
        self.y = 5
        self.vx = pyxel.cos(180)
        self.vy = pyxel.sin(0)

    def move(self):
        self.x += self.vx * Cloud.speed
        if self.x + 150 <= 0:
            self.restart()

    def restart(self):
        self.x = field_size
        self.y = 5
        self.vx = pyxel.cos(180)
        self.vy = pyxel.sin(0)


class Plane1:
    speed = 1
    def __init__(self):
        self.restart()

    def move(self):
        self.x += self.vx * Plane1.speed

    def restart(self):
        self.x = field_size
        self.y = pyxel.rndi(0, field_size - 10)
        self.vx = pyxel.cos(180)
        self.vy = pyxel.sin(0)

class Plane2:
    speed = 1
    def __init__(self):
        self.restart()

    def move(self):
        self.x += self.vx * Plane2.speed
        self.y += self.vy * Plane2.speed

    def restart(self):
        self.x = field_size
        self.y = pyxel.rndi(0, field_size - 10)
        angle = pyxel.rndi(150, 210)
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)


class Balloon:
    speed = 0.8
    def __init__(self):
        self.restart()

    def move(self):
        self.x += self.vx * Balloon.speed
        self.y += self.vy * Balloon.speed

    def restart(self):
        self.x = pyxel.rndi(70, field_size)
        self.y = field_size
        angle = pyxel.rndi(-90, 0)
        self.vx = pyxel.cos(180)
        self.vy = pyxel.sin(angle)

class Heli:
    speed = 1
    def __init__(self):
        self.restart()

    def move(self):
        self.x += self.vx * Heli.speed
        self.y += self.vy * Heli.speed

        if self.x == field_size / 2:
            angle = pyxel.rndi(150, 210)
            self.vx = pyxel.cos(angle)
            self.vy = pyxel.sin(angle)

    def restart(self):
        self.x = field_size
        self.y = pyxel.rndi(0, field_size - 10)
        self.vx = pyxel.cos(180)
        self.vy = pyxel.sin(0)


class Bird:
    def __init__(self):
        self.y = field_size / 2
        self.height = 12

    def catch(self, plane):
        self.y = pyxel.mouse_y  # マウスの位置を bird.y（bird の中心座標）にする
        if plane.x <= 10 and (self.y - self.height / 2 < plane.y < self.y + self.height / 2):
            return True
        else:
            return False

class App():
    def __init__(self):
        pyxel.init(field_size,field_size)
        pyxel.load("minipro.pyxres")

        # ゲームに必要な変数の設定
        self.clouds = [ Cloud() ]
        self.plane1s = [ Plane1() ]
        self.plane2s = [ Plane2() ]
        self.balloons = [ Balloon() ]
        self.helis = [ Heli() ]
        self.bird = Bird()
        self.alive = True
        self.life = 3
        self.score = 0
        self.dodge_plane2 = 0
        self.dodge_heli = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.alive:
            return
        self.bird.y = pyxel.mouse_y #マウスの位置をbirdx（birdの中心座標）にする

        for cloud in self.clouds:
            cloud.move()

        for plane1 in self.plane1s:
            plane1.move()

            if self.bird.catch(plane1):
                # birdにplane1が当たったら
                pyxel.play(0, [0], loop=False)
                self.life -= 1
                Plane1.speed += 0.2
                plane1.restart()
                self.alive = (self.life > 0)

            elif plane1.x + 23 < 0:
                #birdがplane1を避けられたら
                Plane1.speed += 0.2
                plane1.restart()
                self.score += 1


        for plane2 in self.plane2s:
            plane2.move()

            if self.bird.catch(plane2):
                # birdにplaneが当たったら
                pyxel.play(0, [0], loop=False)
                self.life -= 1
                Plane2.speed += 0.2
                plane2.restart()
                self.alive = (self.life > 0)

            elif plane2.x + 23 < 0:
                #birdがplane2を避けられたら
                self.dodge_plane2 += 1
                Plane2.speed += 0.2
                plane2.restart()
                self.score += 1
                if self.dodge_plane2 >= 10:
                    # plane2を10回以上避けられたら
                    Plane2.speed = 1
                    Plane1.speed = 1
                    self.dodge_plane2 = 0
                    self.plane2s.append(Plane2())


        for balloon in self.balloons:
            balloon.move()

            if self.bird.catch(balloon):
                # birdにballoonが当たったら
                pyxel.play(0, [0], loop=False)
                self.life -= 1
                balloon.restart()
                self.alive = (self.life > 0)

            elif balloon.x + 10 < 0:
                #birdがballoonを避けられたら
                balloon.restart()
                self.score += 1


        for heli in self.helis:
            heli.move()

            if self.bird.catch(heli):
                # birdにheliが当たったら
                pyxel.play(0, [0], loop=False)
                self.life -= 1
                heli.restart()
                self.dodge_heli += 1
                self.alive = (self.life > 0)

            elif heli.x + 15 < 0:
                #birdがheliを避けられたら
                Heli.speed += 0.1
                heli.restart()
                self.score += 1
                if self.dodge_heli >= 15:
                    # heliを15個以上避けられたら
                    Heli.speed = 1
                    self.dodge_heli = 0
                    self.helis.append(Heli())


    def draw(self):
        if self.alive:
            pyxel.cls(6)
            for cloud in self.clouds:
                pyxel.blt(cloud.x, cloud.y, 0, 2, 46, 30, 20,6)
                pyxel.blt(cloud.x + 30, cloud.y + 90, 0, 34, 43, 28, 20,6)
                pyxel.blt(cloud.x + 80, cloud.y + 60, 0, 5, 77, 26, 20,6)
                pyxel.blt(cloud.x + 150, cloud.y + 25, 0, 2, 46, 30, 20,6)
                pyxel.blt(cloud.x + 180, cloud.y + 50, 0, 34, 43, 28, 20,6)
                pyxel.blt(cloud.x + 230, cloud.y + 80, 0, 5, 77, 26, 20,6)
                pyxel.blt(cloud.x - 120, cloud.y + 50, 0, 34, 43, 28, 20,6)
                pyxel.blt(cloud.x - 70, cloud.y + 80, 0, 5, 77, 26, 20,6)
                pyxel.blt(cloud.x - 150, cloud.y + 25, 0, 2, 46, 30, 20,6)
            for plane1 in self.plane1s:
                pyxel.blt(plane1.x, plane1.y, 0, 16, 1, 23, 12, 6)
            for plane2 in self.plane2s:
                pyxel.blt(plane2.x, plane2.y, 0, 16, 1, 23, 12, 6)
            for balloon in self.balloons:
                pyxel.blt(balloon.x, balloon.y, 0, 43, 1, 10, 13, 6)
            for heli in self.helis:
                pyxel.blt(heli.x, heli.y, 0, 1, 19, 15, 11, 6)
            pyxel.blt(10, self.bird.y, 0, 1, 2, 14, 12, 6)
            pyxel.text(5, 5, "score: " + str(self.score), 0)
            pyxel.text(5, 10, "life: " + str(self.life), 0)
        else:
            pyxel.text(field_size / 2 - 20, field_size / 2 - 20, "Game Over!!!", 0)


App()
