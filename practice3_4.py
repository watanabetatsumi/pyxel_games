import pyxel

pyxel.init(200,200)

a = 100
b=0


def update():
    global a
    global b
    if pyxel.btnp(pyxel.KEY_SPACE):
        b+=1
    
    if b%2==0:
        a+=1
    else:
        a-=1

def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)
     


pyxel.run(update, draw)