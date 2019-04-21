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

from PIL import Image
pil_im = Image.open('data/empire.jpg')
pil_im

pil_im = Image.open('data/empire.jpg').convert('L')
pil_im


# 1.1.1 画像のファイル形式変換
import os

filelist = ['foo.jpg', 'bar.bmp', 'zot.png']

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except:
            print "cannot convert", infile

import imtools
filelist = imtools.get_imlist('./data')
filelist

# 1.1.2 サムネイルの作成
pil_im = Image.open('data/empire.jpg')
pil_im.thumbnail((128, 128))
pil_im

# 1.1.3 領域のコピーと貼りつけ
pil_im = Image.open('data/empire.jpg')
box = (100, 100, 400, 400)
region = pil_im.crop(box)
region

region = region.transpose(Image.ROTATE_180)
pil_im.paste(region, box)
pil_im

# 拡大縮小と回転
pil_im = Image.open('data/empire.jpg')
out = pil_im.resize((128, 128))
out

pil_im = Image.open('data/empire.jpg')
out = pil_im.rotate(45)
out


