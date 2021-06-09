import pygame, sys, random, os, colorsys, time
pygame.init()
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("  I. R. L")


walkLeft= [pygame.image.load('left_10.png'),pygame.image.load('left_09.png'),pygame.image.load('left_08.png'),pygame.image.load('left_07.png'),pygame.image.load('left_06.png'), pygame.image.load('left_05.png'), pygame.image.load('left_04.png'),pygame.image.load('left_03.png'), pygame.image.load('left_02.png') ]
walkRight= [pygame.image.load('right_04.png'),pygame.image.load('right_05.png'),pygame.image.load('right_06.png'),pygame.image.load('right_07.png'), pygame.image.load('right_08.png'),pygame.image.load('right_09.png'),pygame.image.load('right_10.png'),pygame.image.load('right_11.png'),pygame.image.load('right_12.png')]
bg=pygame.image.load('pozadina.png')
ikonica=pygame.image.load('ikonica.png')
pygame.display.set_icon(ikonica)
walkLeftB= [pygame.image.load('left_10b.png'),pygame.image.load('left_09b.png'),pygame.image.load('left_08b.png'),pygame.image.load('left_07b.png'),pygame.image.load('left_06b.png'), pygame.image.load('left_05b.png'), pygame.image.load('left_04b.png'),pygame.image.load('left_03b.png'), pygame.image.load('left_02b.png')]
walkRightB= [pygame.image.load('right_04b.png'),pygame.image.load('right_05b.png'),pygame.image.load('right_06b.png'),pygame.image.load('right_07b.png'), pygame.image.load('right_08b.png'),pygame.image.load('right_09b.png'),pygame.image.load('right_10b.png'),pygame.image.load('right_11b.png'),pygame.image.load('right_12.png')]

neprijateljImage=[pygame.image.load ('simbolbs_04.png'),pygame.image.load ('simbolbs_05.png'),pygame.image.load ('simbolbs_06.png'),pygame.image.load ('simbolbs_07.png')]
char=pygame.image.load("left_12.png")
char2=pygame.image.load("skok.png")
char3=pygame.image.load("skok.png")
pocetna=pygame.image.load("pocetna2.png")
glava=pygame.image.load("glava2.png")
glave=[pygame.image.load('glava2.png'),pygame.image.load('glava2.png'),pygame.image.load('glava2.png')]
eksplozija=[pygame.image.load('eks1.png'), pygame.image.load('eks2.png'), pygame.image.load('eks3.png'), pygame.image.load('eks4.png'), pygame.image.load('eks5.png'), pygame.image.load('eks6.png'), pygame.image.load('eks7.png'), pygame.image.load('eks8.png'),pygame.image.load('eks9.png'),pygame.image.load('eks10.png'),pygame.image.load('eks11.png'),pygame.image.load('eks12.png'),pygame.image.load('eks13.png'), pygame.image.load('eks14.png'),pygame.image.load('eks15.png')]
eksplozija2=[pygame.image.load('eks01.png'), pygame.image.load('eks02.png'), pygame.image.load('eks03.png'), pygame.image.load('eks04.png'), pygame.image.load('eks05.png'), pygame.image.load('eks06.png'), pygame.image.load('eks07.png'), pygame.image.load('eks08.png'),pygame.image.load('eks09.png'),pygame.image.load('eks010.png'),pygame.image.load('eks011.png'),pygame.image.load('eks012.png'),pygame.image.load('eks013.png'), pygame.image.load('eks014.png'),pygame.image.load('eks015.png')]
bezPostolja=pygame.image.load("Bezpostolja.png")
zastava=[pygame.image.load('zastava 1.png'),pygame.image.load('zastava 2.png'), pygame.image.load('zastava 3.png'), pygame.image.load('zastava 4.png'),pygame.image.load('zastava 5.png'), pygame.image.load('zastava 6.png'), pygame.image.load('zastava 7.png'),pygame.image.load('zastava 8.png'), pygame.image.load('zastava 9.png'), pygame.image.load('zastava 10.png'), pygame.image.load('zastava 11.png'), pygame.image.load('zastava 12.png'), pygame.image.load('zastava 13.png'),pygame.image.load('zastava 14.png'), pygame.image.load('zastava 15.png'), pygame.image.load('zastava 16.png'), pygame.image.load('zastava 17.png'), pygame.image.load('zastava 18.png'), pygame.image.load('zastava 19.png'), pygame.image.load('zastava 20.png'), pygame.image.load('zastava 21.png'), pygame.image.load('zastava 22.png'), pygame.image.load('zastava 23.png'), pygame.image.load('zastava 24.png'), pygame.image.load('zastava 25.png'), pygame.image.load('zastava 26.png'), pygame.image.load('zastava 27.png'), pygame.image.load('zastava 28.png'), pygame.image.load('zastava 29.png'), pygame.image.load('zastava 30.png'), pygame.image.load('zastava 31.png'), pygame.image.load('zastava 32.png'), pygame.image.load('zastava 33.png'), pygame.image.load('zastava 34.png'), pygame.image.load('zastava 35.png'), pygame.image.load('zastava 36.png'), pygame.image.load('zastava 37.png'), pygame.image.load('zastava 38.png'),pygame.image.load('zastava 39.png'), pygame.image.load('zastava 40.png'), pygame.image.load('zastava 41.png'), pygame.image.load('zastava 42.png'), pygame.image.load('zastava 43.png'), pygame.image.load('zastava 44.png'), pygame.image.load('zastava 45.png'), pygame.image.load('zastava 46.png'), pygame.image.load('zastava 47.png'),pygame.image.load('zastava 48.png'),pygame.image.load('zastava 49.png'), pygame.image.load('zastava 50.png'), pygame.image.load('zastava 51.png'),pygame.image.load('zastava 52.png'),pygame.image.load('zastava 53.png'), pygame.image.load('zastava 54.png'), pygame.image.load('zastava 55.png'), pygame.image.load('zastava 56.png'),pygame.image.load('zastava 57.png'), pygame.image.load('zastava 58.png'), pygame.image.load('zastava 59.png'), pygame.image.load('zastava 60.png'), pygame.image.load('zastava 61.png'), pygame.image.load('zastava 62.png'), pygame.image.load('zastava 63.png'), pygame.image.load('zastava 64.png'), pygame.image.load('zastava 65.png'), pygame.image.load('zastava 66.png'), pygame.image.load('zastava 67.png'), pygame.image.load('zastava 68.png'), pygame.image.load('zastava 69.png'), pygame.image.load('zastava 70.png'), pygame.image.load('zastava 71.png'), pygame.image.load('zastava 72.png'),pygame.image.load('zastava 73.png'), pygame.image.load('zastava 74.png')]
zastavaViori=[pygame.image.load('frejm 1.png'), pygame.image.load('frejm 2.png'),pygame.image.load('frejm 3.png'),pygame.image.load('frejm 4.png'),pygame.image.load('frejm 5.png'),pygame.image.load('frejm 6.png'),pygame.image.load('frejm 7.png'),pygame.image.load('frejm 8.png'),pygame.image.load('frejm 9.png'),pygame.image.load('frejm 10.png'),pygame.image.load('frejm 11.png'),pygame.image.load('frejm 12.png'),pygame.image.load('frejm 13.png'), pygame.image.load('frejm 14.png')]
mainClock = pygame.time.Clock()
drugiLevel=False
treciLevel=False
treciL=False
treciLevel2 = False
cetvrtiL=False
cetvrtiLevel=False
kraj=False
prelazDrugi= pygame.image.load("level 2.png")
poslednjiFZastava=pygame.image.load("zastava 74.png")
neprijateljImage2=[pygame.image.load("BOMBA.png"),pygame.image.load("AK47.png"), pygame.image.load("BOMBA2.png"),pygame.image.load("AK472.png")]
neprijateljImage3=[pygame.image.load("izbegavati1.png"),pygame.image.load("izbegavati2.png"), pygame.image.load("izbegavati1.png"),pygame.image.load("izbegavati2.png")]
neprijateljImage4=[pygame.image.load("izbegavati41.png"),pygame.image.load("izbegavati42.png"),pygame.image.load("izbegavati41.png"),pygame.image.load("izbegavati42.png")]

coinsImage=[pygame.image.load ('simbol_01.png'), pygame.image.load ('simbol_02.png'), pygame.image.load ('simbol_03.png')]
coinsImage2=[pygame.image.load("coin1.png"), pygame.image.load("coin2.png"), pygame.image.load("coin3.png")]
coinsImage3=[pygame.image.load("sakupljanje1.png"), pygame.image.load("sakupljanje2.png"), pygame.image.load("sakupljanje3.png")]
coinsImage4=[pygame.image.load("sakupljati41.png"), pygame.image.load("sakupljati42.png"), pygame.image.load("sakupljati43.png")]

