# /bin/bash

modules="preprocess"
addition="daily_dialog_plusplus"

if [ -n "$1" ] && [ -n "$2" ]; then
  modules="$1"
  addition="$2"
fi

if [ "$modules" = "preprocess" ]; then
  cd script/
  sh preprocess_data.sh "$addition"
fi
