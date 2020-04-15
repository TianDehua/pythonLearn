from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, os.path
import random

currentPath = os.path.abspath(".")
thirdModulePath = os.path.join(currentPath, "thirdmodule")
picPath = os.path.join(thirdModulePath, "joy.png")

print('f=', picPath)
im = Image.open(picPath)

# 获取图像尺寸
# w, h = im.size
# print('original image size: %sx%s' % (w, h))

# # 缩放到50%
# im.thumbnail((w//2, h//2))
# # 把缩放后的图像png格式保存
# savePath = os.path.join(thirdModulePath, "thumbnail.png")
# im.save(savePath, 'png')

# # 模糊效果
# im2 = im.filter(ImageFilter.BLUR)
# blurPath = os.path.join(thirdModulePath, "blur.png")
# im2.save(blurPath, 'png')

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色，文字
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60*4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建font对象
font = ImageFont.truetype('arial.ttf', 36)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
#输出文字
for t in range(4):
    draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save(os.path.join(thirdModulePath, 'code.jpg'), 'jpeg' )


