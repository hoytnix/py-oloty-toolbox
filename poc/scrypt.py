import pyscrypt, time

if __name__ == '__main__':
    tests = [
        (b'', b'', 16, 1, 1, 64),
        (b'password', b'NaCl', 1024, 8, 16, 64),
        (b'pleaseletmein', b'SodiumChloride', 16384, 8, 1, 64),
        (b'pleaseletmein', b'SodiumChloride', 1048576, 8, 1, 64)
    ]

    for test in tests:
        start = time.time()
        hashed = pyscrypt.hash(password = test[0], 
            salt = test[1], 
            N = test[2],
            r = test[3],
            p = test[4],
            dkLen = test[5])
        print(time.time() - start, test)