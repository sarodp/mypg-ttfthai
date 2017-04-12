# -*- coding: utf-8 -*-
#
# file: 	pgttfthait.py
# author: 	psarod@gmail.com
# date: 	12-apr-2017
#
# fonts src:
# https://github.com/byrongibson/fonts/tree/master/truetype/tlwg

import pygame, sys, glob, random



#--init PG screenvar
SCREEN_HEIGHT = 600 					#900,800,700,600
SCREEN_WIDTH = SCREEN_HEIGHT * 16 / 9 	#1600

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.get_surface() # This is where images are displayed
    
pygame.display.set_caption('Test Thai Fonts on Pygame Display') # Set the window bar title


#--init pgcolor, xcolor
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
    
#11-init clock
FPS = 5
clock = pygame.time.Clock()
clock.tick(FPS)

#12---init screen
screen.fill(xGray)    
#screen.fill(xWhite)    
      


#--thai fonts list
mypath = "./fonts/*ttf"
ttfthais = glob.glob(mypath)


xx = 0
fsize = 18
running = True
x0 = 0
y0 = 480
while running: # for each frame
	#10---clear screen
	screen.fill(xGray)    
	pygame.draw.rect(window, pgWhite, (x0+10, 10, SCREEN_WIDTH-20, y0))
	pygame.draw.rect(window, pgGray, (x0+10, y0+20, SCREEN_WIDTH-20, SCREEN_HEIGHT-y0-30))


	#11--.blit -> .display
	xcolor = xBlack

	fth0 = pygame.font.Font(ttfthais[xx+0],fsize)
	fth1 = pygame.font.Font(ttfthais[xx+1],fsize)
	fth2 = pygame.font.Font(ttfthais[xx+2],fsize)
	fth3 = pygame.font.Font(ttfthais[xx+3],fsize)
	fth4 = pygame.font.Font(ttfthais[xx+4],fsize)
	fth5 = pygame.font.Font(ttfthais[xx+5],fsize)
	fth6 = pygame.font.Font(ttfthais[xx+6],fsize)
	fth7 = pygame.font.Font(ttfthais[xx+7],fsize)
	fth8 = pygame.font.Font(ttfthais[xx+8],fsize)
	fth9 = pygame.font.Font(ttfthais[xx+9],fsize)

	f00 = pygame.font.Font(None,24)  

	xtxt = "ทดสอบภาษาไทย วิญญูชน ป้าสุข ผู้ใหญ่บ้าน ดีที่สุด"

	uth = unicode( "%s: %s" % (ttfthais[xx+0],xtxt), "utf-8")
	window.blit(fth0.render(uth,True,xcolor),(10,10))
	uth = unicode( "%s: %s" % (ttfthais[xx+1],xtxt), "utf-8")
	window.blit(fth1.render(uth,True,xcolor),(10,50))
	uth = unicode( "%s: %s" % (ttfthais[xx+2],xtxt), "utf-8")
	window.blit(fth2.render(uth,True,xcolor),(10,90))
	uth = unicode( "%s: %s" % (ttfthais[xx+3],xtxt), "utf-8")
	window.blit(fth3.render(uth,True,xcolor),(10,130))
	uth = unicode( "%s: %s" % (ttfthais[xx+4],xtxt), "utf-8")
	window.blit(fth4.render(uth,True,xcolor),(10,170))
	uth = unicode( "%s: %s" % (ttfthais[xx+5],xtxt), "utf-8")
	window.blit(fth5.render(uth,True,xcolor),(10,210))
	uth = unicode( "%s: %s" % (ttfthais[xx+6],xtxt), "utf-8")
	window.blit(fth6.render(uth,True,xcolor),(10,250))
	uth = unicode( "%s: %s" % (ttfthais[xx+7],xtxt), "utf-8")
	window.blit(fth7.render(uth,True,xcolor),(10,290))
	uth = unicode( "%s: %s" % (ttfthais[xx+8],xtxt), "utf-8")
	window.blit(fth8.render(uth,True,xcolor),(10,330))
	uth = unicode( "%s: %s" % (ttfthais[xx+9],xtxt), "utf-8")
	window.blit(fth9.render(uth,True,xcolor),(10,370))


	#14--help message
	xcolor = (155,0,0) 
	msg = "Font Size = %d" % fsize
	window.blit(fth9.render(msg,True,xBlue),(10 ,y0-30))

	msg = "[Left Click] ... next fonts           [Right Click] ... prev fonts"
	window.blit(f00.render(msg,True,xcolor),(SCREEN_WIDTH/4 ,SCREEN_HEIGHT-90))
	msg = "[Scroll Up] ... increase size         [Scroll Dn] ... decrese size"
	window.blit(f00.render(msg,True,xcolor),(SCREEN_WIDTH/4 ,SCREEN_HEIGHT-60))
	msg = "[Middle Click] ... reset fonts and size"
	window.blit(f00.render(msg,True,xcolor),(SCREEN_WIDTH/4 ,SCREEN_HEIGHT-30))

	pygame.display.flip()


	#99--exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

		if event.type == pygame.MOUSEBUTTONDOWN :
			#[1=Lclick 3=Rclick  2=Mclick  4=ScrUp 5=ScrDN]
			if (event.button == 1): #fonts up
				xx +=10
			if (event.button == 3): #fonts dn
				xx -=10
			if (event.button == 2): #reset
				xx = 0
				fsize = 18
			if (event.button == 4): #size up
				fsize +=1
			if (event.button == 5): #size dn
				fsize -=1

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False
				sys.exit(0)

