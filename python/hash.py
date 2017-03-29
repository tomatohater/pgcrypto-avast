""" Create md5 hash of a password """

import hashlib, sys

password = sys.argv[1]
hashed = hashlib.md5(password.encode('utf-8')).hexdigest()

print(hashed)
