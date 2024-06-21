import pyxel

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2
SCENE_GAMECLEAR = 3
start = 4

class App:
    def __init__(self):
        pyxel.init(200, 200)
        pyxel.load("my_resource.pyxres")
        self.player_x = pyxel.width // 2 - 8
        self.player_y = pyxel.height -50
        self.player_dy = 0
        self.is_alive = True
        self.far_cloud = [(-10,  180), (40, 155), (90, 130)]
        self.near_cloud = [(10, 55), (70, 85), (120, 30)]
        self.floor1 = [(i * 60, pyxel.rndi(40, 200), True) for i in range(3)]
        self.floor2 = [(i * 60, pyxel.rndi(40, 200), True) for i in range(1)]
        pyxel.playm(0, loop=True)
        self.scene = SCENE_TITLE
        self.draw = self.draw_play_scene
        pyxel.run(self.update, self.draw)

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = SCENE_PLAY

    def update_play_scene(self):
        if self.player_y <= 0:
            self.scene = SCENE_GAMECLEAR
        if self.player_y >= 200:
            self.scene = SCENE_GAMEOVER

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_player()
        for i, v in enumerate(self.floor1):
            self.floor1[i] = self.update_floor1(*v)
        for i, v in enumerate(self.floor2):
            self.floor2[i] = self.update_floor2(*v)
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            pass
        elif self.scene == SCENE_GAMEOVER:
            self.update_gameover_scene()
        elif self.scene == SCENE_GAMECLEAR:
            self.update_gameclear_scene()

        for i, v in enumerate(self.floor2):
            self.floor2[i] = self.update_floor2(*v)
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            pass
        elif self.scene == SCENE_GAMEOVER:
            self.update_gameover_scene()
        elif self.scene == SCENE_GAMECLEAR:
            self.update_gameclear_scene()


    def update_gameover_scene(self):
        if pyxel.btn(pyxel.KEY_R):
            self.scene = SCENE_PLAY
    def update_gameclear_scene(self):
        if pyxel.btn(pyxel.KEY_RETURN):
            self.scene = SCENE_TITLE


    def update_player(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
        self.player_y += self.player_dy
        self.player_dy = min(self.player_dy + 1, 8)

        if self.player_y > 215:
            if self.is_alive:
                self.is_alive = False
                self.scene = SCENE_GAMEOVER
                pyxel.play(3, 5)
            if self.player_y > 600:
                self.player_x = 72
                self.player_y = -16
                self.player_dy = 0
                self.is_alive = False

    def update_floor1(self, x, y, is_alive):
        if is_alive:
            if (
                self.player_x + 16 >= x
                and self.player_x <= x + 40
                and self.player_y + 16 >= y
                and self.player_y <= y + 8
                and self.player_dy > 0
            ):
                is_alive = False
                self.player_dy = -12
                pyxel.play(3, 3)
        else:
            y += 6
        x -= 4
        if x < -40:
            x += 240
            y = pyxel.rndi(40, 200)
            is_alive = True
        return x, y, is_alive

    def update_floor2(self, x, y, is_alive):
        if is_alive:
            if (
                self.player_x + 16 >= x
                and self.player_x <= x + 40
                and self.player_y + 16 >= y
                and self.player_y <= y + 8
                and self.player_dy > 0
            ):
                is_alive = False
                self.player_dy = -12
                pyxel.play(3, 3)
        else:
            y += 6
        x -= 3
        if x < -40:
            x += 240
            y = pyxel.rndi(40, 200)
            is_alive = True
        return x, y, is_alive
        
    def draw_title_scene(self):
        pyxel.cls(0)
        pyxel.text(86, 90, "Jump Up!!", 9)
        pyxel.text(71, 140, "- PRESS ENTER -", 6)
    def draw_gameover_scene(self):
        pyxel.cls(0)
        pyxel.text(82, 83, "GAME OVER", 7)
        pyxel.text(65, 150, "- PRESS R TO RESTART -", 6)
    def draw_gameclear_scene(self):
        pyxel.cls(14)
        pyxel.text(83, 56, "GAME CLEAR", 7)
        pyxel.text(71, 140, "- PRESS ENTER -", 6)
    def draw_play_scene(self):
        pyxel.cls(12)

        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            # floor1 を描画
            for x, y, is_alive in self.floor1:
                pyxel.blt(x, y, 0, 16, 0, 35, 5)

            # floor2 を描画
            for x, y, is_alive in self.floor2:
                pyxel.blt(x, y, 0, 16, 0, 15, 5)

            # プレイヤーを描画
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 15, 31, 15)

            # 雲を描画
            offset = (pyxel.frame_count // 16) % 160
            for i in range(2):
                for x, y in self.far_cloud:
                    pyxel.blt(x + i * 160 - offset, y, 0, 0, 42, 13, 7, 15)
            offset = (pyxel.frame_count // 8) % 160
            for i in range(2):
                for x, y in self.near_cloud:
                    pyxel.blt(x + i * 160 - offset, y, 0, 0, 42, 13, 7, 15)

        elif self.scene == SCENE_GAMEOVER:
            self.draw_gameover_scene()
        elif self.scene == SCENE_GAMECLEAR:
            self.draw_gameclear_scene()

App()