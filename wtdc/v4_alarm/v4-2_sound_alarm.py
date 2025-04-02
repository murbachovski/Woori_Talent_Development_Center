# pip install pygame
import pygame

pygame.mixer.init()
# pygame.mixer.music.load('C:/Users/Administrator/Desktop/ai/wtdc/v4_alarm/input.mp3')
pygame.mixer.music.load('wtdc/v4_alarm/input.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

print("SUCCESS")