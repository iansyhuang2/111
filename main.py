# main.py

from tactics.tactics import *
from trigger.image_trigger import can_trigger
from bot.telegram_bot import notify
from log.log_tool import write_log
from config.config import DEFAULT_SYMBOL
from predictor.third_candle_predictor import predict_third_candle
import time

print("🖤 影子系統已啟動，正在等待訊號...")

# 模擬三根K棒資料（實戰時應接API）
def get_latest_candles():
    return [
        {
            'open': 0.066, 'high': 0.069, 'low': 0.065, 'close': 0.068,
            'volume': 100000, 'body': 0.002, 'prev_body': 0.0015, 'prev_volume': 95000, 'upper_shadow': 0.001,
        },
        {
            'open': 0.067, 'high': 0.072, 'low': 0.067, 'close': 0.071,
            'volume': 121000, 'body': 0.004, 'prev_body': 0.002, 'prev_volume': 100000, 'upper_shadow': 0.0012,
        },
        {
            'open': 0.070, 'high': 0.073, 'low': 0.069, 'close': 0.072,
            'volume': 132000, 'body': 0.005, 'prev_body': 0.003, 'prev_volume': 125000, 'upper_shadow': 0.0018,
        }
    ]


def main():
    while True:
        try:
            candles = get_latest_candles()
            symbol = DEFAULT_SYMBOL

            prev_candle = candles[0]
            last_candle = candles[1]
            current_candle = candles[2]

            prediction = predict_third_candle(prev_candle, last_candle)

            # 上車訊號處理
            score, level = detect_entry_candle(current_candle)
            if level == "A" and prediction == "續航強" and can_trigger("上車"):
                notify(CHAT_ID, "上車", f"{symbol} 上車機會（預測續航）")
                write_log("上車", symbol, current_candle, prediction, level)
            else:
                write_log("上車略過", symbol, current_candle, prediction, level)

            # 下車訊號處理
            score, level = detect_exit_signal(current_candle)
            if level == "A" and can_trigger("下車"):
                notify(CHAT_ID, "下車", f"{symbol} 下車警示")
                write_log("下車", symbol, current_candle, None, level)
            else:
                write_log("下車略過", symbol, current_candle, None, level)

            # 準備換車處理
            score, level = detect_prepare_switch(current_candle)
            if level == "A" and can_trigger("準備換車"):
                notify(CHAT_ID, "準備換車", f"{symbol} 多空轉折警示")
                write_log("準備換車", symbol, current_candle, None, level)
            else:
                write_log("準備換車略過", symbol, current_candle, None, level)

            # 準備下車處理
            score, level = detect_prepare_exit(current_candle)
            if level == "A" and can_trigger("準備下車"):
                notify(CHAT_ID, "準備下車", f"{symbol} 趨勢減弱預警")
                write_log("準備下車", symbol, current_candle, None, level)
            else:
                write_log("準備下車略過", symbol, current_candle, None, level)

            time.sleep(60)

        except Exception as e:
            print(f"發生錯誤: {e}")
            write_log("系統錯誤", symbol, None, f"錯誤: {e}", "E")
            time.sleep(60)  

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"程式崩潰: {e}")
        write_log("系統錯誤", "全局", None, f"主程式異常: {e}", "E")
