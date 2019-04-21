# -*- coding: utf-8 -*-
import os

def get_imlist(path):
    """ pathに指定されたディレクトリのすべてのjpgファイル名のリストを返す """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
