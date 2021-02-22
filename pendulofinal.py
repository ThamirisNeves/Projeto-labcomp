#!/usr/bin/env python

import numpy as np
import pygame
import sys
from pygame.locals import *
import math

class Pendulo:	
	def __init__ (self, x, v, a, massa):
		self.x = x
		self.v = v
		self.a = a
		self.m = massa

	def verlet(self):
		xtent = self.x+ self.v*dt +0.5*self.a*dt**2
		#if(xtent >= np.pi):
		#	xtent = -2*np.pi + xtent
		#elif(xtent <= -np.pi):
		#	xtent = 2*np.pi - xtent
		self.x = xtent
		atmp = (-(w**2/self.m)*np.sin(self.x) -(gama/self.m)*self.v + A*np.sin(wf*t))
		vtmp = (self.v + 0.5*(self.a + atmp)*dt)
		atmp = (-(w**2/self.m)*np.sin(self.x)-(gama/self.m)*vtmp + A*np.sin(wf*t))
		self.v = self.v + 0.5*(self.a + atmp)*dt
		self.a = (-(w**2/self.m)*np.sin(self.x)-(gama/self.m)*self.v+A*np.sin(wf*t))

t = 0
dt = 1e-2
gama = 0.5
w = 1**0.5
m = 1.
A = 2.
wf = 2./3.
m = 1.
t=0

x1 = 1.			#Posicao inicial de x1
x2 = 0.9999		#Posicao inicial de x2

#Parametros para classe
pendulo1 = Pendulo(x1, 0, -(w**2/m)*np.sin(x1) + A*np.sin(wf*t), m) 	
pendulo2 = Pendulo(x2, 0, -(w**2/m)*np.sin(x1) + A*np.sin(wf*t), m)

##Inicializando Pygame##
pygame.init()
screen = pygame.display.set_mode((600,600))
myfont = pygame.font.Font(None,120)
fundo = pygame.image.load("fundo.jpg").convert()
bola = pygame.image.load("bola.png").convert_alpha()
color = 0, 0, 255
color2 = 255, 255, 0

bola = pygame.transform.scale(bola,(50,50))
posx1,posy1 = np.cos(pendulo1.x),np.sin(pendulo1.x)
posx2,posy2 = np.cos(pendulo2.x),np.sin(pendulo2.x)

while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	screen.blit(fundo,(0,0))
	
	pendulo1.verlet()
	pendulo2.verlet()

	posx1,posy1 = np.cos(pendulo1.x),np.sin(pendulo1.x)
	posx2,posy2 = np.cos(pendulo2.x),np.sin(pendulo2.x)
		
	pygame.draw.line(screen, color, (300, 300),(posx1*600/4+320, posy1*600/4+320), 10) 
	pygame.draw.line(screen, color2, (300, 300),(posx2*600/4+320, posy2*600/4+320), 10)  

	screen.blit(bola,(posx1*600/4+300,posy1*600/4+300))
	screen.blit(bola,(posx2*600/4+300,posy2*600/4+300))
	pygame.display.update()

	t=t+dt

