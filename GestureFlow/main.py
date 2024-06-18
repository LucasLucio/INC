#Importações das bibliotecas
import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

# Cria uma instância do controlador de teclado.
keyboard = Controller()

# Define a largura e altura da imagem capturada, exibição, e iniciliza a captura
width, height = 1280, 720 
hs, ws = 240, 420 
cam = cv2.VideoCapture(0)
cam.set(3, ws)
cam.set(4, hs)

# Define um limite para a detecção de gestos.
gestureThreshold = 300

 # Inicializa o detector de mãos com uma confiança de detecção de 0.8 e detectando no máximo uma mão.
detector = HandDetector(detectionCon=0.8, maxHands=1)

#Variável de controle para troca de slides
slideBlock = False

#Loop para processamento da imagem capturada em tempo real
while True:
    #Captura quadro, corrigem orientação da imagem, e verifica limite 
    success, img = cam.read()
    img = cv2.flip(img, 1)
    img = cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (100, 255, 205), 10)


    #Detecta as mãos na imagem
    hands, img = detector.findHands(img, flipType=False)  # flipType = Flase it will nt flip the img. right will remain right and vice versa.

    #Processa para caso encontrou uma mão
    if hands:

        #Seleciona a primeira mão, obtem estado dos dedos, obtem dados da localização da mão
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lm_list = hand['lmList']

        #Verifica se mão está no limite para detecção
        if cy <= gestureThreshold:

            #Verifica gesto slide anterior
            if fingers == [1, 1, 0, 0, 0] and slideBlock == True:
                keyboard.press(Key.down) #Pressiona tecla
                keyboard.release(Key.down) #Libera tecla
                slideBlock = False #Gerencia controle de slides
            

            #Verifica gesto próximo slide
            if fingers == [0, 0, 0, 0, 0] and slideBlock == True:
                keyboard.press(Key.up) #Pressiona tecla
                keyboard.release(Key.up) #Libera tecla
                slideBlock = False #Gerencia controle de slides

            #Verifica gesto para liberação de bloqueio dos slides
            if fingers == [1, 0, 0, 0, 0]:
                slideBlock = True #Gerencia controle de slides
    
    #Exibe imagem processada
    cv2.imshow('Image', img)

    #Aguarda chamada para encerramento
    KeyCV = cv2.waitKey(1)
    if KeyCV == ord('s'):
        break