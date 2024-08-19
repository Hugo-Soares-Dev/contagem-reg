import pygame
import time
pygame.mixer.init()
def toca_som():
    
    pygame.mixer.music.load('rock.mp3')

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print('Play')
toca_som()

