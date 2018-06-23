from PIL import Image, ImageDraw, ImageFont
font_img = Image.open("./9.jpeg")
draw = ImageDraw.Draw(font_img)
ttfront = ImageFont.truetype('./simhei.ttf',180)
draw.text((400,0),"99", fill=(255,0,0),font=ttfront)
font_img.save("./九.jpeg")