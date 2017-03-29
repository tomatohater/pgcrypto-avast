""" Generate a rainbow table of md5 hashes for given length passwords """

import hashlib, itertools, string, sys

length = int(sys.argv[1])

# All 14,776,336 4 character passwords (alphanumeric only!)
char_set = string.ascii_letters + string.digits
all_passwords = map(''.join, itertools.product(char_set, repeat=length))

for password in all_passwords:
    print(hashlib.md5(password.encode('utf-8')).hexdigest(), password)
