from PIL import Image,ImageDraw,ImageFont
import random
import operator
def text_on_img(filename=r'\01.png',size=12):
    opers = ['+', '-', '/', '*']
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    n1,n2 = random.randint(1, 20),random.randint(1, 5)
    opr = opers[random.randint(0, len(opers) - 1)]
    res = ops[opr](n1,n2)
    fnt = ImageFont.truetype('arial.ttf',size)
    text = str(n1) + ' ' + opr + ' ' + str(n2)
    image = Image.new(mode='RGB',size=(int(size/2)*len(text),size+50),color='blue')
    draw = ImageDraw.Draw(image)
    draw.text((10,10),text,font=fnt,fill=(255,255,0))
    filename = r'C:\sem-3\itws - 3\project\django_project\django_pro\static' + filename
    image.save(filename)
    return res

x = text_on_img(size=300)

print(x)