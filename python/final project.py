import pygame as pg
import math
import random 
import time
pg.init()

# 색 설정
white=(255,255,255)
black=(0,0,0)
green= (60, 179, 113)
brown = (150,75,0)
bright_green = (0,255,0)
yellow = 255,255,0
red = 250,0,0
# 초기 실행창 설정
disw, dish = 800, 600
screen = pg.display.set_mode((disw, dish))
pg.display.set_caption('jeck and the beanstalk')
# 배경 음악
music = pg.mixer.music.load('backmusic.mp3')
pg.mixer.music.play(-1)
# 배경 이미지 불러오기
startback = pg.image.load('startback.png').convert()
stage1_image = pg.image.load('stage1rule.png').convert()
ingame = pg.image.load('game.jpg').convert()
start_image = pg.image.load('start_image.jpg').convert()
# 초당 프레임 설정
clock = pg.time.Clock()
# 텍스트 함수
def message_to_screen(a, msg, color):
  screen_text = a.render(msg, True, color) # 텍스트 객체 생성
  textrect = screen_text.get_rect(); #텍스트 객체의 출력 위치 가져오기
  return screen_text, textrect
# play 버튼 함수 
def button ():
  mouse = pg.mouse.get_pos() 
  click = pg.mouse.get_pressed()
  
  if 430>mouse[0]>330 and 450>mouse[1]>400:
    pg.draw.rect(screen, bright_green,(330,400,100,60))
    if click[0]==1:
        return True
  else :
    pg.draw.rect(screen, green,(330,400,100,60))  
  # play 버튼에 마우수를 갖다 대면 밝은 초록색이 된다.
  # 버튼위치에 play! 글씨 표시 
  playtext = pg.font.Font(None,40)
  s,r = message_to_screen(playtext, 'play!',white)
  r.center = (380,430)
  screen.blit(s,r) 

# 카운트 다운 화면에 출력 함수
def countdown (time):

  counter, text = int(time), str(time)
  pg.time.set_timer(pg.USEREVENT, 1000) 
  font = pg.font.SysFont('Consolas', 80) 
  font2 = pg.font.SysFont(None,40)
  while True: 
    for e in pg.event.get(): 
      if e.type == pg.USEREVENT: 
        counter -= 1 
        if counter > 0 : 
          text = str(counter)  
        else :
          text = 'start!'
      if e.type == pg.QUIT: break 
    else: 
      screen.fill(yellow)
      screen.blit(font.render(text, True, black), (378,250)) 
      if text == 'start!':
          screen.blit(start_image,(0,0))
          screen.blit(font.render(text, True, black), (378,250))           
          screen.blit(font2.render('please close this screen', True, red), (215,350))
      pg.display.update() 
      clock.tick(30) 
      continue 
    break
# stage1에서의 규칙 설명 함수
def stage1rule ():  

  while True :
      for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_SPACE:
            countdown(3)
            break 
      else : 
        screen.blit(stage1_image,(0,0))
        pg.display.update()
        continue
      break 

# 시작 화면 
end = False
while not end :
# 이벤트 타입이 quit일때 끝내기 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True
            pg.quit()

    screen.blit(startback,(0,0))
    a=button()
    if a == True :
        end = True 
# 화면 업데이트
    pg.display.update()   
    pg.display.flip()

# 잭 캐릭터 이미지 
jeck_image = [pg.image.load('jeckr3.png'),pg.image.load('jeckr2.png'),pg.image.load('jeckr1.png'),pg.image.load('jeckl1.png'),pg.image.load('jeckl2.png'),pg.image.load('jeckl3.png')]
# 새와 장애물 이미지 
bird_image = pg.image.load('bird.png').convert_alpha()
ob_image = pg.image.load('obstacle.png').convert_alpha()
# 잭 캐릭터 움직임 
move = False
walkCount = 0
def movement (gox, goy):
  global walkCount,x_change, y_change, jeck_image, move
  if walkCount + 1 > 6:
    walkCount = 0
  if move == True :
    screen.blit(jeck_image[walkCount],(gox,goy))
    walkCount += 1
  if move == False:
    screen.blit(jeck_image[walkCount],(gox,goy))

  pg.display.update()


# 게임 미션 실패와 성공 화면에서 쓸 폰트 객체 
gameover1 = pg.font.SysFont(None, 100)
gameover2 = pg.font.SysFont(None, 50)

