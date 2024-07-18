import cv2

video = cv2.VideoCapture(r'./video.mp4')

def is_close_to_black(pixel, threshold=20):
    # Check if any of the RGB values are below the threshold
    return all(component < threshold for component in pixel)

with open('video.txt', 'w') as file:  # Use 'w' for writing text data
    currentframe = 0
    while True:
        ret, frame = video.read()

        if not ret:
            break
        
        for y in range(frame.shape[0]):
            filtered_pixels = [pixel for pixel in frame[y] if not is_close_to_black(pixel)]
            if filtered_pixels:
                line = ','.join('-'.join(map(str, pixel)) for pixel in frame[y])
            else:
                line = '0'
            file.write(line + '\n')
        
        currentframe += 1

video.release()
