# predictor/third_candle_predictor.py

def predict_third_candle(candle1, candle2):
    """
    分析前兩根K棒，預測第三根K棒的趨勢方向
    - candle1: 前一根 K 棒
    - candle2: 當前這根 K 棒
    """

    # 條件一：連續紅K＋實體變長＋量放大
    is_red_red = candle1["close"] > candle1["open"] and candle2["close"] > candle2["open"]
    is_body_growth = candle2["body"] > candle1["body"]
    is_volume_up = candle2["volume"] > candle1["volume"]

    if is_red_red and is_body_growth and is_volume_up:
        return "續航強"

    # 條件二：紅轉黑 + 上影變長 + 量縮
    is_red_black = candle1["close"] > candle1["open"] and candle2["close"] < candle2["open"]
    is_upper_shadow_rise = candle2["upper_shadow"] > candle1["upper_shadow"]
    is_volume_down = candle2["volume"] < candle1["volume"]

    if is_red_black and is_upper_shadow_rise and is_volume_down:
        return "轉弱警"

    # 其餘不明顯狀況
    return "觀察中"
