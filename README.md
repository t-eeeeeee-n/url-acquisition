# url-acquisition
### URL収集ツール
***
# 説明

対象ページから指定の要素を取得する

args1：URL

args2：取得要素キー

args3：csvExportPath

実行例
```shell
# main.py実行
./exe.sh "https://dev.classmethod.jp" "div.post-container a.link" "./csv/output.csv"
```