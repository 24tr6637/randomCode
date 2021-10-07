
import string
import os
import random
import math
import itertools
import json
import time
import multiprocessing
def randomFinder():
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    names= json.loads(open( "Scam/names.json").read())
    pwL=10
    domain=json.loads(open("Scam/domains.json").read())
    for name in names:
        name_extra=' '.join(random.choice(string.digits))
        username = name.lower() + name_extra + random.choice(domain)
        password = ''.join(random.choice(chars) for i in range(pwL))

        print ('sending username %s and password %s' % (username, password))
def known():

#     userid=str(input("username with domain: "))
#     print(userid)
    passwords=json.loads(open("Scam/passwords.json").read())
    for password in passwords:


        print(password)
known()
