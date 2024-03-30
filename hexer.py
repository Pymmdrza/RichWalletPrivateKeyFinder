#
from random import choice as c


def mHash():
    """ Generated random hash without repetition (default size: 64) """
    return ''.join(c('0123456789abcdef') for _ in range(64))


def mhex128():
    """ Generated random hash without repetition (default size: 128). """
    return ''.join(c('0123456789abcdef') for _ in range(128))


# //=====================================================
# // DONATE (BTC) : 1MMDRZAcM6dzmdMUSV8pDdAPDFpwzve9Fc
# // Website : Mmdrza.Com
# // Email : mmdrza@usa.com
# // Github.com/Pymmdrza
# //=====================================================
