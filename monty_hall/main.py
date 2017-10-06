#!/usr/bin/python

import pygame, sys
from pygame.locals import *
import random
import time
from time import sleep
from datetime import datetime
from os import path



pygame.init()
pygame.mixer.init()


display_width = 1400
display_height = 1300

# Folder path init
media = path.join(path.dirname(__file__), 'media')


x_message = 0.2*display_width
y_message = 70

clock = pygame.time.Clock()
random.seed(datetime.now())

pygame.font.init() 
myfont = pygame.font.SysFont(None, 29)
titlefont = pygame.font.SysFont(None, 50)

gameExit = False
gameOver = False
FPS = 100
#set your own sleeptime to show effect slowly
sleepTime = 0
numOfWins = numOfGames = numOfLosses = 0
numOfSwaps = 0
numOfWinsBySwap = 0

#-------Colors-------#
black = (0,0,0)
white = (255,255,255)
lime = (0,255,0) #lime
yellow = (255,255,0) #yellow
#-------Colors-------#

#-------Coordinates-------#
x1 = (0.2*display_width)
y1 = y2 = y3 = (0.2*display_height)
x2 = (0.45*display_width)
x3 = (0.7*display_width)
#-------Coordinates-------#

#----------------Images and Sounds-----------------#
door1Image = pygame.image.load(path.join(media + '/door1.jpg'))
door2Image = pygame.image.load(path.join(media + '/door2.jpg'))
door3Image = pygame.image.load(path.join(media + '/door3.jpg'))
openGoatImage = pygame.image.load(path.join(media + '/opengoat.jpg'))
openCarImage = pygame.image.load(path.join(media + '/opencar.jpg'))
backgroundImage = pygame.image.load(path.join(media + '/background.jpg'))
congoImage = pygame.image.load(path.join(media + '/congo.gif'))
oopsImage = pygame.image.load(path.join(media + '/oops.png'))
gameSound = path.join(media+'/gameSound.mp3')
gameIcon = pygame.image.load(path.join(media + '/gameIcon.jpeg'))
startImage = pygame.image.load(path.join(media + '/startImage.jpeg'))
promptImage = pygame.image.load(path.join(media + '/prompt.png'))
#---------------------------------------#

gameDisplay = pygame.display.set_mode((display_width,display_height), RESIZABLE)
pygame.display.set_caption('Monty Hall problem')
pygame.display.set_icon(gameIcon)

backgroundRect = backgroundImage.get_rect()
startImageRect = startImage.get_rect()
# congoRect = congoImage.get_rect()
# gameDisplay.blit(backgroundImage, backgroundRect)
# pygame.display.update()

# pygame.mixer.music.load('foo.mp3')
# pygame.mixer.music.play(0)


doorImageList = [door1Image, door2Image, door3Image]
coordinates = [[x1,y1], [x2,y2], [x3,y3]]  
possibleImageList = [openCarImage, openGoatImage]
imageList = [0,1,2]




def displayImage(x,y,currentImage):
	gameDisplay.blit(currentImage, (x,y))

def showMessage(message, x, y):
	textsurface = myfont.render(message, True, yellow)
	gameDisplay.blit(textsurface,(x,y))

def setImagesRandomly():
	randomList = random.sample(range(0, 3), 3)
	imageList[randomList[0]] = possibleImageList[1]
	imageList[randomList[1]] = possibleImageList[0]
	imageList[randomList[2]] = possibleImageList[1]


def displayStartImages():
	displayImage(coordinates[0][0],coordinates[0][1],doorImageList[0])
	displayImage(coordinates[1][0],coordinates[1][1],doorImageList[1])
	displayImage(coordinates[2][0],coordinates[2][1],doorImageList[2])

def displayRandomlySetImages():
	displayImage(coordinates[0][0],coordinates[0][1],imageList[0])
	displayImage(coordinates[1][0],coordinates[1][1],imageList[1])
	displayImage(coordinates[2][0],coordinates[2][1],imageList[2])

def revealImage(doorNumber):
	displayImage(coordinates[doorNumber][0], coordinates[doorNumber][1], imageList[doorNumber])

def findRatio():
	global numOfLosses, numOfWins, numOfWinsBySwap, numOfSwaps
	if numOfSwaps==0 or numOfWins==numOfWinsBySwap:
		showMessage('Wins(With Swap):Wins(Without Swap) = Infinite', x_message+500, y_message+100)

	else:
		ratio = 1.0*(numOfWinsBySwap*(numOfGames - numOfSwaps))/(numOfSwaps*(numOfWins - numOfWinsBySwap))
		showMessage('Wins(With Swap):Wins(Without Swap) = '+str(ratio), x_message+500, y_message+100)

