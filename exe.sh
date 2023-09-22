# 対象URL
arg1=$1
# 取得要素キー
arg2=$2
# csvExportPath
arg3=$3
# main.py を呼び出す
python main.py "$arg1" "$arg2" "$arg3"

#LOG_OUT="./debug.log"
#LOG_ERR="./err.log"
#
## 標準出力
#echo "URL："$arg1 >> $LOG_OUT 2>> $LOG_ERR