levelTriPozadina=pygame.image.load("pozadinalevel3.png")
poza=pygame.image.load("poza3level.png")
poza2=pygame.image.load("poza3level.png")
pomocna=pygame.image.load("pomocna.png")
pomocna2=pygame.image.load("pomocna2.png")
levelCetiriPozadina=pygame.image.load("level4.png")
brojGlava=3
zavrsna=pygame.image.load("zavrsna2.png")
#brzinaSlike=10
score2=0
score3=0
score4=0
x=650
y=510
width=56
height=64
vel=10

isJump=False
jumpCount=10
isJump2=False
jumpCount2=10
left= False
right=False
walkCount=0

score=0
zivot=3
brzinaNeprijatelja=10


music=pygame.mixer.music.load("musicCut.mp3")
pygame.mixer.music.play(-1)
pain= pygame.mixer.Sound("pain.wav")
explosionShort= pygame.mixer.Sound("explosionShort.wav")
coinSound=pygame.mixer.Sound("coin.wav")
explosionBig=pygame.mixer.Sound("explosionBig.wav")
jumpSound=pygame.mixer.Sound("jump.wav")
teleportation=pygame.mixer.Sound("teleportation2.wav")


def show_go_screen():
    screen.blit(pocetna,(0,0))

    pygame.display.flip()
    waiting=True
    while waiting:
        mainClock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            waiting=False

def importneprijatelj():
    global bn
    bn = 0
    for enemy in enemies:
        if bn < 4:
            screen.blit(neprijateljImage[bn], ([enemy[0], enemy[1], 76, 146]))
            bn = bn + 1
        else:
            bn = 0
            screen.blit(neprijateljImage[bn], ([enemy[0], enemy[1], 76, 146]))
            bn = bn + 1

def importneprijatelj2():
    global bn2
    bn2 = 0
    for enemy2 in enemies2:
        if bn2 < 4:

            screen.blit(neprijateljImage2[bn2], ([enemy2[0], enemy2[1], 39, 131]))
            bn2 = bn2 + 1
        else:
            bn2 = 0
            screen.blit(neprijateljImage2[bn2], ([enemy2[0], enemy2[1], 39, 131]))
            bn2 = bn2 + 1
def importneprijatelj3():
    global bn3
    bn3 = 0
    for enemy3 in enemies3:
        if bn3 < 4:

            screen.blit(neprijateljImage3[bn3], ([enemy3[0], enemy3[1], 76, 146]))
            bn3 = bn3 + 1
        else:
            bn3 = 0
            screen.blit(neprijateljImage3[bn3], ([enemy3[0], enemy3[1], 76, 146]))
            bn3 = bn3 + 1

def importneprijatelj4():
    global bn4
    bn4 = 0
    for enemy4 in enemies4:
        if bn4 < 4:

            screen.blit(neprijateljImage4 [bn4], ([enemy4[0], enemy4[1], 76, 146]))
            bn4 = bn4 + 1
        else:
            bn4 = 0
            screen.blit(neprijateljImage4[bn4], ([enemy4[0], enemy4[1], 76, 146]))
            bn4 = bn4 + 1
enemies2=[]
enemies3=[]
enemies4=[]
e2=random.randint(4,5)
e3=random.randint(4,5)
e4=random.randint(4,5)
for nep2 in range(e2):
    neprijateljX2 = random.randint(0, 1300)
    neprijateljY2 = random.randint(-800,-146)
    enemies2.append([neprijateljX2,neprijateljY2])
for nep3 in range(e3):
    neprijateljX3 = random.randint(0, 1300)
    neprijateljY3 = random.randint(-800,-146)
    enemies3.append([neprijateljX3,neprijateljY3])
for nep4 in range(e4):
    neprijateljX4 = random.randint(0, 1300)
    neprijateljY4 = random.randint(-800,-146)
    enemies4.append([neprijateljX4,neprijateljY4])

enemies=[]
e=random.randint(4,5)
for nep in range(e):
    neprijateljX = random.randint(0, 1300)
    neprijateljY = random.randint(-800,-146)
    enemies.append([neprijateljX,neprijateljY])

def all_same(items):
    return all(x == items[0] for x in items)
def all_same2(items2):
    return all(x2 == items2[0] for x2 in items2)
def all_same3(items3):
    return all(x3 == items3[0] for x3 in items3)
def all_same4(items4):
    return all(x4 == items4[0] for x4 in items4)
def importCoins():
    global b
    b=0
    for i in coins:
        if b < 3:
            screen.blit(coinsImage[b], ([i[0], i[1], 76, 146]))
            b = b + 1
        else:
            b = 0
            screen.blit(coinsImage[b], ([i[0], i[1], 76, 146]))
            b = b + 1
def importCoins2():
    global b2
    b2=0
    for ii in coinss:
        if b2 < 3:
            screen.blit(coinsImage2[b2], ([ii[0], ii[1], 61, 107]))
            b2 = b2 + 1
        else:
            b2 = 0
            screen.blit(coinsImage2[b2], ([ii[0], ii[1], 61, 107]))
            b2 = b2 + 1
def importCoins3():
    global b3
    b3=0
    for iii in coinsss:
        if b3 < 3:
            screen.blit(coinsImage3[b3], ([iii[0], iii[1], 61, 107]))
            b3 = b3 + 1
        else:
            b3 = 0
            screen.blit(coinsImage3[b3], ([iii[0], iii[1], 61, 107]))
            b3 = b3 + 1
def importCoins4():
    global b4
    b4=0
    for iiii in coinssss:
        if b4 < 3:
            screen.blit(coinsImage4[b4], ([iiii[0], iiii[1], 61, 107]))
            b4 = b4 + 1
        else:
            b4 = 0
            screen.blit(coinsImage4[b4], ([iiii[0], iiii[1], 61, 107]))
            b4 = b4 + 1
coins = []
c=random.randint(2,5)
for i in range(c):
    xCoin = random.randint(0,1292)
    yCoin = 550
    if xCoin>x+76 or xCoin<x-70:
        coins.append([xCoin, yCoin])
    else:
        xCoin=xCoin+150
        if xCoin<1292:
            coins.append([xCoin,yCoin])

coinss = []
coinsss = []
coinssss = []

cc=random.randint(2,5)
ccc=random.randint(2,5)
cccc=random.randint(2,5)


for i2 in range(cc):
    xCoin2 = random.randint(0,1292)
    yCoin2 = 589
    if xCoin2>x+61 or xCoin2<x-61:
        coinss.append([xCoin2, yCoin2])
    else:
        xCoin2=xCoin2+150
        if xCoin2<1292:
            coinss.append([xCoin2,yCoin2])
for i3 in range(ccc):
    xCoin3 = random.randint(0,1292)
    yCoin3 = 589
    if xCoin3>x+61 or xCoin3<x-61:
        coinsss.append([xCoin3, yCoin3])
    else:
        xCoin3=xCoin3+150
        if xCoin3<1292:
            coinsss.append([xCoin3,yCoin3])
for i4 in range(cccc):
    xCoin4 = random.randint(0,1292)
    yCoin4 = 589
    if xCoin4>x+61 or xCoin4<x-61:
        coinssss.append([xCoin4, yCoin4])
    else:
        xCoin4=xCoin4+150
        if xCoin4<1292:
            coinssss.append([xCoin4,yCoin4])

coins.sort(key=lambda m: m[0])

coinss.sort(key=lambda m2: m2[0])
coinsss.sort(key=lambda m3: m3[0])
coinssss.sort(key=lambda m4: m4[0])
for broj in range(c-1):
    if not coins[c-1-broj][0] - coins[c-1-broj-1][0]>76:
        print(coins[c - 1 - broj - 1])
        coins.pop(c-1-broj-1)

    else:
        print('valja')
for brojj in range(cc-1):
    if not coinss[cc-1-brojj][0] - coinss[cc-1-brojj-1][0]>61:
        print(coinss[cc - 1 - brojj - 1])
        coinss.pop(cc-1-brojj-1)

    else:
        print('valja')
for brojjj in range(ccc-1):
    if not coinsss[ccc-1-brojjj][0] - coinsss[ccc-1-brojjj-1][0]>61:
        print(coinsss[ccc - 1 - brojjj - 1])
        coinsss.pop(ccc-1-brojjj-1)

    else:
        print('valja')
