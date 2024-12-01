# Basic sniping strategy implementation
def basic_strategy(data):
    return [item for item in data if item['profit_margin'] > 0.1]
