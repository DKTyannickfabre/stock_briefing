import yfinance as yf
from crewai.tools import tool

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
        current_stock_price = stock_info.get('currentPrice', 'N/A')
        previous_close = stock_info.get('previousClose', 'N/A')
        fifty_two_week_high = stock_info.get('fiftyTwoWeekHigh', 'N/A')
        fifty_two_week_low = stock_info.get('fiftyTwoWeekLow', 'N/A')
        stock_news_headlines = stock.news if hasattr(stock, 'news') else []
        stock_summary = (
            f"Stock: {ticker}\n"
            f"Current Price: {current_stock_price}\n"
            f"Previous Close: {previous_close}\n"
            f"52-Week High: {fifty_two_week_high}\n"
            f"52-Week Low: {fifty_two_week_low}\n"
            f"News: {', '.join([article['title'] for article in stock_news_headlines[:5]])}\n"
        )
        if current_stock_price != 'N/A'and previous_close != 'N/A':
            stock_summary += f"Price Change: {(current_stock_price - previous_close)/previous_close * 100:.2f}%\n"
        else:
            stock_summary += "Price Change: not available\n"
        return stock_summary
    except Exception as e:
        return f"Error fetching data for {ticker}: {e}"