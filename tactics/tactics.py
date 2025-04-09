def score_to_level(score):
    if score >= 4:
        return "A"
    elif score == 3:
        return "B"
    else:
        return "C"

def detect_entry_candle(candle):
    score = 0
    if candle['close'] > candle['open']:
        score += 1
    if candle['volume'] > candle['prev_volume'] * 1.2:
        score += 1
    if candle['body'] > candle['prev_body']:
        score += 1
    if candle['upper_shadow'] < candle['body']:
        score += 1
    return score, score_to_level(score)

def detect_exit_signal(candle):
    score = 0
    if candle['close'] < candle['open']:
        score += 1
    if candle['body'] < candle['prev_body']:
        score += 1
    if candle['volume'] < candle['prev_volume']:
        score += 1
    if candle['prev_body'] > 0 and (candle['body'] / candle['prev_body']) < 0.5:
        score += 1
    return score, score_to_level(score)

def detect_prepare_switch(candle):
    score = 0
    if candle['upper_shadow'] > candle['body'] * 1.5:
        score += 1
    if candle['close'] > candle['open'] and candle['body'] < candle['prev_body']:
        score += 1
    if candle['volume'] < candle['prev_volume']:
        score += 1
    return score, score_to_level(score)

def detect_prepare_exit(candle):
    score = 0
    if candle['close'] > candle['open'] and candle['body'] < candle['prev_body']:
        score += 1
    if candle['volume'] < candle['prev_volume']:
        score += 1
    if candle['upper_shadow'] > candle['body']:
        score += 1
    return score, score_to_level(score)
