from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
import random
#随机颜色
def getrandomcolor():
    c1=random.randint(0,255)
    c2=random.randint(0,255)
    c3=random.randint(0,255)
    return (c1,c2,c3)
#随机验证码
def getrandomstr():
    s1=str(random.randint(0,9))
    s2=chr(random.randint(65,90))
    s3=chr(random.randint(97,122))
    randomstr=random.choice((s1,s2,s3))
    return randomstr
def main():
    image=Image.new("RGB",(150,30),getrandomcolor())
#将图片放入 绘画的地方
    img = ImageDraw.Draw(image)
#字体设置
    font=ImageFont.truetype("arial",size=32)
#生成4个随机字母和数字
    for i in range(4):
        randomstr=getrandomstr()
        img.text((10 + i * 40, 0), randomstr, getrandomcolor(), font=font)
#加入噪点噪线的方法一致，我觉得太乱了，就注释掉噪线
    width=150
    height=30
 #   for i in range(5):
 #       x1=random.randint(0,width)
  #      x2=random.randint(0,width)
   #     y1=random.randint(0,height)
    #    y2=random.randint(0,height)
     #   img.line((x1,y1,x2,y2),fill=getrandomcolor())

    for i in range(30):
        img.point([random.randint(0, width), random.randint(0, height)], 'gray')
        x = random.randint(0, width)
        y = random.randint(0, height)
        img.arc((x, y, x + 4, y + 4), 0, 90, fill=getrandomcolor())

    photo = image.filter(ImageFilter.MinFilter)
    photo.save(r'C:\Users\qqq\PycharmProjects\untitled\python小项目\ten.png', 'png')

main()

