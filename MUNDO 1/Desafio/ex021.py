import playsound
playsound.playsound('juliete.mp3')

import pygame
pygame.init()
pygame.mixer.music.load('juliete.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()