# risk_manager.py

class RiskManager:
    def __init__(self, account_balance, risk_per_trade=0.01, max_drawdown=0.2):
        """
        Initializes the RiskManager.
        
        :param account_balance: Total account balance.
        :param risk_per_trade: Percentage of account balance to risk per trade (e.g., 0.01 for 1%).
        :param max_drawdown: Maximum drawdown as a percentage of the account balance (e.g., 0.2 for 20%).
        """
        self.account_balance = account_balance
        self.risk_per_trade = risk_per_trade
        self.max_drawdown = max_drawdown
        self.initial_balance = account_balance
        self.current_drawdown = 0.0

    def calculate_position_size(self, entry_price, stop_loss_price):
        """
        Calculates the position size based on risk per trade and stop loss distance.
        
        :param entry_price: Entry price for the trade.
        :param stop_loss_price: Stop loss price for the trade.
        :return: Position size in units or contracts.
        """
        risk_amount = self.account_balance * self.risk_per_trade
        stop_loss_distance = abs(entry_price - stop_loss_price)
        position_size = risk_amount / stop_loss_distance
        
        return position_size

    def update_account_balance(self, pnl):
        """
        Updates the account balance based on profit and loss (PnL).
        
        :param pnl: Profit or loss from the trade.
        """
        self.account_balance += pnl
        self.update_drawdown()

    def update_drawdown(self):
        """
        Updates the current drawdown based on the account balance.
        """
        peak_balance = max(self.initial_balance, self.account_balance)
        self.current_drawdown = (peak_balance - self.account_balance) / peak_balance

    def check_drawdown_limit(self):
        """
        Checks if the drawdown exceeds the maximum allowed limit.
        
        :return: True if drawdown exceeds the limit, False otherwise.
        """
        return self.current_drawdown > self.max_drawdown

    def can_place_trade(self):
        """
        Determines if a new trade can be placed based on risk parameters.
        
        :return: True if a trade can be placed, False otherwise.
        """
        return not self.check_drawdown_limit()
