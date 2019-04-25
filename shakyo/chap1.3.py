# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Default
#     language: python
#     name: python2
# ---

# +
# 1.3.1
from PIL import Image
from numpy import array

im = array(Image.open('data/empire.jpg'))
print im.shape, im.dtype

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
print im.shape, im.dtype
im
# -

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
i, j = 0, 1
im[i, :]

im[j, :]

im[i, :] = im[j, :]
im

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
im[:, i] = 100
im

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
im[:100, :50].sum()

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
im[50:100, 50:100]

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
im.mean()

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
im[:, -1]

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
im[-2, :]

im = array(Image.open('data/empire.jpg').convert('L'), 'f')
im[-2]


# +
# 1.3.2
from PIL import Image
from numpy import *

im = array(Image.open('data/empire.jpg').convert('L'))

im2 = 255 - im # 画像を反転

im3 = (100.0/255) * im + 100 # 明度を 100 ~ 200 の値に縮める

im4 = 255.0 * (im/255.0)**2 # 2乗する

print int(im.min()),  int(im.max())
print int(im2.min()), int(im2.max())
print int(im3.min()), int(im3.max())
print int(im4.min()), int(im4.max())
# -

print im2
Image.fromarray(im2)

print im3
# Image.fromarray(im3).convert("L")
Image.fromarray(uint8(im3))

print im4
# Image.fromarray(im4).convert('L')
Image.fromarray(uint8(im4))


# +
# 1.3.4
from PIL import Image
from numpy import *
import imtools

im = array(Image.open('data/AquaTermi_lowcontrast.JPG').convert('L'))
Image.fromarray(uint8(im))
# -


im2, cdf = imtools.histeq(im)
im2

cdf

Image.fromarray(uint8(im2))


