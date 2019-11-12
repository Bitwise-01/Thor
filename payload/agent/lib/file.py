# Date: 11/03/2019
# Author: Mohamed
# Description: File manager

from lib.crypto import CryptoRSA, CryptoAES


class File(object):

    chunk_size = (64 << 10) - 1

    @classmethod
    def read(cls, file):
        with open(file, 'rb') as f:
            while True:
                data = f.read(cls.chunk_size)
                if data:
                    yield data
                else:
                    break

    @classmethod
    def write(cls, file, RSA_private_key):
        AES_key = b''
        key_size = 256
        key_read = False

        with open(file, 'rb') as f:
            while True:
                data = f.read(cls.chunk_size)

                if not data:
                    break

                if not key_read:
                    key_read = True
                    AES_key = CryptoRSA.decrypt(
                        data[:key_size], RSA_private_key)

                    yield CryptoAES.decrypt(data[key_size:], AES_key)
                else:
                    yield CryptoAES.decrypt(data, AES_key)
