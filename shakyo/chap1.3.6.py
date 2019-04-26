# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
# ---

from PIL import Image
from numpy import *
from pylab import *

# +
def pca(X):
    """ 主成分分析
    入力: X, 訓練データを平板化した配列を行として格納した行列
    出力: 写像行列（次元の重要度順）, 分散, 平均 """

    # 次元数を取得
    num_date, dim = X.shape

    # データをセンタリング
    mean_X =  X.mean(axis=0)
    X = X - mean_X

    if dim > num_date:
        # PCA - 高次元のときはコンパクトな裏技を用いる
        M = dot(X, X.T)         # 共分散行列
        e, EV = linalg.eigh(M)  # 固有値と固有ベクトル
        tmp = dot(X.T, EV).T    # ここがコンパクトな裏技
        V = tmp[::-1]           # 末尾の固有ベクトルほど重要なので、反転する
        S = sqrt(e)[::-1]       # 固有値の並びも反転する
        for i in range(V.shape[1]):
            V[:, i] /= S
    else:
        # PCA - 低次元なら特異値分解を用いる
        U, S, V = linalg.svd(X)
        V = V[:num_date]        # 最初のnum_dataの分が有用

    return V, S.mean_X
# -

# +
import glob
imlist = glob.glob('./data/a_thumbs/*')

im = array(Image.open(imlist[0])) # サイズを得るために画像を1つ開く
m, n = im.shape[0:2]
imnbr = len(imlist)

immatrix = array([array(Image.open(im)).flatten
                  for im in imlist], 'f')

V, S, immean = pca(immatrix)

figure()
gray()
subplot(2, 4, 1)
imshow(immean.reshape(m, n))
for i in range(7):
    subplot(2, 4, i+2)
    imshow(V[i].reshape(m, n))

show()
# -
