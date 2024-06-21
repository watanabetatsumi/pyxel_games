import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for b in range(10, 200, 20):
    for a in range(10, 200, 20):
        if a+b <= 100:
            pyxel.circ(a, b, 10, 2)
        elif a+b <= 200:
            pyxel.circ(a, b, 10, 3)
        elif a+b <= 300:
            pyxel.circ(a, b, 10, 6)
        else:
            pyxel.circ(a, b, 10, 14)
pyxel.show()