import random


def make_random_mac():
    fields = map(lambda x: '{:02x}'.format(x),
                 (random.randrange(1 << 8) for _ in range(6)))

    return ':'.join(fields)


def ip_to_num(ip):
    fields = map(int, ip.split('.', 3))
    num = 0
    for field in fields:
        num <<= 8
        num += field

    return num


def num_to_ip(num):
    fields = []
    for _ in range(4):
        field = num & 0xff
        fields.insert(0, field)
        num >>= 8

    return '{}.{}.{}.{}'.format(*fields)


def make_random_ip(cidr):
    addr, netmask = cidr.split('/', 1)
    addr = ip_to_num(addr)
    netmask = int(netmask)

    network_addr = addr & (0xffffffff << (32 - netmask))
    host_addr = random.randrange(1 << (32 - netmask))

    return num_to_ip(network_addr + host_addr)
