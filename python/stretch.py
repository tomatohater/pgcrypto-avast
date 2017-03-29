""" Create key stretched md5 hash of a password """

import hashlib, sys

password, iterations = sys.argv[1], int(sys.argv[2])

hashed = password
for _ in range(iterations):
    hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest()

print(hashed)
