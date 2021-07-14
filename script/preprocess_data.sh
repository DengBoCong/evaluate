# /bin/bash
dataset="daily_dialog_plusplus"

if [ -n "$1" ]; then
  dataset="$1"
fi

cd ../preprocess/
echo "开始执行原始数据 ${dataset} 的处理"


if [ $dataset == "daily_dialog_plusplus" ]; then
  python daily_dialog_plusplus.py
fi