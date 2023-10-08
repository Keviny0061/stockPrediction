def fetch_data(self):
    ticker = self.ids.ticker_input.text
    if ticker:
        try:
            data = fetch_data(ticker)
            formatted_data = data.tail(1).to_string()  # Converts the last row of DataFrame to string
            self.ids.stock_info.text = formatted_data
        except Exception as e:
            self.ids.stock_info.text = f"Error: {str(e)}"
    else:
        self.ids.stock_info.text = "Please enter a valid stock ticker."
