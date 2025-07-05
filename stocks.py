import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ('AAPL', 'META', 'TSLA')
colors = {
    'AAPL': ('red', 'blue'),
    'META': ('orange', 'violet'),
    'TSLA': ('yellow', 'green')
}

start_date = '2024-01-01'
end_date = '2025-01-01'

plt.figure(figsize=(16, 8))

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)

    data['Market Average'] = data['Close'].rolling(window=20).mean()

    latest_date = data.index[-1]
    closing_price = data['Close'].iloc[-1].item()
    average_price = data['Market Average'].iloc[-1].item()

    if pd.notna(closing_price) and pd.notna(average_price):
        print(f'{ticker} price on ({latest_date.date()}):')
        print(f'  • Closing price: ${closing_price:.2f}')
        print(f'  • 20-day Average: ${average_price:.2f}')
        print('--' * 40)
    else:
        print(f'{ticker} price on ({latest_date.date()}): Data Unavailable')

    close_color, avg_color = colors[ticker]
    plt.plot(data['Close'], label=f'{ticker} Closing Price', color=close_color)
    plt.plot(data['Market Average'], label=f'{ticker} 20-Day Avg', color=avg_color)


plt.title(f'Closing Prices & 20-Day Moving Averages for {", ".join(tickers)}')
plt.xlabel('Date')
plt.ylabel('Stock Price in USD ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()