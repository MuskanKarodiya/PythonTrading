import pandas as pd


def get_historical_data(symbol, from_date, to_date, resolution="D"):
    data = {
        "symbol": symbol,
        "resolution": resolution,
        "date_format": "1",
        "range_from": from_date,
        "range_to": to_date,
        "cont_flag": "1"
    }
    response = fyers.history(data)

    if 'candles' in response:
        # Convert data to DataFrame
        df = pd.DataFrame(response['candles'], columns=["timestamp", "open", "high", "low", "close", "volume"])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        return df
    else:
        print("Error fetching historical data:", response)
        return None


# Example usage
symbol = "NSE:RELIANCE"
from_date = "2023-01-01"  # Date format 'YYYY-MM-DD'
to_date = "2023-12-31"

historical_data = get_historical_data(symbol, from_date, to_date)
print(historical_data.head())
