# log/log_tool.py

import os
import datetime

# 按日期儲存 log 檔：logs/2025-04-08.txt
LOG_PATH = f"logs/{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"

def write_log(tag, symbol, candle_data, prediction=None, level=None):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{now}] [{symbol}] [{tag}]"
    if prediction:
        message += f" 預測：{prediction}"
    if level:
        message += f" 等級：{level}"
    message += f"\nK棒: Open={candle_data['open']} High={candle_data['high']} Low={candle_data['low']} Close={candle_data['close']}\n"

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(message)
