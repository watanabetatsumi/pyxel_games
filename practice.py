import pyxel
pyxel.init(200,200)
pyxel.cls(7)
for a in range(0,101,10):
    pyxel.line(a,0,100+a,200,1)
pyxel.show()