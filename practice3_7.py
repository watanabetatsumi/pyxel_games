import pyxel

pyxel.init(200,200)
pyxel.cls(7)
pyxel.mouse(True)

x=0
y=0
z=0
w=0
a=0

def update():
    global x,y,w,z,a
    if a==1:
        w = pyxel.mouse_x
        z = pyxel.mouse_y
        if pyxel.btnp(pyxel.KEY_SPACE):
            a=0
            
    else:
      
        if pyxel.btnp(pyxel.KEY_SPACE):
            w = pyxel.mouse_x
            z = pyxel.mouse_y
            x = pyxel.mouse_x
            y = pyxel.mouse_y
            a = 1
            

        
 
def draw():
    pyxel.cls(7)
    global x,y,w,z
    pyxel.line(x,y,w,z,0)

pyxel.run(update,draw)