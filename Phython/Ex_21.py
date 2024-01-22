'''DESAFIO MP3 PLAYER'''
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('amusic.mp3')
pygame.mixer.music.play()
pygame.event.wait()
