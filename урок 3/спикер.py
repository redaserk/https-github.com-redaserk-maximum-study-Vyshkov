import pygame
from gtts import gTTS
pygame.mixer.init()
pygame.display.set_mode((200 , 100))
line = str(input("Введите текст для озвучивания: "))

my_file = open("text.txt", "a")
my_file.write(line)
my_file.close()


sth = gTTS(text = line, lang = 'ru')
sth.save('audio.mp3')

pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
