import pyxel

pyxel.init(200,200)

a = 100

while a<200:
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)
    pyxel.flip()
    a += 1

a=0

while a<200:
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)
    pyxel.flip()
    a += 1

