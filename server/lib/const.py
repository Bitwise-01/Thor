import os

KEY_DIR = 'server/keys/'
RSA_PUBLIC_KEY = os.path.join(KEY_DIR, 'public.pem')
RSA_PRIVATE_KEY = os.path.join(KEY_DIR, 'private.key')


if not os.path.exists(KEY_DIR):
    os.mkdir(KEY_DIR)
