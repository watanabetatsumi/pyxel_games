import pyxel

pyxel.init(200,200)

a = 0

def update():
    global a
    a += 1

def draw():
    global a
    if a<100:
        pyxel.cls(7)
        pyxel.circ(100+a, a, 10, 0)
        pyxel.circ(a, 100-a, 10, 0)
        pyxel.circ(100-a, 200-a, 10, 0)
        pyxel.circ(200-a, 100+a, 10, 0)
    else:
        a=0
        pyxel.cls(7)
        pyxel.circ(100+a, a, 10, 0)
        pyxel.circ(a, 100-a, 10, 0)
        pyxel.circ(100-a, 200-a, 10, 0)
        pyxel.circ(200-a, 100+a, 10, 0)
pyxel.run(update, draw)