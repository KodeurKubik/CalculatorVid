# PYTHON EXPORT giffer()

from graphic import draw_rectangle
from sys import exit

PIXEL_SIZE = 4
WIDTH, HEIGHT = 320 // PIXEL_SIZE, 240 // PIXEL_SIZE

def process_line(line, y):
    if line.strip() == '0':
        draw_rectangle(0, y * PIXEL_SIZE, WIDTH * PIXEL_SIZE, PIXEL_SIZE, [0, 0, 0])
        return

    colors = [list(map(int, clr.split('-'))) for clr in line.strip().split(',')]
    x = 0
    while x < len(colors):
        start_x = x
        current_color = colors[x]
        # Find the length of the current run of the same color
        while x < len(colors) and colors[x] == current_color:
            x += 1
        end_x = x
        # Draw the combined rectangle
        draw_rectangle(start_x * PIXEL_SIZE, y * PIXEL_SIZE, (end_x - start_x) * PIXEL_SIZE, PIXEL_SIZE, [current_color[2], current_color[1], current_color[0]])

    # Open the video file for reading in text mode ('r')
    with open('../videos.hpappdir/' + input('File ID: ') + '.txt', 'r', encoding='utf-8') as f:
        try:
            y = 0
            
            for line in f:
                process_line(line, y)
                if y == HEIGHT:
                    y = 0
                else:
                    y += 1

        except KeyboardInterrupt:
            print("\nProcess interrupted. Closing file...")
            f.close()
            exit(0)

# end
