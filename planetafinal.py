#!/usr/bin/env python

import math 
import numpy as np
import pygame
import sys
from pygame.locals import *

class Planeta:
	def __init__ (self, name,  m, x, y, vx, vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.mass = m
		self.name = name

	def distanceS(self):
		return np.sqrt(self.x**2 + self.y**2)
	
	def distanceplanet(self, other):
		return np.sqrt( (self.x-other.x)**2 + (self.y-other.y)**2)	

	def move(self, other):
		self.ax = -G*self.x/self.distanceS()**3 -G*other.mass*(self.x-other.x)/self.distanceplanet(other)**3
		self.ay = -G*self.y/self.distanceS()**3 -G*other.mass*(self.y-other.y)/self.distanceplanet(other)**3

		self.x = self.x + self.vx*dt + 0.5*self.ax*dt**2
		self.y = self.y + self.vy*dt + 0.5*self.ay*dt**2

		self.vx = self.vx + self.ax*dt
		self.vy = self.vy + self.ay*dt

G = 4*np.pi**2
dt = 1e-3
MS = 1.98e30			#Massa do sol em kg -> massa do sol em AU = 1 AU
MT = 5.9742e24/MS		#Massa da terra em AU
MJ = 1.898e27/MS		#Massa de jupiter em AU
dist1 = 1.			#Raio da Terra em AU
dist2 = 5.202 			#Raio de Jupiter em AU
periodo1 = 1.			#Periodo: Terra (anos)
periodo2 = 11.89		#Periodo: Jupiter (anos)
vely1 = 2*np.pi*dist1/periodo1	#Velocidade inicial da Terra em y
vely2=	2*np.pi*dist2/periodo2	#Velocidade inicial de Jupiter em y


terra = Planeta("Terra", MT, dist1, 0, 0, vely1)
jupiter = Planeta("Jupiter", MJ, dist2, 0, 0, vely2)



##Inicialiazando o Pygame##

pygame.init()

screen = pygame.display.set_mode((600,600))
myfont = pygame.font.Font(None, 120)
space = pygame.image.load("milkyway.png").convert()
sun = pygame.image.load("sun.png").convert_alpha()
sun = pygame.transform.scale(sun,(60,60))
planet = pygame.image.load("planeta.png").convert_alpha()
planet = pygame.transform.scale(planet, (25,25))
outro = pygame.image.load("jupiter.png").convert_alpha()
outro = pygame.transform.scale(outro, (35,35))
sunw, sunh =sun.get_size()
pygame.display.set_caption('Sol, Terra e Jupiter')


while True:
	
	for event in pygame.event.get():	
		if event.type in (QUIT, KEYDOWN):
			sys.exit()

	screen.blit(space, (0,0))		
	screen.blit(sun, (300-sunw/2, 300-sunh/2))

	xant, yant = terra.x, terra.y
	terra.move(jupiter)
	jupiter.move(terra)
	dx = terra.x - xant
	dy = terra.y - yant
	angulo = math.atan2(dy, dx)
	angulo = (-math.degrees(angulo)+90)%360
	dayplanet = pygame.transform.rotate(planet, angulo)
	screen.blit(dayplanet, (terra.x*(250./4.5)+280, terra.y*(250./4.5)+280))
	screen.blit(outro, (jupiter.x*(250./4.5)+280, jupiter.y*(250./4.5)+280))
	pygame.display.update()

