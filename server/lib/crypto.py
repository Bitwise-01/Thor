# Date: 11/03/2019
# Author: Mohamed
# Description: Encryption & Decryption

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

import server.lib.const as const 


class CryptoRSA:

    @staticmethod
    def gen_keys():
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return public_key, private_key

    @staticmethod
    def encrypt(data, rec_publ_key):
        recipient_key = RSA.import_key(rec_publ_key)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        return cipher_rsa.encrypt(data)

    @staticmethod
    def decrypt(data, priv_key):
        key = RSA.import_key(priv_key)
        cipher_rsa = PKCS1_OAEP.new(key)
        return cipher_rsa.decrypt(data)

    @staticmethod
    def sign(data, priv_key):
        key = RSA.import_key(priv_key)
        _hash = SHA256.new(data)
        return pkcs1_15.new(key).sign(_hash)

    @staticmethod
    def verify(data, signature, publ_key):
        key = RSA.import_key(publ_key)
        _hash = SHA256.new(data)

        try:
            pkcs1_15.new(key).verify(_hash, signature)
            return True
        except ValueError:
            return False

    @staticmethod
    def save(publ, priv):
        for fname, key in zip([const.RSA_PUBLIC_KEY, const.RSA_PRIVATE_KEY], [publ, priv]):
            with open(fname, 'wb') as f:
                f.write(key)

    @staticmethod
    def read(publ_file, priv_file):
        publ = b''
        priv = b''

        with open('public.pem', 'rb') as f:
            for n in f:
                publ += n

        with open('private.key', 'rb') as f:
            for n in f:
                priv += n

        return publ, priv


class CryptoAES:

    nonce_size = 12

    @staticmethod
    def generate_key():
        return get_random_bytes(AES.block_size)

    @staticmethod
    def encrypt(data, key):
        key = SHA256.new(key).digest()
        nonce = get_random_bytes(CryptoAES.nonce_size)

        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        ciphertext = cipher.encrypt(data)
        return nonce + ciphertext

    @staticmethod
    def decrypt(ciphertext, key):
        cipher_nonce = ciphertext
        key = SHA256.new(key).digest()

        nonce = cipher_nonce[:CryptoAES.nonce_size]
        ciphertext = cipher_nonce[CryptoAES.nonce_size:]

        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext
