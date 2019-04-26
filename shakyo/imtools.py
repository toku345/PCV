# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np


def get_imlist(path):
    """ pathに指定されたディレクトリのすべてのjpgファイル名のリストを返す """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def imresize(im, sz):
    """ PILをつかって画像サイズを変更する """
    pil_im = Image.fromarray(uint8(im))
    return np.array(pil_im.resize(sz))


def histeq(im, nbr_bins=256):
    """ グレースケール画像のヒストグラム平坦化 """
    imhist, bins = np.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()       # 累積分布関数
    cdf = 255 * cdf / cdf[-1]   # 正規化

    # cdf を線形補間し、新しいピクセル値とする
    im2 = np.interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf


def compute_average(imlist):
    """ 画像の平均を求める """

    # 最初の画像を開き、浮動小数点の配列に変換
    averageim = np.array(Image.open(imlist[0], 'f'))

    for imname in imlist[1:]:
        try:
            averageim += np.array(Image.open(imname))
        except:
            print imname + '...skipped'
    averageim /= len(imlist)

    return np.array(averageim, 'uint8')
