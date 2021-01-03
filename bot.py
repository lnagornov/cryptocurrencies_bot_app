from abc import ABCMeta, abstractmethod
import requests


class TelegramBot(metaclass=ABCMeta):
    ''' 
    For making and recieving requests every bot must has a token and actual api url.
    '''
    def __init__(self, token: str, telegram_api_url: str) -> None:
        self.__token: str = token
        self.__telegram_api_url: str = telegram_api_url
        self._bot_url: str = self.__telegram_api_url + self.__token


    @abstractmethod
    def get_updates(self) -> None:
        #to be able get states of connection with user like chat_id, user_data, messages and etc.
        pass

    
    @abstractmethod
    def get_message(self) -> None:
        #get user message to habdle
        pass


    @abstractmethod
    def send_message(self) -> None:
        #send message to user
        pass


class CryptocurrencyBot(TelegramBot):

    def __init__(self, token: str, telegram_api_url: str) -> None:
        super().__init__(token, telegram_api_url)


    def get_updates(self) -> dict:
        '''
        Sends GET request to telegram bot api. 
        Transforms response of states in JSON into dict.
        :return: dict 
        '''
        
        method_config: str = 'getupdates' 
        method_url: str = '/'.join([self._bot_url, method_config])
        response: requests.Response = requests.get(method_url)
        
        return response.json()


    def get_message(self) -> dict:
        '''
        Get the last message that have been sent to the bot.
        :return: dict 'chat_id' and 'text'
        '''
        data: dict = self.get_updates()
        chat_id: int = data['result'][-1]['message']['chat']['id']
        text: str = data['result'][-1]['message']['text']
        message: dict = {
            'chat_id': chat_id,
            'text': text
        }

        return message


    def send_message(self, chat_id: int, message: str='I\'m alive!!!') -> None:
        '''
        To send a message to user you need to provide 'chat_id' and 'message'
        :return: None
        '''

        method_config: str = 'sendmessage?chat_id={}&text={}'.format(
            chat_id, message
        ) 
        method_url: str = '/'.join([self._bot_url, method_config])
        requests.get(method_url)
