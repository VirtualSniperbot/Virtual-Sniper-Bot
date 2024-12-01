# Pro sniping strategy implementation
def pro_strategy(data):
    return sorted(data, key=lambda x: x['profit_margin'], reverse=True)
