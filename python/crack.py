""" Cracks md5 hash of a 4 character alphanumeric password """

import hashlib, itertools, string, sys, time

hashed = sys.argv[1]

# All 14,776,336 4 character passwords (alphanumeric only!)
char_set = string.ascii_letters + string.digits
all_passwords = map(''.join, itertools.product(char_set, repeat=4))

start = time.time()
for attempt in all_passwords:
    if hashed == hashlib.md5(attempt.encode('utf-8')).hexdigest():
        elapsed = (time.time()-start)
        print('Cracked in', elapsed, 'seconds. Password is:', attempt)
        break
else:
    elapsed = (time.time()-start)
    print('Can\'t crack password.', elapsed, 'seconds elapsed.')
