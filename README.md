# Telegram-Integrated System Monitor on AWS EC2

This project sets up a **system monitoring solution** on an **AWS EC2 instance** that sends **real-time system metrics and alerts to Telegram** using Python.

## 🚀 Features
- Monitor CPU, memory, and disk usage on an EC2 instance.
- Send instant alerts to a Telegram bot when thresholds are exceeded.
- Runs continuously as a background service for proactive monitoring.

## 🛠️ Tech Stack
- Python 🐍
- AWS EC2 ☁️
- Telegram Bot 🤖
- psutil for system metrics

## 💻 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/telegram-system-monitor.git
cd telegram-system-monitor
```

2. Install dependencies
```bash
pip install psutil requests 
```

3. Create Telegram Bot

- Message BotFather on Telegram to create a new bot.
- Copy the bot token and your chat ID.

4. Configure the script

- Replace `YOUR_BOT_TOKEN` and `YOUR_CHAT_ID` in `telegram_system_monitor.py`.

5. Run the script
```python
python telegram_system_monitor.py
```

6. Optional: Run as background service
```python
nohup python telegram_system_monitor.py &
```

## 🔧 Usage

- The script checks system metrics every 60 seconds (configurable).
- Sends Telegram alerts when CPU, memory, or disk usage exceeds thresholds.

## 📈 Lessons Learned

- Telegram API allows instant notifications without manual checks.
- psutil provides detailed real-time system metrics.
- Continuous monitoring improves server reliability and proactive maintenance.
