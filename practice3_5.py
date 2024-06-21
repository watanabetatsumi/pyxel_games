import pyxel

pyxel.init(200,200)
pyxel.cls(7)
pyxel.mouse(True)

x=0
y=0

def update():
    global x, y
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        x = pyxel.mouse_x
        y = pyxel.mouse_y

def draw():
    global x, y
    pyxel.cls(7)
    pyxel.line(0,0,x,y,0)

pyxel.run(update, draw)