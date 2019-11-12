# Date: 11/02/2019
# Author: Mohamed
# Description: A simple file finder


import os
import time
import queue
import lib.const as const
from random import randint
from getpass import getuser
from threading import Thread


class FileFinder:

    root_dir = os.path.join(
        os.path.abspath(os.path.sep), 'Users', getuser(
        ), 'Desktop', 'Target_Folder'
    )

    ### Do not uncomment the code below, or there might be dire consequences ###

    #### Uncomment code below at your own risk ####
    # root_dir = os.path.join(
    #     os.path.abspath(os.path.sep), 'Users', getuser(),
    # )

    filetypes = const.filetypes
    exclude = const.exclude

    def __init__(self):
        self.is_active = True
        self.targets = queue.Queue()

    def start(self):

        for root, dirs, files in os.walk(self.root_dir, topdown=True):

            dirs[:] = [
                d for d in dirs if d not in self.exclude
                and d.lower() not in self.exclude
                and not d.startswith('.')
                and not d.startswith('__')
            ]

            for file in files:

                path = os.path.join(root, file)

                if os.path.splitext(path)[-1].lower() in self.filetypes:
                    self.targets.put(path)

        self.is_active = False
