# CryptoMind 🧠💰

![CryptoMind Logo](https://raw.githubusercontent.com/mySatoshist/CryptoMind/main/images/cryptomind_logo.png)

**CryptoMind** is a sophisticated technical analysis bot designed to help traders make informed decisions when trading Bitcoin and other cryptocurrencies. The bot analyzes market data, including moving averages, technical indicators, and market sentiment, to provide actionable recommendations. 🚀📈

## Features 🌟

- **Advanced Technical Analysis**: Uses multiple indicators (RSI, MACD, Bollinger Bands) to identify market trends. 📉📊
- **Real-time Bitcoin Data**: Fetches the latest market data for accurate analysis and recommendations. 💹
- **Smart Recommendations**: Provides clear buy, sell, or hold advice based on comprehensive technical analysis. 💸⚖️
- **Telegram Integration**: Easy-to-use Telegram bot interface for accessing analysis anywhere. 📱
- **Customizable Indicators**: Flexible framework for technical indicators and analysis parameters. ⚙️

## Technologies Used 🛠️

- **Gemini API**: Powers the AI analysis for context-aware recommendations. 🤖
- **LangChain**: For building sophisticated AI chains and processing. 🔗
- **yfinance**: Retrieves real-time and historical cryptocurrency data. 📊
- **Technical Indicators**: RSI, MACD, Bollinger Bands, ATR, VWAP, and more. 📈🔧
- **Telegram Bot API**: Provides an accessible interface for users. 💬

## How It Works 🔄

1. The bot fetches the latest Bitcoin data including price, volume, and historical data
2. It calculates key technical indicators (RSI, MACD, Bollinger Bands, etc.)
3. The data is processed through an AI analysis chain using Gemini API
4. A comprehensive recommendation is generated with justification
5. Users receive the analysis through a simple Telegram command

## Technical Analysis Example 📉

**Recommendation: Wait** ⏳

**Analysis:**

The current price ($82,449.68) is below both the short-term ($85,237.91) and long-term ($88,784.38) moving averages, indicating a downward trend. The MACD is negative (-1,011.09) and remains below the signal line (-1,155.54), reinforcing this bearish outlook.

The RSI (49.66) is neutral, but price proximity to the lower Bollinger Band ($80,607.19) suggests potential selling pressure. With 2.68% volatility, significant price fluctuations are possible.

**Risk assessment:** The downward trend may continue, potentially breaking through the lower Bollinger Band support.

**Summary:** Technical indicators suggest caution. Waiting for clearer trend reversal signals is the most prudent strategy at this time.

## Setup ⚙️

### Prerequisites 📋

- Python 3.8+
- Telegram account
- Google API key (for Gemini AI)

### Installation 📥

1. Clone the repository:
   ```bash
   git clone https://github.com/mySatoshist/CryptoMind.git
   cd CryptoMind
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file with the following:
   ```
   TELEGRAM_BOT_API_KEY=your_telegram_bot_token
   GOOGLE_API_KEY=your_gemini_api_key
   ```

### Running the Bot 🚀

Start the Telegram bot with:
```bash
python src/telegram_bot.py
```

Then, in Telegram:
1. Search for your bot using the username you created with BotFather
2. Start a conversation with `/start` or `/help`
3. Get Bitcoin analysis with `/analysis`

## Customization Options 🔧

- Modify `bot_tools.py` to adjust technical indicators or add new ones
- Edit prompts in `bot_prompts.py` to customize analysis style and format
- Change default analysis timeframe in `crypto_mind.py`

## Contributing 🤝

Contributions are welcome! To contribute:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments 👏

- Thanks to all the open-source projects that made this possible
- Special appreciation to the yfinance, Telegram API, and LangChain communities