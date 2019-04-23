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
from PIL import Image
from pylab import *

im = array(Image.open('data/empire.jpg'))

imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x, y, 'r*')

plot(x[:2], y[:2])

title('Plotting: "empire.jpg"')
show()

# +
from PIL import Image
from pylab import *

im = array(Image.open('data/empire.jpg'))

imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x, y, 'r*')

plot(x[:2], y[:2])

title('Plotting: "empire.jpg"')

axis('off')

show()
# -

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'r*')

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'go-')

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'ks:')

# +
# 1.2.2
from PIL import Image
from pylab import *

im = array(Image.open('data/empire.jpg').convert('L'))

figure()

gray()

contour(im, origin='image')
axis('equal')
axis('off')
# -


figure()
hist(im.flatten(), 128)
show()

type(im)

array

# +
# 1.2.3
# Note: Jupyter notebook 上では動かない...
from PIL import Image
from pylab import *

im = array(Image.open('data/empire.jpg'))
imshow(im)
print '3点クリックしてください'
x = ginput(3)
print 'クリックした座標: ', x
show()
# -


