from sniper_bot import VirtualsSniperBot
from config import API_KEY

def main():
    print("Starting Virtuals Sniper Bot...")
    bot = VirtualsSniperBot(api_key=API_KEY)
    bot.run()

if __name__ == "__main__":
    main()
