import random

from netaddr import IPNetwork


def make_random_mac():
    fields = map(lambda x: '{:02x}'.format(x),
                 (random.randrange(1 << 8) for _ in range(6)))

    return ':'.join(fields)


def make_random_ip(cidr):
    network = IPNetwork(cidr)
    return str(random.choice(network))
