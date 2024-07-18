from graphic import draw_rectangle


PIXEL_SIZE = 4
WIDTH, HEIGHT = 320 / PIXEL_SIZE, 240 / PIXEL_SIZE

with open('../videos.hpappdir/' + input('File ID: ') + '.txt') as f:
    y = 0
    for line in f:
        colors = [list(map(int, clr.split('-'))) for clr in line.split(',')]
        
        for x in range(len(colors)):
            draw_rectangle(x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE, [colors[x][2], colors[x][1], colors[x][0]])
             
        if y == HEIGHT: y = 0
        y += 1
