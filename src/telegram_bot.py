import telebot
import os
from dotenv import load_dotenv
from crypto_mind import *

load_dotenv()
telegram_bot_api_key = os.getenv("TELEGRAM_BOT_API_KEY", "")

help_commands = """
📊 *比特币分析机器人* 📊

可用命令：

/help       ---> 显示帮助信息
/analysis   ---> 执行比特币技术分析

这个机器人帮助您做出更明智的比特币交易决策，通过分析市场数据提供专业建议。
"""

try:
    print("机器人已启动！")
    bot = telebot.TeleBot(telegram_bot_api_key, parse_mode=None)

    @bot.message_handler(commands=["help", "start"])
    def help(message):
        bot.reply_to(message, help_commands)

    @bot.message_handler(commands=["analysis"])
    def analysis(message):
        bot.reply_to(message, crypto_mind_analysis())
    
    bot.infinity_polling()

except Exception as error:
    print(error)