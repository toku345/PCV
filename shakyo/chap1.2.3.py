# -*- coding: utf-8 -*-
# NOTE: うまく動かないときは → https://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49 などを参考に...
from PIL import Image
from pylab import *

im = array(Image.open('data/empire.jpg'))
imshow(im)
print '3点クリックしてください'
x = ginput(3)
print 'クリックした座標: ', x
show()
