import pyxel
pyxel.init(200,200)
pyxel.cls(7)
for a in range(0,201,10):
    pyxel.line(a,0,0-a/10,200-a,1)
pyxel.show()