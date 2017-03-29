""" Create a salted md5 hash of a password """

import hashlib, sys

password, salt = sys.argv[1], sys.argv[2]

encrypted = hashlib.md5((password + salt).encode('utf-8')).hexdigest()

print(encrypted)
