

import random, string
from PIL import Image,ImageDraw
from io import BytesIO

def get_random_char():
    char = ''
    ran = string.ascii_lowercase + string.digits

    for i in range(4):
        char += random.choice(ran)

    return char

def get_random_color():
    return (random.randint(50,300),random.randint(50,150),random.randint(50,200))

def create_code():
    img = Image.new('RGB', (120,30),(255,255,255))
    drow = ImageDraw.Draw(img)

    code = get_random_char()

    for i in range(4):
        drow.text((30*i+5,0),code[i],get_random_color())

    line_number = random.randint(1,5)
    for j in range(line_number):
        begin = (random.randint(0,120),random.randint(0,30))
        end = (random.randint(0,120), random.randint(0,30))

        drow.line([begin,end],fill=(0,0,0))

        img.save(''.join(code)+'.jpg','jpeg')
        print(img,code)

        return img,code

f = BytesIO()
img,code = create_code()

print(img)

