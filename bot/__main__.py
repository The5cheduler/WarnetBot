import asyncio
from bot.bot import WarnetBot

def main():
    bot = WarnetBot()
    try:
        asyncio.run(bot.start(debug=False))
    except KeyboardInterrupt:
        print("Logging Out...")

if __name__ == "__main__":
    main()