# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from PIL import Image
from numpy import *
from scipy.ndimage import filters

import matplotlib.pyplot as plt
# -

im = array(Image.open('data/empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im, 5)

plt.imshow(im)

plt.imshow(im2)

plt.imshow(array(Image.open('data/empire.jpg')))

im = array(Image.open('data/empire.jpg'))
im2 = zeros(im.shape)

im2

# カラー画像は色チャンネルごとにぼかしをかける
for i in range(3):
    im2[:, :, i] = filters.gaussian_filter(im[:, :, i], 5)
im2 = uint8(im2)

plt.imshow(im2)


