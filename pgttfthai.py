# -*- coding: utf-8 -*-
#
# file:     pgttfthai.py
#
# author:   psarod@gmail.com
# date:     13-apr-2017
#
# fonts src:
# https://github.com/byrongibson/fonts/tree/master/truetype/tlwg

import pygame,sys,glob,random

#00--init pgcolor, xcolor
pgRed = pygame.Color(255, 0, 0)
pgGreen = pygame.Color(0, 255, 0)
pgBlue = pygame.Color(0, 0, 255)
pgWhite = pygame.Color(255, 255, 255)  
pgGray = pygame.Color(222, 222, 222)  

xBlack = (0,0,0)   
xGray = (200,200,200)
xWhite = (255,255,255)
xGreen = (0,255,0)
xRed = (255,0,0)
xBlue = (0,0,255)

#------------------------------------------------------------------
#1a--init caption pwindow psurf
pygame.init()
pygame.display.set_caption('Test Thai Fonts on Pygame Display') # Set the window bar title

SCREEN_HEIGHT = 680                     #900,800,700,600
SCREEN_WIDTH = SCREEN_HEIGHT * 16 / 9   #1600,...

pwindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pwindow0 = pygame.display.get_surface() # This is where images are displayed
pwindow0.fill(xGray)    

#1b--init pclock
FPS = 5
pclock = pygame.time.Clock()
pclock.tick(FPS)

 
    
#---------------------------------------------------------
#10a--get thai fonts list
mypath = "./fonts/*ttf"
ttfthais = glob.glob(mypath)
ttfthais.sort()

#10b--init while running
xx = 0
xlast = len(ttfthais)-1
fsizestart = 20 
fsize = fsizestart
x0 = 0
y0 = 540
running = True


while running: # for each frame
  #-------------------------------------------------------------------
  #10---clean screen
  pwindow0.fill(xGray)
  pygame.draw.rect(pwindow, pgWhite, (x0+10, 10, SCREEN_WIDTH-20, y0))
  pygame.draw.rect(pwindow, pgGray, (x0+10, y0+20, SCREEN_WIDTH-20, SCREEN_HEIGHT-y0-30))


  #11--.blit -> .display Fonts...
  xcolor = xBlack
  xtxt = "ทดสอบภาษาไทย วิญญูชน ป้าสุข ผู้ใหญ่บ้าน ดีที่สุด"
  y00 =10
  xilast = 0
  for i in range(0,10):
    xi = xx+i; 
    if not (xi > xlast):
      xilast = xi
      uthx = unicode( "#%02d %s: %s" % (xi+1,ttfthais[xi],xtxt), "utf-8")
      fthx = pygame.font.Font(ttfthais[xi],fsize)
      pwindow.blit(fthx.render(uthx,True,xcolor),(10,y00+i*50))

  msg = "[#%02d..#%02d] of Total %d Fonts     [Font Size = %d]" % (xx+1,xilast+1,xlast+1,fsize)
  pwindow.blit(fthx.render(msg,True,xBlue),(10 ,y0-30))

  #18--help message
  xcolor = (155,0,0) 
  f00 = pygame.font.Font(None,24)  
  msg = "[Left Click] ... next fonts           [Right Click] ... prev fonts"
  pwindow.blit(f00.render(msg,True,xcolor),(SCREEN_WIDTH/4 ,SCREEN_HEIGHT-90))
  msg = "[Scroll Up] ... increase size         [Scroll Dn] ... decrese size"
  pwindow.blit(f00.render(msg,True,xcolor),(SCREEN_WIDTH/4 ,SCREEN_HEIGHT-60))
  msg = "[Middle Click] ... reset fonts and size"
  pwindow.blit(f00.render(msg,True,xcolor),(SCREEN_WIDTH/4 ,SCREEN_HEIGHT-30))

  #19--.flip
  pygame.display.flip()


  #-------------------------------------------------------------------
  #99--events 
  for event in pygame.event.get():
    #99a
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit(0)
    #99b
    if event.type == pygame.MOUSEBUTTONDOWN :
      #[1=Lclick 3=Rclick  2=Mclick  4=ScrUp 5=ScrDN]
      if (event.button == 1): #fonts up
        xx +=10
        #if (xx > (xlast-9)): xx = (xlast-9)
        if (xx > (xlast)): xx -=10

      if (event.button == 3): #fonts dn
        xx -=10
        if (xx < 0): xx = 0

      if (event.button == 2): #reset
        xx = 0
        fsize = fsizestart

      if (event.button == 4): #size up
        fsize +=1

      if (event.button == 5): #size dn
        fsize -=1
    #99c
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        running = False
        sys.exit(0)
