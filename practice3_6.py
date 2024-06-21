import pyxel

pyxel.init(200,200)
pyxel.cls(7)
pyxel.mouse(True)

x=0
y=0
z=0
w=0

def update():
    global x,y,w,z
    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.cls(7)
        x = pyxel.mouse_x
        y = pyxel.mouse_y
    if pyxel.btn(pyxel.KEY_SPACE):
        pass
    if pyxel.btnr(pyxel.KEY_SPACE):
        z= pyxel.mouse_x
        w= pyxel.mouse_y
    

def draw():
    pyxel.cls(7)
    global x,y,w,z
    if w>0 and z>0:
        pyxel.line(x,y,z,w,0)

pyxel.run(update,draw)