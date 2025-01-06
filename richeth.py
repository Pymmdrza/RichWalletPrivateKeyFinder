from cryptofuzz import Ethereum
from hexer import mHash
from colorama import Fore,Style

mmdrza = '''
             ||=======================================================================||
             ||- ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗ -||-                                   -||
             ||- ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║ -||-                                   -||
             ||- ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩ -||-    @@@@@@@@ @@@@@@@ @@@  @@@      -||
             ||--------------------------------||-    @@!        @@!   @@!  @@@      -||
             ||-| WebSite : Mmdrza.Com        -||-    @!!!:!     @!!   @!@!@!@!      -||
             ||--------------------------------||-    !!:        !!:   !!:  !!!      -||               
             ||-| Github.Com/PyMmdrza         -||-    : :: :::    :     :   : :      -||
             ||-| Mdrza.Medium.Com            -||-  PrivateKey Rich Wallet Cracker   -||
             ||-----------------------------------------------------------------------||
             ||-|  Donate BTC Address Wallet  => 1MMDRZAcM6dzmdMUSV8pDdAPDFpwzve9Fc  -||
             ||=======================================================================||
-----------------------------------------------------------------------------------------------------------------             
'''


filename = input('FileName >> ')
with open(filename) as f:
    add = f.read().split()
add = set(add)
print('\n\n\n\n\n\n\n\n\n\n\n\n', Fore.RED, str(mmdrza), Style.RESET_ALL, '\n')
z = 1
eth = Ethereum()
while True:
    hex64 = mHash()
    priv = hex64
    addr = eth.hex_addr(priv)
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

