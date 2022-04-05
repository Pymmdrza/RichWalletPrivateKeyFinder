from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL
from hexer import mHash
from colorama import Fore,Style

mmdrza = '''
             ||=======================================================================||
             ||- ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗ -||-                                   -||
             ||- ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║ -||-                                   -||
             ||- ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩ -||-    @@@@@@@@ @@@@@@@ @@@  @@@      -||
             ||--------------------------------||-    @@!        @@!   @@!  @@@      -||
             ||-| WebSite : Mmdrza.Com        -||-    @!!!:!     @!!   @!@!@!@!      -||
             ||-| Mail : X4@Mmdrza.Com        -||-    !!:        !!:   !!:  !!!      -||               
             ||-| DEV.to/Mmdrza               -||-    : :: :::    :     :   : :      -||
             ||-| Github.Com/PyMmdrza         -||-  PrivateKey Rich Wallet Cracker   -||
             ||-| PythonWithMmdrza.Medium.Com -||-                                   -||
             ||-----------------------------------------------------------------------||
             ||-|  Donate BTC Address Wallet  => 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8  -||
             ||=======================================================================||
-----------------------------------------------------------------------------------------------------------------             
'''


filename = input('FileName ====================>>====>> ')
with open(filename) as f:
    add = f.read().split()
add = set(add)
print('\n\n\n\n\n\n\n\n\n\n\n\n', Fore.RED, str(mmdrza), Style.RESET_ALL, '\n')
z = 1
while True:
    hex64 = mHash()
    PRIVATE_KEY: str = hex64
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    priv = hdwallet.private_key()
    addr = hdwallet.p2pkh_address()
    print(Fore.WHITE, str(z), Fore.YELLOW, 'Total Scan Checking ----- ETH Address =', Fore.GREEN, str(addr), end='\r')
    z += 1
    if addr in add:
        f = open("EthereumRichWinnerWallet.txt","a")
        f.write('\nAddress = ' + str(addr))
        f.write('\nPrivate Key = ' + str(priv))
        f.write('\n=========================================================\n')
        f.close()
        print('Winner information Saved On text file')
        continue

