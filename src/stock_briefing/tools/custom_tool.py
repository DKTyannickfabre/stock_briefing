import yfinance as yf
from crewai.tools import tool
from datetime import datetime

@tool ('Get Stock Data')
def get_stock_data(ticker: str) -> str:
    """
    Fetches stock data for a given ticker symbol using yfinance.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple Inc.).

    Returns:
        str: A string representation of the stock data.
    """
    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.info
        stock_info_datetime = datetime.fromtimestamp(stock_info.get('regularMarketTime', 0)) if stock_info.get('regularMarketTime', None) else None
        current_stock_price = stock_info.get('currentPrice', 'N/A')
        previous_close = stock_info.get('previousClose', 'N/A')
        fifty_two_week_high = stock_info.get('fiftyTwoWeekHigh', 'N/A')
        fifty_two_week_low = stock_info.get('fiftyTwoWeekLow', 'N/A')
        stock_news_headlines = stock.news if hasattr(stock, 'news') else []
        stock_news_headlines_title = [
            news.get('content', {}).get('title', 'N/A') for news in stock_news_headlines
        ]
        stock_summary = (
            f"Stock: {ticker}\n"
            f"Date: {stock_info_datetime}\n"
            f"Current Price: {current_stock_price}\n"
            f"Previous Close: {previous_close}\n"
            f"52-Week High: {fifty_two_week_high}\n"
            f"52-Week Low: {fifty_two_week_low}\n"
            f"News: {', '.join(stock_news_headlines_title)}\n"
        )
        if current_stock_price != 'N/A'and previous_close != 'N/A':
            stock_summary += f"Price Change: {(current_stock_price - previous_close)/previous_close * 100:.2f}%\n"
        else:
            stock_summary += "Price Change: not available\n"
        return stock_summary
    except Exception as e:
        return f"Error fetching data for {ticker}: {e}"