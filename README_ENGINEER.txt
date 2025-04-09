ShadowTact v5.7 安裝與注意事項（給工程師閱讀）

1. 啟動主程式為 main.py，請勿刪除或改動內部邏輯。
2. 所有 .py 檔案請保留原樣，尤其：
   - config/config.py（內含貼圖ID與模式設定）
   - bot/telegram_bot.py（處理 Telegram 通知）
   - trigger/image_trigger.py（處理貼圖冷卻）
   - log/log_tool.py（訊號紀錄用）
   - tactics/tactics.py（主邏輯）
   - predictor/third_candle_predictor.py（第三根K棒預測）
3. 預設幣種為 TRX/USDT，週期為 3 分鐘。
4. 本版本為貼圖通知 + 預測版，支援「上車／下車／準備下車／準備換車」。
5. 若需部署到 Render，需使用付費版本（Starter 以上），否則無法使用 HTTP 連線。
6. 請先執行以下指令安裝必要套件：
   pip install -r requirements.txt

請勿擅自修改冷卻時間、TOKEN、主程式判斷邏輯。

由影子戰術系統 ShadowTact 製作
