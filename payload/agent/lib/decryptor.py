# Date: 11/03/2019
# Author: Mohamed
# Description: Locate and decrypt files

import os
import time
import lib.const as const
from lib.file import File
from threading import Thread, RLock
from lib.file_finder import FileFinder
from lib.crypto import CryptoRSA, CryptoAES


class Decryptor:

    def __init__(self, RSA_private_key):
        self.active_threads = 0
        self.max_active_threads = 256
        self.file_finder = FileFinder()
        self.active_threads_lock = RLock()
        self.RSA_private_key = RSA_private_key

    def _decrypt_file(self, file):

        new_file_path = os.path.splitext(file)[0]

        try:
            with open(new_file_path, 'wb') as f:
                for data in File.write(file, self.RSA_private_key):
                    f.write(data)

            # delete the encrypted file
            os.remove(file)
        except:
            pass
        finally:
            with self.active_threads_lock:
                self.active_threads -= 1

    def _decrypt_files(self):

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

                with self.active_threads_lock:
                    self.active_threads += 1

                Thread(target=self._decrypt_file, args=[
                       file], daemon=True).start()

    def start(self):
        self.file_finder.filetypes = [const.encrypted_extension]

        # start file search
        Thread(target=self.file_finder.start, daemon=True).start()
        time.sleep(1)

        self._decrypt_files()
