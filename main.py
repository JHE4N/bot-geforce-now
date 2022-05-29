#bot que lê o que está na tela 
#pip install pyautogui
#pip install opencv-python
#pip install pytesseract
#pip install playsound==1.2.2
#pip install pygobject gg sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
#pip intall  gTTS
#sudo apt-get install scrot
#sudo apt-get install python3-tk python3-dev
#sudo apt-get install tesseract-ocr tesseract-ocr-por
#erro? https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
import pyautogui, time, cv2, pytesseract, gtts, pygame
from playsound import playsound

def gambiarra():
    pygame.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

frase = 'Jogadores na sua frente:'
#deixe o zoom da tela do game em 150%
time.sleep(5)
pyautogui.screenshot('img.png')
time.sleep(5)
img = cv2.imread('img.png')
texto = pytesseract.image_to_string(img)
if frase not in texto:
    print('[ERRO] Não encontrei a frase: ' + frase)
else:
    pos = texto.find(frase)
    #mostrar a posição [] que está a frase
    print('Está na tela')
    jogadores_a_frente = texto[pos + 25: pos +28]
    jogadores_a_frente = jogadores_a_frente + ' jogadores na sua frente'
    song = gtts.gTTS(jogadores_a_frente, lang='pt-br').save('audio.mp3')
    gambiarra()
