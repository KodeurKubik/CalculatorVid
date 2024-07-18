import cv2

video = cv2.VideoCapture(r'./video.mp4')


COLORS = []
with open('video.txt', 'w') as file:
    file.flush()
    currentframe = 0
    while(True):
        # if currentframe > 1: break
        ret,frame = video.read()

        if ret:
            print('Captured ' + str(currentframe))
            
            framelist = frame.tolist()
            
            for x in framelist:
                file.write(','.join(['-'.join(map(str, sublist)) for sublist in x]) + '\n')
                
            
            currentframe += 1
        else: 
            break
    
    file.close()

video.release() 
cv2.destroyAllWindows()
