# trigger/image_trigger.py

import time
from config.config import COOLDOWN_SECONDS

# 單圖冷卻紀錄（每張貼圖個別控制）
last_trigger_time = {
    "上車": 0,
    "下車": 0,
    "準備換車": 0,
    "準備下車": 0,
    "影轉強": 0,
    "影轉弱": 0,
    "量爆弱": 0,
}

# 全域冷卻：控制整體貼圖頻率（避免短時間內連發）
last_global_trigger = 0
GLOBAL_COOLDOWN = 90  # 秒

def can_trigger(tag):
    global last_global_trigger

    now = time.time()
    last_tag_time = last_trigger_time.get(tag, 0)

    # 全域冷卻未滿，不發圖
    if now - last_global_trigger < GLOBAL_COOLDOWN:
        return False

    # 單圖冷卻未滿，不發圖
    if now - last_tag_time < COOLDOWN_SECONDS:
        return False

    # 通過兩層條件，更新時間
    last_trigger_time[tag] = now
    last_global_trigger = now
    return True
