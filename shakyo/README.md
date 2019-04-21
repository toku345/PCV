# 写経用ディレクトリ


# 準備

## shellの設定に LC_ALL を設定

以下の設定を（なければ）追加する

```shell
# config.fish
set -x LC_ALL en_US.UTF-8

# .bash_profile, .zshenv など
export LC_ALL=en_US.UTF-8
```


## jupytext の設定

jupytext を使えるように設定する（初回のみ）

``` console
$ pipenv run jupyter notebook --generate-config # ~/.jupyter/jupyter_notebook_config.py 作成
```

好きなエディタで `~/.jupyter/jupyter_notebook_config.py` を開いて以下の2行を追加する

``` python
c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
c.ContentsManager.default_jupytext_formats = "ipynb,py"
```

# 画像データのダンロード

``` console
$ wget http://programmingcomputervision.com/downloads/pcv_data.zip .
$ unzip pcv_data.zip
```

# 起動

``` console
$ pipenv run jupyter notebook
```

# ライセンスについて

ipynb ファイルに出力されている画像ファイルのライセンスは Creative Commons Attribution 3.0 (CC BY 3.0) license です

``` text
These images and data files may be used freely under a Creative Commons Attribution 3.0 (CC BY 3.0) license.

Attribution should preferably cite the book "Programming Computer Vision with Python" by Jan Erik Solem (O'Reilly Media, 2012).

Full license text available here:
http://creativecommons.org/licenses/by/3.0/
```
