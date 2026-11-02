from PIL import Image
import numpy as np
import re

def createImage(mode='L', size=(100, 100), color=255):
    image = Image.new(mode, size, color)
    np_image = np.array(image)

    print('\nBlank image created successfully.')
    print('Mode: ', mode)
    print('Size: ', size)
    print('Color :', color)

    return np_image

def randomPoint(x, y, v):
    return (np.random.randint(x-v, x+v), np.random.randint(y-v, y+v))

def bezierPoint(p1, p2, p3, p4, t):
    return (1-t)**3 * p1[0] + 3*(1-t)**2 * t * p2[0] + 3*(1-t)* t**2 * p3[0] + t**3 * p4[0],\
        (1-t)**3 * p1[1] + 3*(1-t)**2 * t * p2[1] + 3*(1-t)* t**2 * p3[1] + t**3 * p4[1]

def bezierCurve(img, p1, p2, p3, p4, steps, pixelValue = 0):
    p2 = randomPoint(p2[0], p2[1], p2[2])
    p3 = randomPoint(p3[0], p3[1], p3[2])

    for i in range(steps):
        i = i/steps
        x,y = bezierPoint(p1, p2, p3, p4, i)
        img[int(x), int(y)] = pixelValue

    return img

def parse(file):
    reg = r'\((\((\d+, ?){2}\d+\)){4}\)'
    data = []
    with open(file) as f:
        for i, lines in enumerate(f.readlines()):
            if re.search(reg, lines):
                curve = []
                content = lines.strip()[1:-1]
                point = re.split(r'\)\(', lines)
                for num in point:
                    num = num.replace('(', '')
                    num = num.replace(')', '')
                    co = re.split(r', ?', num)
                    curve.append((int(co[0]), int(co[1]), int(co[2])))
                data.append(curve)
            else:
                print(f"-- Syntax error on line {i+1}")
        return data

np_image = createImage()
parsed_data = parse(input('\nEnter the path of the generator file: '))
print(parsed_data)

pixelValue = int(input('\nEnter the pixel value for the curve: '))

for curve in parsed_data:
    np_image = bezierCurve(np_image, curve[0], curve[1], curve[2], curve[3], 100, pixelValue)

image = Image.fromarray(np_image)
image.save("outputs/generated_image.png")
print('\nBézier image saved successfully.')
image.show()