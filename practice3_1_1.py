import pyxel

pyxel.init(200,200)

a = 100

def update():
    global a
    a += 1

def draw():
    global a
    pyxel.cls(7)
    if a<200:
        pyxel.circ(a, a, 10, 0)
    else:
        a=0
        


pyxel.run(update, draw)