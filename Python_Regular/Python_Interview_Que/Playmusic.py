import pygame
import time

def playmusic(song):
    pygame.mixer.init()
    sound_file = song
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    time.sleep(10)
    sound.stop()
while True:
    print("choose a type of music to play:")
    print("1.Hindi")
    print("2.Punjabi")
    print("3.Telugu")
    print("4.Tamil")
    print("5.Exit")
    choice = int(input("Enter the number of your choice:"))
    match choice:
      case 1:
          playmusic('Spark.mp3')
      case 2:
          playmusic('punjabi.mp3')
      case _:
          print("not available")
          break