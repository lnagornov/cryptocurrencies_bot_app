from bot import *



def main() -> None :
    """Main entry point. Runs the app"""
    print('I\'am alive')

    bot: CryptocurrencyBot = CryptocurrencyBot(
        token='1396495701:AAFGlWKD6_lk8iMdORqjwhOixbIuxVSabHw', 
        telegram_api_url='https://api.telegram.org/bot'
    )

    print(bot.send_message(chat_id=
        bot.get_message()['chat_id'])
    )


if __name__ == '__main__':
    main()