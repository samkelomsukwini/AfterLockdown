import random
import string

def secret_key(size=355, chars=string.ascii_letters + string.digits):
    '''
    Generates and returns 355 character base64 secret key
    '''
    return ''.join(random.choice(chars) for _ in range(size))