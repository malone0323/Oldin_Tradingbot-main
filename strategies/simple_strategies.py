def moving_average_crossover(data, short_window=5, long_window=20):
    data["short_ma"] = data["close"].rolling(window=short_window).mean()
    data["long_ma"] = data["close"].rolling(window=long_window).mean()
    if data["short_ma"].iloc[-1] > data["long_ma"].iloc[-1]:
        return "BUY"
    elif data["short_ma"].iloc[-1] < data["long_ma"].iloc[-1]:
        return "SELL"
    return "HOLD"￼Enter
