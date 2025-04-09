# config/config.py

# Telegram Bot Token（自動填入）
TELEGRAM_TOKEN = '7479198697:AAHwy8OG8OZzcZjzyI6eRdP3YaCYcNVYR-I'
CHAT_ID = "5770539551"


# Telegram 貼圖 ID（妳提供過的貼圖 file_id）
STICKERS = {
    "上車": "CAACAgUAAxkBAAEJkx9lXYZxyzabc123",     # 火焰上車
    "下車": "CAACAgUAAxkBAAEJkyFlXYZxyzdef456",     # 雪崩下車
    "準備換車": "CAACAgUAAxkBAAEJkyPlXYZxyzghi789",  # 轉向箭頭
    "準備下車": "CAACAgUAAxkBAAEJkyhlXYZxyzjkl012",  # 漸弱提示
    "影轉強": "CAACAgUAAxkBAAEJkzBlXYZxyzmno345",     # 黑翻紅
    "影轉弱": "CAACAgUAAxkBAAEJkzJlXYZxyzpqr678",     # 紅翻黑
    "量爆弱": "CAACAgUAAxkBAAEJkzRlXYZxyzstu901",     # 突破反殺
}

# 貼圖冷卻時間（單張圖不會重複發送）
COOLDOWN_SECONDS = 600  # 每張圖冷卻 10 分鐘

# 幣種與週期設定
DEFAULT_SYMBOL = "TRX/USDT"
DEFAULT_INTERVAL = "3m"

# 模式控制
ENABLE_IMAGE_MODE = True
ENABLE_TEXT_MODE = True
DEBUG_MODE = False

# 通知簽章
SIGNATURE = {
    "判斷": "#影子判斷",
    "預測": "#影子預測"
}
