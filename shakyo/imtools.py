# -*- coding: utf-8 -*-
import os
from PIL import Image


def get_imlist(path):
    """ pathに指定されたディレクトリのすべてのjpgファイル名のリストを返す """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def imresize(im, sz):
    """ PILをつかって画像サイズを変更する """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))
