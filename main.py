import pandas as pd
from utils.data_fetcher import fetch_historical_data
from strategies.simple_strategy import moving_average_crossover

SYMBOL = "BTCUSDT"
INTERVAL = "1h"

def main():
    # Fetch data
    data = fetch_historical_data(SYMBOL, INTERVAL)
    df = pd.DataFrame(data)
    
    # Run strategy
    signal = moving_average_crossover(df)
    print(f"Trading Signal: {signal}")
    
    # Placeholder for order execution
    if signal == "BUY":
        print("Executing BUY order...")
    elif signal == "SELL":
        print("Executing SELL order...")
    else:
        print("No action taken.")

if __name__ == "__main__":
    main()
