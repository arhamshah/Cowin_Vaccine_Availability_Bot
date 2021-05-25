import requests

from constants import chat_id, base_url


def initiate_send_message():
    '''
    This is closure implementation of Sending Message to a Particular Telegram Channel
    :return: request_send_message()
    '''
    chat_id
    base_url

    def request_send_message(msg):
        '''
        This Function makes a request to Telegram API to send a message in a particular chat
        :param msg: Message to send (String)
        :return: None
        '''
        requests.get(base_url + chat_id + "&text=" + msg)

    return request_send_message
