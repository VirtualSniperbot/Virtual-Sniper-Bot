from sniper_bot import VirtualsSniperBot

def test_should_snipe():
    bot = VirtualsSniperBot(api_key="dummy")
    assert bot.should_snipe({'profit_margin': 0.2}) == True
    assert bot.should_snipe({'profit_margin': 0.05}) == False
