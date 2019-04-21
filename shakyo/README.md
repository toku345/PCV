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
