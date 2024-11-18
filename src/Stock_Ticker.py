def get_stock_tickers():
    Ticker = input("Enter stock ticker(s), in CAPS separated by commas: ")
    stock_ticker = [symbol.strip() for symbol in Ticker.split(",")]
    print("Stock ticker recorded")
    return stock_ticker


if __name__ == "__main__":
    stock_ticker = get_stock_tickers()
    print("You entered:", stock_ticker)
