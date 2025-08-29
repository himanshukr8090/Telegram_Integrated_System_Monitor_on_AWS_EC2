import psutil
import time
import requests

# -------------------------
# Telegram Bot Configuration
# -------------------------
TELEGRAM_TOKEN = 'YOUR_BOT_TOKEN'  # Replace with your Telegram bot token
CHAT_ID = 'YOUR_CHAT_ID'           # Replace with your chat ID
ALERT_INTERVAL = 60                # Seconds between checks

# -------------------------
# Thresholds
# -------------------------
CPU_THRESHOLD = 80      # %
MEMORY_THRESHOLD = 80   # %
DISK_THRESHOLD = 80     # %

# -------------------------
# Telegram Alert Function
# -------------------------
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

# -------------------------
# Monitoring Loop
# -------------------------
while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    alert_messages = []
    if cpu > CPU_THRESHOLD:
        alert_messages.append(f"⚠️ High CPU Usage: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        alert_messages.append(f"⚠️ High Memory Usage: {memory}%")
    if disk > DISK_THRESHOLD:
        alert_messages.append(f"⚠️ High Disk Usage: {disk}%")

    if alert_messages:
        message = "\n".join(alert_messages)
        send_telegram_message(message)

    time.sleep(ALERT_INTERVAL)

