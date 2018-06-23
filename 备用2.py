from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
def getRandomColor():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)
def getRandomStr():
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])

    return random_char
image = Image.new('RGB', (150, 30), getRandomColor())
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial", size=26)

for i in range(5):
    random_char = getRandomStr()

    draw.text((10 + i * 30, 0), random_char, getRandomColor(), font=font)
image.save(open('test.png', 'wb'), 'png')