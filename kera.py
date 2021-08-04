import cv2
# import numpy as np
# import tensorflow.keras
import minimax

img = cv2.imread('board\\0.jpg')
gamestate = [["-","-","-"],["-","-","-"],["-","-","-"]]
imgArr1 = [[[5,5,240,160],[240,5,240,160],[480,5,240,160]],[[5,160,240,160],[240,160,240,160],[480,160,240,160]],
           [[5,320,240,160],[240,320,240,160],[480,320,240,160]]]
players = ['X','O']

# data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# np.set_printoptions(suppress=True)
# model = tensorflow.keras.models.load_model('keras_model.h5')
player, gamestate = minimax.go_first(gamestate) 
while True:
    
    
    if player == 2:
        row,cell = minimax.findBestMove(gamestate)
        gamestate[row][cell] = "X"
    if player == 1:
        move = int(input('hang: '))
        move1 = int(input('o: '))
        gamestate[move][move1] = "O"

    
    
    # for i in range(len(imgArr1)):
    #     for j in range(len(imgArr1[i])):
    #         x,y,w,h = imgArr1[i][j]
    #         imgCrop = img[y:y+h,x:x+w]
    #         # cv2.imshow('img', imgCrop)
    #         # cv2.waitKey(500)
    #         image = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2RGB)
    #         img1 = cv2.resize(image,(224, 224))
    #         image_array = np.asarray(img1)
    #         normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    #         data[0] = normalized_image_array
    #         prediction = model.predict(data)
    #         index_max = np.argmax(prediction)
    #         Gia_tri_max = prediction[0][index_max]
    #         if index_max == 1 :
    #             gamestate[i][j] = 'X'
    #         if index_max == 0 :
    #             gamestate[i][j] = 'O'
        
    
        
        
    for row in range(len(gamestate)):
        for cell in range(len(gamestate[row])):
            if gamestate[row][cell] == 'X':
                x,y,w,h = imgArr1[row][cell]
                cv2.line(img,(x+20,y+20),(x+w-20,y+h-20),(255,0,0),5)
                cv2.line(img,(x+w-20,y+20),(x+20,y+h-20),(255,0,0),5)
            if gamestate[row][cell] == 'O':
                x,y,w,h = imgArr1[row][cell]
                centerx = int(x + (w/2))
                centery = int(y + (h/2))
                cv2.circle(img,(centerx,centery),70,(255,0,0),5)
            
    if minimax.isGameEnd(gamestate):
        cv2.putText(img,'Game Over', (160,160), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,0))
        cv2.imshow('img',img)
        cv2.waitKey(20000)
        break
            
    
    # if utls.win_condition(gamestate, players[0]):
    #     break
    # if utls.win_condition(gamestate, players[1]):
    #     break
    # if np.array(gamestate).flatten().tolist().count("-") == 0:
    #     break
    cv2.imshow('img', img)
    cv2.waitKey(20000)
    player = minimax.switch(player)
    k = cv2.waitKey(1)
    if k%256 == 32:
        break
# cv2.circle(img, (242,163),2,(0,255,0),-1)
# cv2.circle(img, (5,163),2,(0,255,0),-1)
# cv2.circle(img, (245,5),2,(0,255,0),-1)
# cv2.circle(img, (7,5),2,(0,255,0),-1)


# cv2.imshow('img', img)
# # cv2.imwrite('board.png',img)
# cv2.waitKey()
cv2.destroyAllWindows()
