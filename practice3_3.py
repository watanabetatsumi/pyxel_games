import pyxel

pyxel.init(200,200)

a = 100

def update():
    global a
    if a<400:
        a += 1
    else:
        a=0

def draw():
    global a
    pyxel.cls(7)
    if a<200:
        pyxel.circ(a, a, 10, 0)
    else:
        pyxel.circ(200-(a-200), 200-(a-200), 10, 0)


pyxel.run(update, draw)