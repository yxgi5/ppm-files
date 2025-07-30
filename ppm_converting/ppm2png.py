#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import cv2
import sys


 
def convert(filename):
    im = Image.open(filename)       # open ppm file
 
    newname = filename[:-4] + '.png'# new name for png file
    im.save(newname)                # save picture to new file
 
if "__main__" == __name__:
    filename= sys.argv[1]
    convert(filename)

# 存储PPM格式
im = Image.open('xxx.jpg')
im.save('xxx.ppm')

# 读取PPM格式
im = Image.open('xxx.ppm')
im.show()

'''
python ppm2png.py ppm-file.ppm
'''
i = cv2.imread('rgb888.ppm')
cv2.imwrite('rgb888.jpg',i)

i = cv2.imread('480x640a.ppm')
cv2.imwrite('480x640a.jpg',i)

im = Image.open('480x640a.jpg')
im.convert('RGB').save("480x640a.png","PNG")

imm = Image.open('480x640a.png')
imm.convert('RGB').save("480x640a.jpeg","JPEG")

immm = cv2.imread('480x640a.jpeg')
cv2.imwrite('480x640a_1.ppm',immm)

params=[0,0]
params[0] = cv2.IMWRITE_PXM_BINARY
params[1] = 0
cv2.imwrite('480x640a_2.ppm',immm, params)
'''
then in bash
#sed ':a;N;$!ba;s/ /\n/g' -i 480x640a_2.ppm #需要手动修改第2行
sed -i -e 'N' -e '2b' -e 's/ /\n/g' 480x640a_2.ppm # 空格用换行符替换
sed -i '/^$/d'  480x640a_2.ppm #去空行 
#sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g' file
#sed ':a;N;$!ba;s/ /\n/g' file 
'''
