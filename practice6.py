import pyxel
pyxel.init(200, 200)
pyxel.cls(2)  
for a in range(0, 151, 10):
    pyxel.line(0, a/10, 200, 200-a/10, 4)
for a in range(0, 151, 10):
    pyxel.line(a/10, 0, 200-a/10, 200, 4)
for a in range(0, 151, 10):
    pyxel.line(0, 200+a/10, 200, 0-a/10, 4)
for a in range(0, 151, 10):
    pyxel.line(0, 200-a/10, 200, 0+a/10, 4)
for a in range(0, 1001, 10):
    pyxel.line(0, a, 200, 200-a, 4)
for a in range(0, 1001, 10):
    pyxel.line(a, 0, 200-a, 200, 4)  
for a in range(0, 1001, 10):
    pyxel.line(0, 200-a, 200, 0+a, 4)        
for a in range(0, 1001, 10):
    pyxel.line(200-a,0, 0+a,200, 4)   
for a in range(0,201,10):
    pyxel.line(a,0,0-a/10,200-a,14)
for a in range(0,201,10):
    pyxel.line(200-a,200,200+a/10,a,9)
for a in range(0,201,10):
    pyxel.line(a,0-a/10,200,a,9)
for a in range(0,201,10):
    pyxel.line(0-a/10,a,0+a,200,14)

pyxel.show()