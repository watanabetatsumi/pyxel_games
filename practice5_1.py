import pyxel

pyxel.init(200,200)#画面の大きさ
pyxel.mouse(True)#カーソルの軌跡
pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)#サウンドの設定
pyxel.sound(1).set(notes='A2C3', tones='NN', volumes='33', effects='NN', speed=10)

ballx = [pyxel.rndi(0, 199), pyxel.rndi(0, 199), pyxel.rndi(0, 199)]  #ボールの初期位置のx座標(0~199のランダム)
bally = [0, 0, 0] #ｙの座標
padx = 100 
score=0
angle = [pyxel.rndi(30, 150), pyxel.rndi(30, 150),pyxel.rndi(30, 150)] #ボールの軌跡
vx = [pyxel.cos(angle[0]), pyxel.cos(angle[1]), pyxel.cos(angle[2])] 
vy = [pyxel.sin(angle[0]), pyxel.sin(angle[1]), pyxel.sin(angle[2])]

def update():
    global ballx, bally, vx, vy,padx,score
    for i in range(0, len(ballx)):　#リストの分だけ球を増やす
        padx = pyxel.mouse_x
        if ballx[i] >= 200 or ballx[i] <= 0:#よこの壁にぶつかったとき
            vx[i] = vx[i] * -1#式に－1を入れることで恒常的に負となる
    
        ballx[i] += vx[i]　#ボールが落ちる
        bally[i] += vy[i]
    
        if bally[i] >= 200:　#ボールをとらえきれなかったとき
            pyxel.play(0,0)　#失敗の音
            ballx[i] = pyxel.rndi(0,199)　#設定の初期化
            bally[i] = 0
            angle[i] = pyxel.rndi(30, 150)
            vx[i] = pyxel.cos(angle[i])
            vy[i] = pyxel.sin(angle[i])
    
        if 195< bally[i] and padx -20 < ballx[i] < padx +40:#ボールをとらえきれたとき
            score += 10#点が入る
            pyxel.play(0,1)#成功の音
            ballx[i] = pyxel.rndi(0,199)#設定の初期化
            bally[i] = 0
            angle[i] = pyxel.rndi(30, 150)
            vx[i] = pyxel.cos(angle[i])
            vy[i] = pyxel.sin(angle[i])
    

def draw():
    global ballx, bally, vx, vy, padx,score
    pyxel.cls(7)#軌跡を消す
    for i in range(0, len(ballx)):
        pyxel.circ(ballx[i], bally[i], 10, 6)#表示
        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.text(100,30,'you got:'+str(score),1)

pyxel.run(update, draw)