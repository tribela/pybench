import random

def make_random_mac():
    fields = map(lambda x: '{:02x}'.format(x),
                 (random.randrange(1 << 8) for _ in range(6)))

    return ':'.join(fields)

def make_random_ip():
    fields = map(lambda x: str(x),
                (random.randrange(1 << 8) for _ in range(4)))

    return '.'.join(fields)