for brojjjj in range(cccc-1):
    if not coinssss[cccc-1-brojjjj][0] - coinssss[cccc-1-brojjjj-1][0]>61:
        print(coinssss[cccc - 1 - brojjjj - 1])
        coinssss.pop(cccc-1-brojjjj-1)

    else:
        print('valja')
coins2 = []
coinss2 = []
coinsss2 = []
coinssss2 = []
for clan in coins:
    coins2.append(clan)
random.shuffle(coins)

for clann in coinss:
    coinss2.append(clann)
random.shuffle(coinss)

for clannn in coinsss:
    coinsss2.append(clannn)
random.shuffle(coinsss)
for clannnn in coinssss:
    coinssss2.append(clannnn)
random.shuffle(coinssss)
coins3=[]
for clan2 in coins2:
    coins3.append(clan2)

coins32=[]
for clan22 in coinss2:
    coins32.append(clan22)
coins33=[]
for clan23 in coinsss2:
    coins33.append(clan23)
coins34=[]
for clan24 in coinssss2:
    coins34.append(clan24)
def redrawGameWin():
    global walkCount
    screen.fill((255, 255, 204))
    screen.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left and isJump:
        screen.blit(walkLeftB[walkCount // 3], (x, y))
        walkCount += 1

    if right and isJump:
        screen.blit(walkRightB[walkCount // 3], (x, y))
        walkCount += 1

    if left and not isJump:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount+=1
    if right and not isJump:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount+=1
    if isJump and not left and not right:
        screen.blit(char2, (x,y))

    if not left and not right and not isJump:
       screen.blit(char, (x, y))
def redrawGameWin2():
    global walkCount
    screen.fill((255, 255, 204))
    screen.blit(bezPostolja, (0, 0))
    screen.blit(poslednjiFZastava, (597, 283))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left and isJump:
        screen.blit(walkLeftB[walkCount // 3], (x, y))
        walkCount += 1

    if right and isJump:
        screen.blit(walkRightB[walkCount // 3], (x, y))
        walkCount += 1

    if left and not isJump:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount+=1
    if right and not isJump:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount+=1
    if isJump and not left and not right:
        screen.blit(char2, (x,y))

    if not left and not right and not isJump:
       screen.blit(char, (x, y))
def redrawGameWin3():
    global walkCount
    screen.fill((255, 255, 204))
    screen.blit(levelTriPozadina, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left and isJump:
        screen.blit(walkLeftB[walkCount // 3], (x, y))
        walkCount += 1

    if right and isJump:
        screen.blit(walkRightB[walkCount // 3], (x, y))
        walkCount += 1

    if left and not isJump:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount+=1
    if right and not isJump:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount+=1
    if isJump and not left and not right:
        screen.blit(char2, (x,y))

    if not left and not right and not isJump:
       screen.blit(char, (x, y))

def redrawGameWin4():
    global walkCount
    screen.fill((255, 255, 204))
    screen.blit(levelCetiriPozadina, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left and isJump:
        screen.blit(walkLeftB[walkCount // 3], (x, y))
        walkCount += 1

    if right and isJump:
        screen.blit(walkRightB[walkCount // 3], (x, y))
        walkCount += 1

    if left and not isJump:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount+=1
    if right and not isJump:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount+=1
    if isJump and not left and not right:
        screen.blit(char2, (x,y))

    if not left and not right and not isJump:
       screen.blit(char, (x, y))

game_over= True
running = True



while running:

    if score<=100:
        print("ninaaaa")
        mainClock.tick(27)
        if game_over:
            show_go_screen()
            brojGlava=3
            for i in range(brojGlava):
                screen.blit(glava, (1108 + i * 70, 90))
            game_over = False
            print("da")
            x = 650
            y = 510
            width = 56
            height = 64
            vel = 10

            isJump = False
            jumpCount = 10
            left = False
            right = False
            walkCount = 0

            score = 0
            zivot = 3
            brzinaNeprijatelja = 20


        #mainClock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys= pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and  x>vel:
            x-=vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and  x< 1366 - width- vel:
            x+=vel
            left = False
            right = True
        else:
            left = False
            right = False
            walkCount = 0
        if not(isJump):
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] :
                isJump = True
                left = False
                right =False
                walkCount = 0

        else:
            if jumpCount >=-10:
                neg=1
                if jumpCount<0:
                    neg=-1
                y-= (jumpCount**2) * 0.5 * neg
                jumpCount-=1
            else:
                isJump = False
                jumpCount = 10

        redrawGameWin()

        importCoins()
        for j in coins:
            if x>=j[0]-76 and x<=j[0]+76 and y>450:
                coinSound.play()
                cuvajIndeks = coins.index(j)
                if cuvajIndeks%3==0:
                    score=score+1
                if cuvajIndeks%3==1:
                    score=score+2
                if cuvajIndeks%3==2:
                    score=score+4
                coins.remove(j)
                coins.insert(cuvajIndeks, [-200,0])
                if all_same(coins):
                    for q in range(len(coins)):
                        coins.pop()
                    c2 = random.randint(2, 5)
                    for w in range(c2):
                        xCoin2 = random.randint(0, 1290)
                        yCoin2 = 550
                        if xCoin2 > x + 76 and xCoin2<1290 or xCoin2 < x - 70 and x>0:
                            coins.append([xCoin2, yCoin2])
                        else:
                            xCoin2 = xCoin2 + 150
                            if xCoin2 < 1290 and xCoin2>0:
                                coins.append([xCoin2, yCoin2])
                    coins.sort(key=lambda e: e[0])
                    duzinaNiza = len(coins)
                    for broj2 in range(len(coins)-1):
                        if not coins[duzinaNiza - 1 - broj2][0] - coins[duzinaNiza - 1 - broj2 - 1][0] > 76:
                            coins.pop(c2 - 1 - broj2 - 1)
                    random.shuffle(coins)

        font2 = pygame.font.SysFont('Calibri', 150, True, False)
        gameOver = font2.render("KRAJ", True, (255, 255, 255))
        importneprijatelj()
        for brojNep in range (e):
            enemies[brojNep][1]+=brzinaNeprijatelja
            if  enemies[brojNep][1]>610:
                neprijateljX = random.randint(0, 1300)
                neprijateljY = random.randint(-1000, -146)
                enemies[brojNep][1]=neprijateljY
                enemies[brojNep][0]=neprijateljX

        for neprijatelj in enemies:
            if x>=neprijatelj[0]-30 and x<=neprijatelj[0]+30 and y-neprijatelj[1]<20 and y-neprijatelj[1]>0:
                if zivot>=1:
                    zivot-=1
                    brojGlava=brojGlava-1
                    pain.play()
                    screen.blit(eksplozija[0], (x, y))
                if zivot==0:
                    vreme=pygame.time.get_ticks()
                    explosionShort.play()
                    screen.blit(eksplozija[0], (x, y))
                    for eks in range(75):
                        explosionBig.play()
                        if eks<5:

                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[0],(x,y))
                            pygame.display.update()

                        if 5<=eks<10:
                            screen.blit(bg,(0,0))
                            screen.blit(eksplozija[1], (x, y))
                            pygame.display.update()
                        if 10<=eks<15:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[2], (x, y))
                            pygame.display.update()
                        if 15 <= eks < 20:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[3], (x, y))
                            pygame.display.update()
                        if 20 <= eks < 25:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[4], (x, y))
                            pygame.display.update()
                        if 25 <= eks < 30:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[5], (x, y))
                            pygame.display.update()
                        if 30<=eks<35:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[6], (x, y))
                            pygame.display.update()
                        if 35<=eks < 40:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[7], (x, y))
                            pygame.display.update()
                        if 40<=eks < 45:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[8], (x, y))
                            pygame.display.update()
                        if 45<=eks<50:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[9], (x, y))
                            pygame.display.update()
                        if 50<=eks < 55:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[10], (x, y))
                            pygame.display.update()
                        if 55<=eks < 60:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[11], (x, y))
                            pygame.display.update()
                        if 60<=eks < 65:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[12], (x, y))
                            pygame.display.update()
                        if 65<=eks < 70:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[13], (x, y))
                            pygame.display.update()
                        if 70<=eks < 75:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[14], (x, y))
                            pygame.display.update()
                            game_over = True
                        #pygame.time.delay(50)

                        #pygame.display.update()
                    #if pygame.time.get_ticks()-15>=vremePre:
                    #game_over=True

        font = pygame.font.SysFont('Video', 30, False, False)
        text = font.render(str(score)+ '%', True, (219, 215, 215))
        if score<100:
            pygame.draw.rect(screen,(105,103,103), (1100, 50, 200, 20))
            pygame.draw.rect(screen, (169, 63, 63), (1100, 50, score*2, 20))
            screen.blit(text, (1188, 52))
        if score>=100:
            score=100
            pygame.draw.rect(screen, (105, 103, 103), (1100, 50, 200, 20))
            pygame.draw.rect(screen, (169, 63, 63), (1100, 50, score * 2, 20))
            screen.blit(text, (1188, 52))
        for i in range(brojGlava):
            screen.blit(glava,(1108+i*70,90))

    if score==100:

        screen.blit(bg,(0,0))
        xEks=590
        yEks=200
        for eks2 in range(600):
            explosionBig.play()
            if eks2 < 40:
                screen.blit(bg, (0, 0))
                screen.blit(eksplozija2[0], (xEks,yEks))
                pygame.display.update()
            if 40 <= eks2 < 80:
                screen.blit(bg, (0, 0))
                screen.blit(eksplozija2[1], (xEks,yEks))
                pygame.display.update()
            if 80 <= eks2 < 120:
                screen.blit(bg, (0, 0))
                screen.blit(eksplozija2[2], (xEks,yEks))
                pygame.display.update()
            if 120 <= eks2 < 160:
                screen.blit(bg, (0, 0))
                screen.blit(eksplozija2[3], (xEks,yEks))
                pygame.display.update()
            if 160 <= eks2 < 200:
                screen.blit(bg, (0, 0))
                screen.blit(eksplozija2[4], (xEks,yEks))
                pygame.display.update()
            if 200 <= eks2 < 240:
                screen.blit(bg, (0, 0))
                screen.blit(eksplozija2[5], (xEks,yEks))
                pygame.display.update()
            if 240 <= eks2 < 280:
                screen.blit(bg, (0, 0))
                screen.blit(eksplozija2[6], (xEks,yEks))
                pygame.display.update()
            if 280 <= eks2 < 320:
                screen.blit(bg, (0, 0))
                screen.blit(eksplozija2[7], (xEks,yEks))
                pygame.display.update()
            if 320 <= eks2 < 360:
                screen.blit(prelazDrugi, (0, 0))
                screen.blit(eksplozija2[8], (xEks,yEks))
                pygame.display.update()
            if 360 <= eks2 < 400:
                screen.blit(prelazDrugi, (0, 0))
                screen.blit(eksplozija2[9], (xEks,yEks))
                pygame.display.update()
            if 400 <= eks2 < 440:
                screen.blit(prelazDrugi, (0, 0))
                screen.blit(eksplozija2[10], (xEks,yEks))
                pygame.display.update()
            if 440 <= eks2 < 480:
                screen.blit(prelazDrugi, (0, 0))
                screen.blit(eksplozija2[11], (xEks,yEks))
                pygame.display.update()
            if 480 <= eks2 < 520:
                screen.blit(prelazDrugi, (0, 0))
                screen.blit(eksplozija2[12], (xEks,yEks))
                pygame.display.update()
            if 520 <= eks2 < 560:
                screen.blit(prelazDrugi, (0, 0))
                screen.blit(eksplozija2[13], (xEks,yEks))
                pygame.display.update()
            if 560 <= eks2 < 600:
                screen.blit(prelazDrugi, (0, 0))
                screen.blit(eksplozija2[14], (xEks,yEks))
                pygame.display.update()


        for zas in range(74):
            print(zas)
            if drugiLevel==True and zas==73:
                 break
            else:
                 screen.blit(zastava[zas], (597,283))
                 pygame.display.update()
                 screen.blit(bezPostolja, (0, 0))
                 drugiLevel=True
        score = 101
        print(drugiLevel)
    if drugiLevel:
        screen.blit(bezPostolja, (0, 0))
        screen.blit(poslednjiFZastava,(597,283))

        mainClock.tick(27)

        # mainClock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 1366 - width - vel:
            x += vel
            left = False
            right = True
        else:
            left = False
            right = False
            walkCount = 0
        if not (isJump):
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                isJump = True
                left = False
                right = False
                walkCount = 0

        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

        redrawGameWin2()
        importCoins2()
        for j2 in coinss:
            if x >= j2[0] - 61 and x <= j2[0] + 61 and y>450:
                coinSound.play()
                cuvajIndeks2 = coinss.index(j2)
                if cuvajIndeks2 % 3 == 0:
                    score2 = score2 + 1

                if cuvajIndeks2 % 3 == 1:
                    score2 = score2 + 2
                if cuvajIndeks2 % 3 == 2:
                    score2 = score2 + 4
                coinss.remove(j2)
                coinss.insert(cuvajIndeks2, [-200, 0])
                print(score2)
                if all_same2(coinss):
                    for q2 in range(len(coinss)):
                        coinss.pop()

                    c22 = random.randint(2, 5)

                    for w2 in range(c22):
                        xCoin22 = random.randint(0, 1290)
                        yCoin22 = 589
                        if xCoin22 > x + 61 and xCoin22 < 1290 or xCoin22 < x - 61 and x > 0:
                            coinss.append([xCoin22, yCoin22])
                        else:
                            xCoin22 = xCoin22 + 150
                            if xCoin22 < 1290 and xCoin22 > 0:
                                coinss.append([xCoin22, yCoin22])

                    coinss.sort(key=lambda e2: e2[0])

                    duzinaNiza2 = len(coinss)
                    for broj22 in range(len(coinss) - 1):

                        if not coinss[duzinaNiza2 - 1 - broj22][0] - coinss[duzinaNiza2 - 1 - broj22 - 1][0] > 61:
                            coinss.pop(c22 - 1 - broj22 - 1)

                    random.shuffle(coinss)



        importneprijatelj2()
        for brojNep2 in range (e2):

            enemies2[brojNep2][1]+=brzinaNeprijatelja+5
            if  enemies2[brojNep2][1]>580:
                neprijateljX2 = random.randint(0, 1300)
                neprijateljY2 = random.randint(-1000, -146)
                enemies2[brojNep2][1]=neprijateljY2
                enemies2[brojNep2][0]=neprijateljX2
        for neprijatelj2 in enemies2:

            if x>=neprijatelj2[0]-30 and x<=neprijatelj2[0]+30 and y-neprijatelj2[1]<25 and y-neprijatelj2[1]>0:
                if zivot>=1:
                    zivot-=1
                    brojGlava=brojGlava-1
                    pain.play()
                    screen.blit(eksplozija[0], (x, y))

                if zivot==0:
                    #for eks in range(15):
                    explosionShort.play()
                    vreme=pygame.time.get_ticks()
                    print(vreme)
                    screen.blit(eksplozija[0], (x, y))
                    game_over=True
                    score=0
                    drugiLevel=False

                    for eks in range(75):


                        if eks<5:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[0],(x,y))
                            pygame.display.update()
                        if 5<=eks<10:
                            screen.blit(bg,(0,0))
                            screen.blit(eksplozija[1], (x, y))
                            pygame.display.update()
                        if 10<=eks<15:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[2], (x, y))
                            pygame.display.update()
                        if 15 <= eks < 20:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[3], (x, y))
                            pygame.display.update()
                        if 20 <= eks < 25:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[4], (x, y))
                            pygame.display.update()
                        if 25 <= eks < 30:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[5], (x, y))
                            pygame.display.update()

                        if 30<=eks<35:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[6], (x, y))
                            pygame.display.update()
                        if 35<=eks < 40:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[7], (x, y))
                            pygame.display.update()
                        if 40<=eks < 45:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[8], (x, y))
                            pygame.display.update()
                        if 45<=eks<50:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[9], (x, y))
                            pygame.display.update()
                        if 50<=eks < 55:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[10], (x, y))
                            pygame.display.update()
                        if 55<=eks < 60:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[11], (x, y))
                            pygame.display.update()
                        if 60<=eks < 65:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[12], (x, y))
                            pygame.display.update()
                        if 65<=eks < 70:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[13], (x, y))
                            pygame.display.update()
                        if 70<=eks < 75:
                            screen.blit(bg, (0, 0))
                            screen.blit(eksplozija[14], (x, y))
                            pygame.display.update()
                            game_over = True
        for iG in range(brojGlava):
            screen.blit(glava, (1108 + iG * 70, 90))
        font = pygame.font.SysFont('Video', 30, False, False)

        text2 = font.render(str(score2) + '%', True, (219, 215, 215))
        if score2<100:
            pygame.draw.rect(screen,(105,103,103), (1100, 50, 200, 20))
            pygame.draw.rect(screen, (169, 63, 63), (1100, 50, 0+score2*2, 20))
            screen.blit(text2, (1188, 52))
        if score2>=100:
            score2=100
            pygame.draw.rect(screen, (105, 103, 103), (1100, 50, 200, 20))
            pygame.draw.rect(screen, (169, 63, 63), (1100, 50, 0 + score2 * 2, 20))
            screen.blit(text2, (1188, 52))

    if score2==100:
        score2=101
        print(str(score2)+"aaa")
        screen.blit(bezPostolja, (0,0))
        screen.blit(poslednjiFZastava, (597,283))
        screen.blit(char, (x,y))
        print("uslo zbog skora")
        for pozadinaTri in range(300):
            if pozadinaTri < 5:
                screen.blit(levelTriPozadina, (0, -770))
                print("blblbb")
                pygame.display.update()
            if 5 <= pozadinaTri < 10:
                screen.blit(levelTriPozadina, (0, -761))
                print("blblbb")
                pygame.display.update()
            if 10 <= pozadinaTri < 15:
                screen.blit(levelTriPozadina, (0, -752))
                pygame.display.update()
            if 15 <= pozadinaTri < 20:
                screen.blit(levelTriPozadina, (0, -743))
                pygame.display.update()
            if 20 <= pozadinaTri < 25:
                screen.blit(levelTriPozadina, (0, -734))
                pygame.display.update()
            if 25 <= pozadinaTri < 30:
                screen.blit(levelTriPozadina, (0, -725))
                pygame.display.update()
            if 30 <= pozadinaTri < 35:
                screen.blit(levelTriPozadina, (0, -716))
                pygame.display.update()
            if 35 <= pozadinaTri < 40:
                screen.blit(levelTriPozadina, (0, -707))
                pygame.display.update()
            if 40 <= pozadinaTri < 45:
                screen.blit(levelTriPozadina, (0, -698))
                pygame.display.update()
            if 45 <= pozadinaTri < 50:
                screen.blit(levelTriPozadina, (0, -689))
                pygame.display.update()
            if 50 <= pozadinaTri < 55:
                screen.blit(levelTriPozadina, (0, -680))
                pygame.display.update()
            if 55 <= pozadinaTri < 60:
                screen.blit(levelTriPozadina, (0, -671))
                pygame.display.update()
            if 60 <= pozadinaTri < 65:
                screen.blit(levelTriPozadina, (0, -662))
                pygame.display.update()
            if 65 <= pozadinaTri < 70:
                screen.blit(levelTriPozadina, (0, -653))
                pygame.display.update()
            if 70 <= pozadinaTri < 75:
                screen.blit(levelTriPozadina, (0, -644))
                pygame.display.update()
            if 75 <= pozadinaTri < 80:
                screen.blit(levelTriPozadina, (0, -635))
                pygame.display.update()
            if 80 <= pozadinaTri < 85:
                screen.blit(levelTriPozadina, (0, -626))
                pygame.display.update()
            if 85 <= pozadinaTri < 90:
                screen.blit(levelTriPozadina, (0, -617))
                pygame.display.update()
            if 90 <= pozadinaTri < 95:
                screen.blit(levelTriPozadina, (0, -608))
                pygame.display.update()
            if 95 <= pozadinaTri < 100:
                screen.blit(levelTriPozadina, (0, -599))
                pygame.display.update()
            if 100 <= pozadinaTri < 105:
                screen.blit(levelTriPozadina, (0, -590))
                pygame.display.update()
            if 105 <= pozadinaTri < 110:
                screen.blit(levelTriPozadina, (0, -581))
                pygame.display.update()
            if 110 <= pozadinaTri < 115:
                screen.blit(levelTriPozadina, (0, -572))
                pygame.display.update()
            if 115 <= pozadinaTri< 120:
                screen.blit(levelTriPozadina, (0, -563))
                pygame.display.update()
            if 120 <=pozadinaTri < 125:
                screen.blit(levelTriPozadina, (0, -554))
                pygame.display.update()
            if 125 <= pozadinaTri < 130:
                screen.blit(levelTriPozadina, (0, -545))
                pygame.display.update()
            if 130 <= pozadinaTri< 135:
                screen.blit(levelTriPozadina, (0, -536))
                pygame.display.update()
            if 135 <= pozadinaTri < 140:
                screen.blit(levelTriPozadina, (0, -527))
                pygame.display.update()
            if 140 <= pozadinaTri < 145:
                screen.blit(levelTriPozadina, (0, -518))
                pygame.display.update()
            if 145 <= pozadinaTri < 150:
                screen.blit(levelTriPozadina, (0, -509))
                pygame.display.update()
            if 150 <= pozadinaTri < 155:
                screen.blit(levelTriPozadina, (0, -500))
                pygame.display.update()
            if 155 <= pozadinaTri< 160:
                screen.blit(levelTriPozadina, (0, -491))
                pygame.display.update()
            if 160 <= pozadinaTri < 165:
                screen.blit(levelTriPozadina, (0, -483))
                pygame.display.update()
            if 165 <= pozadinaTri < 170:
                screen.blit(levelTriPozadina, (0, -474))
                pygame.display.update()
            if 170 <= pozadinaTri < 175:
                screen.blit(levelTriPozadina, (0, -465))
                pygame.display.update()
            if 175 <= pozadinaTri < 180:
                screen.blit(levelTriPozadina, (0, -456))
                pygame.display.update()
            if 180 <= pozadinaTri < 185:
                screen.blit(levelTriPozadina, (0, -447))
                pygame.display.update()
            if 185 <= pozadinaTri < 190:
                screen.blit(levelTriPozadina, (0, -438))
                pygame.display.update()
            if 190 <= pozadinaTri < 195:
                screen.blit(levelTriPozadina, (0, -429))
                pygame.display.update()
            if 195 <= pozadinaTri < 200:
                screen.blit(levelTriPozadina, (0, -420))
                pygame.display.update()
            if 200 <= pozadinaTri < 205:
                screen.blit(levelTriPozadina, (0, -411))
                pygame.display.update()
            if 205 <= pozadinaTri < 210:
                screen.blit(levelTriPozadina, (0, -402))
                pygame.display.update()
            if 210 <= pozadinaTri < 215:
                screen.blit(levelTriPozadina, (0, -393))
                pygame.display.update()
            if 215 <= pozadinaTri < 220:
                screen.blit(levelTriPozadina, (0, -384))
                pygame.display.update()
            if 220 <= pozadinaTri < 225:
                screen.blit(levelTriPozadina, (0, -375))
                pygame.display.update()
            if 225 <= pozadinaTri < 230:
                screen.blit(levelTriPozadina, (0, -366))
                pygame.display.update()
            if 230 <= pozadinaTri < 235:
                screen.blit(levelTriPozadina, (0, -357))
                pygame.display.update()
            if 235 <= pozadinaTri < 240:
                screen.blit(levelTriPozadina, (0, -348))
                pygame.display.update()
            if 240 <= pozadinaTri < 245:
                screen.blit(levelTriPozadina, (0, -339))
                pygame.display.update()
            if 245 <= pozadinaTri < 250:
                screen.blit(levelTriPozadina, (0, -330))
                pygame.display.update()
            if 250 <= pozadinaTri < 255:
                screen.blit(levelTriPozadina, (0, -321))
                pygame.display.update()
            if 255 <= pozadinaTri < 260:
                screen.blit(levelTriPozadina, (0, -312))
                pygame.display.update()
            if 260 <= pozadinaTri < 265:
                screen.blit(levelTriPozadina, (0, -303))
                pygame.display.update()
            if 265 <= pozadinaTri < 270:
                screen.blit(levelTriPozadina, (0, -294))
                pygame.display.update()
            if 270 <= pozadinaTri < 275:
                screen.blit(levelTriPozadina, (0, -285))
                pygame.display.update()
            if 275 <= pozadinaTri < 280:
                screen.blit(levelTriPozadina, (0, -276))
                pygame.display.update()
            if 280 <= pozadinaTri < 285:
                screen.blit(levelTriPozadina, (0, -267))
                pygame.display.update()
            if 285 <= pozadinaTri < 290:
                screen.blit(levelTriPozadina, (0, -258))
                pygame.display.update()
            if 290 <= pozadinaTri < 295:
                screen.blit(levelTriPozadina, (0, -249))
                pygame.display.update()
            if 295 <= pozadinaTri < 300:
                screen.blit(levelTriPozadina, (0, -240))
                pygame.display.update()
            if 300 <= pozadinaTri < 305:
                screen.blit(levelTriPozadina, (0, -231))
                pygame.display.update()
        for skTl in range(31):
            jumpSound.play()
            print("skace")
            screen.blit(pomocna, (0, 0))
            screen.blit(char2, (x, int(y - skTl * 10)))
            pygame.display.update()
        for skTl2 in range (3):
            screen.blit(pomocna, (0, 0))
            screen.blit(char2, (x, int(210+skTl2**2*1.5*10)))
            pygame.display.update()
        for sp in range(120):
            if sp < 5:
                screen.blit(levelTriPozadina, (0, -230))
                screen.blit(char, (x, 280))
                pygame.display.update()
            if 5 <= sp < 10:
                screen.blit(levelTriPozadina, (0, -220))
                screen.blit(char, (x, 290))
                pygame.display.update()
            if 10 <= sp < 15:
                screen.blit(levelTriPozadina, (0, -210))
                screen.blit(char, (x, 300))
                pygame.display.update()
            if 15 <= sp < 20:
                screen.blit(levelTriPozadina, (0, -200))
                screen.blit(char, (x, 310))
                pygame.display.update()
            if 20 <= sp < 25:
                screen.blit(levelTriPozadina, (0, -190))
                screen.blit(char, (x, 320))
                pygame.display.update()
            if 25 <= sp < 30:
                screen.blit(levelTriPozadina, (0, -180))
                screen.blit(char, (x, 330))
                print("sp radiii")
                pygame.display.update()
            if 30 <= sp < 35:
                screen.blit(levelTriPozadina, (0, -170))
                screen.blit(char, (x, 340))
                pygame.display.update()
            if 35 <= sp < 40:
                screen.blit(levelTriPozadina, (0, -160))
                screen.blit(char, (x, 350))
                pygame.display.update()
            if 40 <= sp < 45:
                screen.blit(levelTriPozadina, (0, -150))
                screen.blit(char, (x, 360))
                pygame.display.update()
            if 45 <= sp < 50:
                screen.blit(levelTriPozadina, (0, -140))
                screen.blit(char, (x, 370))
                pygame.display.update()
            if 50 <= sp < 55:
                screen.blit(levelTriPozadina, (0, -130))
                screen.blit(char, (x, 380))
                pygame.display.update()
            if 55 <= sp < 60:
                screen.blit(levelTriPozadina, (0, -120))
                screen.blit(char, (x, 390))
                pygame.display.update()
            if 60 <= sp < 65:
                screen.blit(levelTriPozadina, (0, -110))
                screen.blit(char, (x, 400))
                pygame.display.update()
            if 65 <= sp < 70:
                screen.blit(levelTriPozadina, (0, -100))
                screen.blit(char, (x, 410))
                pygame.display.update()
            if 70 <= sp < 75:
                screen.blit(levelTriPozadina, (0, -90))
                screen.blit(char, (x, 420))
                pygame.display.update()
            if 75 <= sp < 80:
                screen.blit(levelTriPozadina, (0, -80))
                screen.blit(char, (x, 430))
                pygame.display.update()
            if 80 <= sp < 85:
                screen.blit(levelTriPozadina, (0, -70))
                screen.blit(char, (x, 440))
                pygame.display.update()
            if 85 <= sp < 90:
                screen.blit(levelTriPozadina, (0, -60))
                screen.blit(char, (x, 450))
                pygame.display.update()
            if 90 <= sp < 95:
                screen.blit(levelTriPozadina, (0, -50))
                screen.blit(char, (x, 460))
                pygame.display.update()
            if 95 <= sp < 100:
                screen.blit(levelTriPozadina, (0, -40))
                screen.blit(char, (x, 470))
                pygame.display.update()
            if 100 <= sp < 105:
                screen.blit(levelTriPozadina, (0, -30))
                screen.blit(char, (x, 480))
                pygame.display.update()
            if 105 <= sp < 110:
                screen.blit(levelTriPozadina, (0, -20))
                screen.blit(char, (x, 490))
                pygame.display.update()
            if 110 <= sp < 115:
                screen.blit(levelTriPozadina, (0, -10))
                screen.blit(char, (x, 500))
                pygame.display.update()
            if 115 <= sp < 120:
                screen.blit(levelTriPozadina, (0, 0))
                screen.blit(char, (x, 510))
                pygame.display.update()
                print("ulazi pa ulazi")
                drugiLevel=False
                treciLevel2=True
        score2=101

    if treciLevel2:
        print("opop")
        screen.blit(levelTriPozadina, (0, 0))
        #screen.blit(char, (x, 510))
        mainClock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 1366 - width - vel:
            x += vel
            left = False
            right = True
        else:
            left = False
            right = False
            walkCount = 0
        if not (isJump):
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                isJump = True
                left = False
                right = False
                walkCount = 0

        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
        redrawGameWin3()
        importCoins3()
        for j3 in coinsss:
            if x >= j3[0] - 61 and x <= j3[0] + 61 and y>450:
                coinSound.play()
                cuvajIndeks3 = coinsss.index(j3)
                if cuvajIndeks3 % 3 == 0:
                    score3 = score3 + 1

                if cuvajIndeks3 % 3 == 1:
                    score3 = score3 + 2
                if cuvajIndeks3 % 3 == 2:
                    score3 = score3 + 4
                coinsss.remove(j3)
                coinsss.insert(cuvajIndeks3, [-200, 0])
                print(score3)
                if all_same3(coinsss):
                    for q3 in range(len(coinsss)):
                        coinsss.pop()

                    c23 = random.randint(2, 5)

                    for w3 in range(c23):
                        xCoin23 = random.randint(0, 1290)
                        yCoin23 = 589
                        if xCoin23 > x + 61 and xCoin23 < 1290 or xCoin23 < x - 61 and x > 0:
                            coinsss.append([xCoin23, yCoin23])
                        else:
                            xCoin23 = xCoin23 + 150
                            if xCoin23 < 1290 and xCoin23 > 0:
                                #pazi
                                coinsss.append([xCoin23, yCoin23])

                    coinsss.sort(key=lambda e3: e3[0])

                    duzinaNiza3 = len(coinsss)
                    for broj23 in range(len(coinsss) - 1):

                        if not coinsss[duzinaNiza3 - 1 - broj23][0] - coinsss[duzinaNiza3 - 1 - broj23 - 1][0] > 61:
                            coinsss.pop(c23 - 1 - broj23 - 1)

                    random.shuffle(coinsss)
        importneprijatelj3()
        for brojNep3 in range(e3):

            enemies3[brojNep3][1] += brzinaNeprijatelja + 7
            if enemies3[brojNep3][1] > 580:
                neprijateljX3 = random.randint(0, 1300)
                neprijateljY3 = random.randint(-1000, -146)
                enemies3[brojNep3][1] = neprijateljY3
                enemies3[brojNep3][0] = neprijateljX3
        for neprijatelj3 in enemies3:

            if x >= neprijatelj3[0] - 30 and x <= neprijatelj3[0] + 30 and y - neprijatelj3[1] < 27 and y - neprijatelj3[1] > 0:
                if zivot >= 1:
                    zivot -= 1
                    brojGlava = brojGlava - 1
                    pain.play()
                    screen.blit(eksplozija[0], (x, y))

                if zivot == 0:
                    # for eks in range(15):
                    explosionShort.play()
                    vreme = pygame.time.get_ticks()
                    print(vreme)
                    screen.blit(eksplozija[0], (x, y))
                    game_over = True
                    score = 0
                    score2=0
                    treciLevel2 = False
        for iG2 in range(brojGlava):
            screen.blit(glava, (1108 + iG2 * 70, 90))
        font = pygame.font.SysFont('Video', 30, False, False)

        text3 = font.render(str(score3) + '%', True, (219, 215, 215))
        if score3 < 100:
            pygame.draw.rect(screen, (105, 103, 103), (1100, 50, 200, 20))
            pygame.draw.rect(screen, (169, 63, 63), (1100, 50, 0 + score3 * 2, 20))
            screen.blit(text3, (1188, 52))
        if score3 >= 100:
            score3 = 100
            pygame.draw.rect(screen, (105, 103, 103), (1100, 50, 200, 20))
            pygame.draw.rect(screen, (169, 63, 63), (1100, 50, 0 + score3 * 2, 20))
            screen.blit(text3, (1188, 52))
            #cetvrtiL=True
            treciLevel2=False
        #score3=21
    if score3==100:
        score3=101
        screen.blit(levelTriPozadina, (0,0))
        screen.blit(char, (x, y))
        for bs4 in range(300):
            if bs4 < 5:
                screen.blit(levelCetiriPozadina, (0, -770))
                print("blblbb")
                pygame.display.update()
            if 5 <= bs4 < 10:
                screen.blit(levelCetiriPozadina, (0, -761))
                print("blblbb")
                pygame.display.update()
            if 10 <= bs4 < 15:
                screen.blit(levelCetiriPozadina, (0, -752))
                pygame.display.update()
            if 15 <= bs4 < 20:
                screen.blit(levelCetiriPozadina, (0, -743))
                pygame.display.update()
            if 20 <= bs4 < 25:
                screen.blit(levelCetiriPozadina, (0, -734))
                pygame.display.update()
            if 25 <= bs4 < 30:
                screen.blit(levelCetiriPozadina, (0, -725))
                pygame.display.update()
            if 30 <= bs4 < 35:
                screen.blit(levelCetiriPozadina, (0, -716))
                pygame.display.update()
            if 35 <= bs4 < 40:
                screen.blit(levelCetiriPozadina, (0, -707))
                pygame.display.update()
            if 40 <= bs4 < 45:
                screen.blit(levelCetiriPozadina, (0, -698))
                pygame.display.update()
            if 45 <= bs4 < 50:
                screen.blit(levelCetiriPozadina, (0, -689))
                pygame.display.update()
            if 50 <= bs4 < 55:
                screen.blit(levelCetiriPozadina, (0, -680))
                pygame.display.update()
            if 55 <= bs4 < 60:
                screen.blit(levelCetiriPozadina, (0, -671))
                pygame.display.update()
            if 60 <= bs4 < 65:
                screen.blit(levelCetiriPozadina, (0, -662))
                pygame.display.update()
            if 65 <= bs4 < 70:
                screen.blit(levelCetiriPozadina, (0, -653))
                pygame.display.update()
            if 70 <= bs4 < 75:
                screen.blit(levelCetiriPozadina, (0, -644))
                pygame.display.update()
            if 75 <= bs4 < 80:
                screen.blit(levelCetiriPozadina, (0, -635))
                pygame.display.update()
            if 80 <= bs4 < 85:
                screen.blit(levelCetiriPozadina, (0, -626))
                pygame.display.update()
            if 85 <= bs4 < 90:
                screen.blit(levelCetiriPozadina, (0, -617))
                pygame.display.update()
            if 90 <= bs4 < 95:
                screen.blit(levelCetiriPozadina, (0, -608))
                pygame.display.update()
            if 95 <= bs4 < 100:
                screen.blit(levelCetiriPozadina, (0, -599))
                pygame.display.update()
            if 100 <= bs4 < 105:
                screen.blit(levelCetiriPozadina, (0, -590))
                pygame.display.update()
            if 105 <= bs4 < 110:
                screen.blit(levelCetiriPozadina, (0, -581))
                pygame.display.update()
            if 110 <= bs4 < 115:
                screen.blit(levelCetiriPozadina, (0, -572))
                pygame.display.update()
            if 115 <= bs4 < 120:
                screen.blit(levelCetiriPozadina, (0, -563))
                pygame.display.update()
            if 120 <= bs4 < 125:
                screen.blit(levelCetiriPozadina, (0, -554))
                pygame.display.update()
            if 125 <= bs4 < 130:
                screen.blit(levelCetiriPozadina, (0, -545))
                pygame.display.update()
            if 130 <= bs4 < 135:
                screen.blit(levelCetiriPozadina, (0, -536))
                pygame.display.update()
            if 135 <= bs4 < 140:
                screen.blit(levelCetiriPozadina, (0, -527))
                pygame.display.update()
            if 140 <= bs4 < 145:
                screen.blit(levelCetiriPozadina, (0, -518))
                pygame.display.update()
            if 145 <= bs4 < 150:
                screen.blit(levelCetiriPozadina, (0, -509))
                pygame.display.update()
            if 150 <= bs4 < 155:
                screen.blit(levelCetiriPozadina, (0, -500))
                pygame.display.update()
            if 155 <= bs4 < 160:
                screen.blit(levelCetiriPozadina, (0, -491))
                pygame.display.update()
            if 160 <= bs4 < 165:
                screen.blit(levelCetiriPozadina, (0, -483))
                pygame.display.update()
            if 165 <= bs4 < 170:
                screen.blit(levelCetiriPozadina, (0, -474))
                pygame.display.update()
            if 170 <= bs4 < 175:
                screen.blit(levelCetiriPozadina, (0, -465))
                pygame.display.update()
            if 175 <= bs4 < 180:
                screen.blit(levelCetiriPozadina, (0, -456))
                pygame.display.update()
            if 180 <= bs4 < 185:
                screen.blit(levelCetiriPozadina, (0, -447))
                pygame.display.update()
            if 185 <= bs4 < 190:
                screen.blit(levelCetiriPozadina, (0, -438))
                pygame.display.update()
            if 190 <= bs4 < 195:
                screen.blit(levelCetiriPozadina, (0, -429))
                pygame.display.update()
            if 195 <= bs4 < 200:
                screen.blit(levelCetiriPozadina, (0, -420))
                pygame.display.update()
            if 200 <= bs4 < 205:
                screen.blit(levelCetiriPozadina, (0, -411))
                pygame.display.update()
            if 205 <= bs4 < 210:
                screen.blit(levelCetiriPozadina, (0, -402))
                pygame.display.update()
            if 210 <= bs4 < 215:
                screen.blit(levelCetiriPozadina, (0, -393))
                pygame.display.update()
            if 215 <= bs4 < 220:
                screen.blit(levelCetiriPozadina, (0, -384))
                pygame.display.update()
            if 220 <= bs4 < 225:
                screen.blit(levelCetiriPozadina, (0, -375))
                pygame.display.update()
            if 225 <= bs4 < 230:
                screen.blit(levelCetiriPozadina, (0, -366))
                pygame.display.update()
            if 230 <= bs4 < 235:
                screen.blit(levelCetiriPozadina, (0, -357))
                pygame.display.update()
            if 235 <= bs4 < 240:
                screen.blit(levelCetiriPozadina, (0, -348))
                pygame.display.update()
            if 240 <= bs4 < 245:
                screen.blit(levelCetiriPozadina, (0, -339))
                pygame.display.update()
            if 245 <= bs4 < 250:
                screen.blit(levelCetiriPozadina, (0, -330))
                pygame.display.update()
            if 250 <= bs4 < 255:
                screen.blit(levelCetiriPozadina, (0, -321))
                pygame.display.update()
            if 255 <= bs4 < 260:
                screen.blit(levelCetiriPozadina, (0, -312))
                pygame.display.update()
            if 260 <= bs4 < 265:
                screen.blit(levelCetiriPozadina, (0, -303))
                pygame.display.update()
            if 265 <= bs4 < 270:
                screen.blit(levelCetiriPozadina, (0, -294))
                pygame.display.update()
            if 270 <= bs4 < 275:
                screen.blit(levelCetiriPozadina, (0, -285))
                pygame.display.update()
            if 275 <= bs4 < 280:
                screen.blit(levelCetiriPozadina, (0, -276))
                pygame.display.update()
            if 280 <= bs4 < 285:
                screen.blit(levelCetiriPozadina, (0, -267))
                pygame.display.update()
            if 285 <= bs4 < 290:
                screen.blit(levelCetiriPozadina, (0, -258))
                pygame.display.update()
            if 290 <= bs4 < 295:
                screen.blit(levelCetiriPozadina, (0, -249))
                pygame.display.update()
            if 295 <= bs4 < 300:
                screen.blit(levelCetiriPozadina, (0, -240))
                print("2bl")
                pygame.display.update()
                cetvrtiL = True

        score3=101
    if cetvrtiL:
        print("cetvrti")

        #treciLevel2 = False
        screen.blit(pomocna2, (0, 0))
        screen.blit(poza, (x, y))
        for skk in range(31):
            jumpSound.play()
            screen.blit(pomocna2, (0, 0))
            screen.blit(char2, (x, int(y - skk * 10)))
            pygame.display.update()
        for skk2 in range(3):
            screen.blit(pomocna2, (0, 0))
            screen.blit(char2, (x, int(210 + skk2 ** 2 * 1.5 * 10)))
            pygame.display.update()
        screen.blit(levelCetiriPozadina, (0, -240))
        screen.blit(char, (x, 270))
        for spp in range(120):
            if spp < 5:
                screen.blit(levelCetiriPozadina, (0, -230))
                screen.blit(char, (x, 280))
                pygame.display.update()
                print("ualzi u cetvrti")
            if 5 <= spp < 10:
                screen.blit(levelCetiriPozadina, (0, -220))
                screen.blit(char, (x, 290))
                pygame.display.update()
            if 10 <= spp < 15:
                screen.blit(levelCetiriPozadina, (0, -210))
                screen.blit(char, (x, 300))
                pygame.display.update()
            if 15 <= spp < 20:
                screen.blit(levelCetiriPozadina, (0, -200))
                screen.blit(char, (x, 310))
                pygame.display.update()
            if 20 <= spp < 25:
                screen.blit(levelCetiriPozadina, (0, -190))
                screen.blit(char, (x, 320))
                pygame.display.update()
            if 25 <= spp < 30:
                screen.blit(levelCetiriPozadina, (0, -180))
                screen.blit(char, (x, 330))
                pygame.display.update()
            if 30 <= spp < 35:
                screen.blit(levelCetiriPozadina, (0, -170))
                screen.blit(char, (x, 340))
                pygame.display.update()
            if 35 <= spp < 40:
                screen.blit(levelCetiriPozadina, (0, -160))
                screen.blit(char, (x, 350))
                pygame.display.update()
            if 40 <= spp < 45:
                screen.blit(levelCetiriPozadina, (0, -150))
                screen.blit(char, (x, 360))
                pygame.display.update()
            if 45 <= spp < 50:
                screen.blit(levelCetiriPozadina, (0, -140))
                screen.blit(char, (x, 370))
                pygame.display.update()
            if 50 <= spp < 55:
                screen.blit(levelCetiriPozadina, (0, -130))
                screen.blit(char, (x, 380))
                pygame.display.update()
            if 55 <= spp < 60:
                screen.blit(levelCetiriPozadina, (0, -120))
                screen.blit(char, (x, 390))
                pygame.display.update()
            if 60 <= spp < 65:
                screen.blit(levelCetiriPozadina, (0, -110))
                screen.blit(char, (x, 400))
                pygame.display.update()
            if 65 <= spp < 70:
                screen.blit(levelCetiriPozadina, (0, -100))
                screen.blit(char, (x, 410))
                pygame.display.update()
            if 70 <= spp < 75:
                screen.blit(levelCetiriPozadina, (0, -90))
                screen.blit(char, (x, 420))
                pygame.display.update()
            if 75 <= spp < 80:
                screen.blit(levelCetiriPozadina, (0, -80))
                screen.blit(char, (x, 430))
                pygame.display.update()
            if 80 <= spp < 85:
                screen.blit(levelCetiriPozadina, (0, -70))
                screen.blit(char, (x, 440))
                pygame.display.update()
            if 85 <= spp < 90:
                screen.blit(levelCetiriPozadina, (0, -60))
                screen.blit(char, (x, 450))
                pygame.display.update()
            if 90 <= spp < 95:
                screen.blit(levelCetiriPozadina, (0, -50))
                screen.blit(char, (x, 460))
                pygame.display.update()
            if 95 <= spp < 100:
                screen.blit(levelCetiriPozadina, (0, -40))
                screen.blit(char, (x, 470))
                pygame.display.update()
            if 100 <= spp < 105:
                screen.blit(levelCetiriPozadina, (0, -30))
                screen.blit(char, (x, 480))
                pygame.display.update()
            if 105 <= spp < 110:
                screen.blit(levelCetiriPozadina, (0, -20))
                screen.blit(char, (x, 490))
                pygame.display.update()
            if 110 <= spp < 115:
                screen.blit(levelCetiriPozadina, (0, -10))
                screen.blit(char, (x, 500))
                pygame.display.update()
            if 115 <= spp < 120:
                screen.blit(levelCetiriPozadina, (0, 0))
                screen.blit(char, (x, 510))
                pygame.display.update()

                cetvrtiLevel= True
                cetvrtiL = False

    if cetvrtiLevel:
        screen.blit(levelCetiriPozadina, (0, 0))
        # screen.blit(char, (x, 510))
        mainClock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 1366 - width - vel:
            x += vel
            left = False
            right = True
        else:
            left = False
            right = False
            walkCount = 0
        if not (isJump):
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                isJump = True
                left = False
                right = False
                walkCount = 0

        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
        redrawGameWin4()
        importCoins4()
        for j4 in coinssss:
            if x >= j4[0] - 61 and x <= j4[0] + 61 and y>450:
                coinSound.play()
                cuvajIndeks4 = coinssss.index(j4)
                if cuvajIndeks4 % 3 == 0:
                    score4 = score4 + 1

                if cuvajIndeks4 % 3 == 1:
                    score4 = score4 + 2
                if cuvajIndeks4 % 3 == 2:
                    score4 = score4 + 4
                coinssss.remove(j4)
                coinssss.insert(cuvajIndeks4, [-200, 0])
                print(score4)
                if all_same4(coinssss):
                    for q4 in range(len(coinssss)):
                        coinssss.pop()

                    c24 = random.randint(2, 5)

                    for w4 in range(c24):
                        xCoin24 = random.randint(0, 1290)
                        yCoin24 = 589
                        if xCoin24 > x + 61 and xCoin24 < 1290 or xCoin24 < x - 61 and x > 0:
                            coinssss.append([xCoin24, yCoin24])
                        else:
                            xCoin24 = xCoin24 + 150
                            if xCoin24 < 1290 and xCoin24 > 0:
                                coinssss.append([xCoin24, yCoin24])

                    coinssss.sort(key=lambda e4: e4[0])

                    duzinaNiza4 = len(coinssss)
                    for broj24 in range(len(coinssss) - 1):

                        if not coinssss[duzinaNiza4 - 1 - broj24][0] - coinssss[duzinaNiza4 - 1 - broj24 - 1][0] > 61:
                            coinssss.pop(c24 - 1 - broj24 - 1)

                    random.shuffle(coinssss)

        importneprijatelj4()
        for brojNep4 in range(e4):

            enemies4[brojNep4][1] += brzinaNeprijatelja + 9
            if enemies4[brojNep4][1] > 580:
                neprijateljX4 = random.randint(0, 1300)
                neprijateljY4 = random.randint(-1000, -146)
                enemies4[brojNep4][1] = neprijateljY4
                enemies4[brojNep4][0] = neprijateljX4
        for neprijatelj4 in enemies4:

            if x >= neprijatelj4[0] - 30 and x <= neprijatelj4[0] + 30 and y - neprijatelj4[1] < 29 and y - neprijatelj4[1] > 0:
                if zivot >= 1:
                    zivot -= 1
                    brojGlava = brojGlava - 1
                    pain.play()
                    screen.blit(eksplozija[0], (x, y))

                if zivot == 0:
                    # for eks in range(15):
                    explosionShort.play()
                    vreme = pygame.time.get_ticks()
                    print(vreme)
                    screen.blit(eksplozija[0], (x, y))
                    game_over = True
                    score = 0
                    score2=0
                    score3=0
                    cetvrtiLevel = False
        for iG3 in range(brojGlava):
            screen.blit(glava, (1108 + iG3 * 70, 90))
        font = pygame.font.SysFont('Video', 30, False, False)

        text4 = font.render(str(score4) + '%', True, (219, 215, 215))
        if score4 < 100:
            pygame.draw.rect(screen, (105, 103, 103), (1100, 50, 200, 20))
            pygame.draw.rect(screen, (169, 63, 63), (1100, 50, 0 + score4 * 2, 20))
            screen.blit(text4, (1188, 52))
        if score4 >= 100:
            score4 = 100
            pygame.draw.rect(screen, (105, 103, 103), (1100, 50, 200, 20))
            pygame.draw.rect(screen, (169, 63, 63), (1100, 50, 0 + score4 * 2, 20))
            screen.blit(text4, (1188, 52))
            #gameOver=True
            cetvrtiLevel = False
            kraj = True
            # treciLevel2=False
        #score4 = 21

    if kraj:
        teleportation.play()
        print('5')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        for kraj in range(2000):

            print("kfraaaj")
            screen.blit(zavrsna, (0,0))
            pygame.display.update()
            kraj=False
        show_go_screen()
        score=0
        score2=0
        score3=0
        score4=0
        zivot = 3
        brojGlava=3
        #gameOver =True
        #kraj=False



    pygame.display.update()

pygame.quit()
