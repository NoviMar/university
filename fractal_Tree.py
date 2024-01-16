from PIL import Image, ImageDraw
import math as m


img = Image.new("RGB", (500, 500), "white")
idraw = ImageDraw.Draw(img)
x, y = 250, 250  

def draw_fractal(x,y,angle, length): 
    a = angle*m.pi / 180
    x1 = x + length*m.sin(a)
    y1 = y + length*m.cos(a)
    idraw.line((x, 500 - y, x1, 500 - y1), 'green', 1)
    if length>1:
        draw_fractal(x1, y1, angle + 40, length/1.47)
        draw_fractal(x1, y1, angle - 40, length/1.47)
        
draw_fractal(x, y, 0, 87)
img.show()