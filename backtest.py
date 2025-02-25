import pandas as pd
from strategies.simple_strategy import moving_average_crossover

def backtest_strategy(data):
    data["signal"] = data.apply(moving_average_crossover, axis=1)
    # Calculate profit/loss based on signals
    # (Implementation depends on specifics)