# timer font 객체 
timefont = pg.font.SysFont(None, 30)


# 시간 표시 함수와 이동하는 배경화면  
def displaytimer() :
  global timer,displaytime,clock1
  seconds = clock1.tick(60)/1000.0
  timer -= seconds
  displaytime = math.trunc(timer)

# 오브젝트 화면에 그리기 함수 
def drawObject(obj, x,y):
    global screen
    screen.blit(obj,(x,y))

# stage 1

def gameLoop() :
  global lead_x, lead_y, x_change, y_change, move, timer,displaytime,clock1
  global bird_image, ob_image
  # stage 1 규칙 설명 space 누르면 3초 후 게임 시작
  stage1rule()
  # 배경음악2
  music = pg.mixer.music.load('music.mp3')
  pg.mixer.music.play(-1) 
  # 초기 잭의 위치 
  lead_x=300
  lead_y=300
  # timer 초기 설정
  timer = 20
  # 잭의 위치 변화 변수 선언
  x_change = 0 
  y_change = 0
  # 장애물 위치 변수 선언
  ob_x,ob_y = random.randrange(0,800), -100 #거인이 던지는 장애물
  bird_x,bird_y = 900, random.randrange(0,600) # 하늘의 새 

  stage1_start = True
  gameover = False    
  clock1 = pg.time.Clock()
  while stage1_start :
    screen.blit(ingame,(0,0))
    # timer 
    displaytimer()
    screen.blit(timefont.render('Time : '+str(displaytime),True, black),(0,0))
    # 제한 시간이 지났을 때 
    if displaytime < 0:
      c=True
      while c :
        screen.blit(ingame,(0,-300))
        #박수 소리 
        music = pg.mixer.music.load('Applause.wav')
        pg.mixer.music.play()     
        screen.blit(gameover1.render('Success!', True, white), (250,250)) 
        screen.blit(gameover2.render('The screen turns off after 5 seconds.', True, white), (105,350)) 
        pg.display.update()
        time.sleep(5)
        c= False
      stage1_start =False   

    # 미션 실패일 때 이용자의 선택에 따라 게임을 끝내거나 재시작할 수 있음
    while gameover == True :
      screen.fill(green)
      screen.blit(gameover1.render('Game over !', True, white), (200,250)) 
      screen.blit(gameover2.render('press \'R\' to play again or \'Q\' to quit', True, white), (120,400)) 

      pg.display.update()

      for ev in pg.event.get() :
        if ev.type == pg.KEYDOWN:
          if ev.key == pg.K_q:
            gameover = False
            stage1_start = False
          if ev. key == pg.K_r:
            gameLoop()

    # 키 이벤트 
    for e in pg.event.get():
      if e.type == pg.QUIT:
          stage1_start = False
      if e.type == pg.KEYDOWN:
          if e.key == pg.K_LEFT:
              x_change = -10
  
          if e.key == pg.K_RIGHT:
              x_change = 10

          if e.key == pg.K_UP:
              y_change = -10

          if e.key == pg.K_DOWN:
              y_change = 10
             
          move = True
      if e.type == pg.KEYUP:
          x_change = 0
          y_change = 0
          move = False 
    # 창 범위에서 벗어 났을 때 
    if lead_x >= 800 or lead_x <= -190 :
      gameover = True

    lead_x += x_change
    lead_y += y_change
    

    drawObject(bird_image,bird_x,bird_y)
    drawObject(ob_image, ob_x, ob_y)
    bird_x -= 5
    ob_y += 5
    movement(lead_x, lead_y)
    # 장애물이 화면 밖으로 나갔을 때 랜덤으로 재생성
    if bird_x <=0:
      bird_x = 900
      bird_y = random.randrange(0,600)
    if ob_y >= 600:
      ob_x,ob_y = random.randrange(0,800), -100
    # 장애물과 부딪치면 게임 오버
    if lead_x + 150 > bird_x:
      if(lead_y < bird_y and lead_y +150 > bird_y )or(lead_y < bird_y+50 and lead_y + 150 > bird_y+50):
        gameover = True
    if lead_y < ob_y + 170:
      if(lead_x < ob_x  and lead_x +150 > ob_x) or (lead_x+150 > ob_x +150 and lead_x < ob_x+150):
        gameover = True
    
    pg.display.flip()
    clock.tick(30)



  pg.quit()
  quit()

gameLoop()