def displayGoat(keyValue):
	randomList = random.sample(range(0, 3), 3)
	for i in range(len(imageList)):
		if randomList[i] != keyValue and imageList[randomList[i]] != openCarImage:
			revealImage(randomList[i])
			return randomList[i]

def validate(doorNumber):
	global numOfWins, numOfLosses, numOfGames
	if imageList[doorNumber] == openCarImage:
		numOfWins += 1
		numOfGames += 1
		displayImage(display_width/2.5, display_height/2.5, congoImage)
		showMessage('Enter q to update the score and play again.', x_message, y_message+100)
		return 1
	else:
		numOfLosses += 1
		numOfGames += 1
		displayImage(display_width/2.5, display_height/2.5, oopsImage)
		showMessage('Enter q to update the score and play again.', x_message, y_message+100)
		return 0


def displayDetails():
	showMessage('Number of Games = '+str(numOfGames), x_message+500, y_message)
	showMessage('Number of Wins = '+str(numOfWins), x_message+500, y_message+20)
	showMessage('Number of Losses = '+str(numOfGames - numOfWins), x_message+500, y_message+40)
	showMessage('With swap => Won '+str(numOfWinsBySwap) +' out of ' +str(numOfSwaps), x_message+500, y_message+60)
	showMessage('Without swap => Won '+str(numOfWins- numOfWinsBySwap) +' out of ' +str(numOfGames - numOfSwaps), x_message+500, y_message+80)
	findRatio()



def awardTheGuest(keyValue, doorNumber):
	global numOfSwaps, numOfWinsBySwap
	gameOver = False
	showMessage('Would you like to swap your choice[Y/N]:', x_message, y_message+60)
	pygame.display.update()
	while not gameOver:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:                  
				if event.key == pygame.K_n:
					showMessage('You chose not to Swap.', x_message, y_message+80)
					pygame.display.update()
					time.sleep(sleepTime)
					validate(keyValue)
					revealImage(keyValue)
					pygame.display.update()
					gameOver = True
					break

				if event.key == pygame.K_y:
					numOfSwaps += 1
					showMessage('You chose to Swap.', x_message, y_message+80)
					pygame.display.update()
					for i in range(3):
						if i not in [doorNumber, keyValue]:
							time.sleep(sleepTime)
							x = validate(i)
							revealImage(i)
							if(x == 1):
								numOfWinsBySwap += 1
							pygame.display.update()
							gameOver = True
							break

			if event.type == pygame.QUIT:
				gameOver = True
				pygame.quit()
				quit()
				break

				



def main():
	play = False
	pygame.mixer.music.load(gameSound)
	pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.
	gameDisplay.blit(startImage, startImageRect)
	displayImage(135, 50, promptImage)
	pygame.display.update()
	while not play:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					play = True
					break

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				break

	while not gameExit:
		gameOver = False
		gameDisplay.fill(white)
		gameDisplay.blit(backgroundImage, backgroundRect)
		displayStartImages()
		showMessage("Follow the Instructions Below:", x_message, y_message)
		textsurface = titlefont.render('!--Welcome to Monty Hall Game--!', True, lime)
		gameDisplay.blit(textsurface,(0.3*display_width,15))
		showMessage("Press Key 1, 2 or 3 to Choose Corresponding Door:", x_message, y_message+20)
		displayDetails()
		pygame.display.update()
		setImagesRandomly()
		while not gameOver:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = True
						break
						
					if event.key == pygame.K_1:
						showMessage("You Chose Door1!", x_message, y_message+40)
						pygame.display.update()
						time.sleep(sleepTime)
						revealedDoor = displayGoat(0)
						time.sleep(sleepTime)
						pygame.display.update()
						time.sleep(sleepTime)
						awardTheGuest(0, revealedDoor)
						
			  

					if event.key == pygame.K_2:
						showMessage("You Chose Door2!", x_message, y_message+40)
						pygame.display.update()
						time.sleep(sleepTime)
						revealedDoor = displayGoat(1)
						time.sleep(sleepTime)
						pygame.display.update()
						time.sleep(sleepTime)
						awardTheGuest(1, revealedDoor)
						
				   

					if event.key == pygame.K_3:
						showMessage("You Chose Door3!", x_message, y_message+40)
						pygame.display.update()
						time.sleep(sleepTime)
						revealedDoor = displayGoat(2)
						time.sleep(sleepTime)
						pygame.display.update()
						time.sleep(sleepTime)
						awardTheGuest(2, revealedDoor)

						


				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					break

			
			clock.tick(FPS)



main()

pygame.quit()
quit()