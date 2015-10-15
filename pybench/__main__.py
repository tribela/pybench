import argparse
from pybench import benchmark


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('host',
                        help='Controller address')
arg_parser.add_argument('port', default=6633, type=int,
                        help='Controller port')
arg_parser.add_argument('-n', '--switch-num', type=int, default=1,
                        help='Number of switches')
arg_parser.add_argument('-t', '--duration', type=int, default=10,
                        help='Test duration')
arg_parser.add_argument('-d', '--dstip', nargs=2,
                        help='Destination ip addresses in CIDR format')
arg_parser.add_argument('-r', '--ratio', type=int, default=50,
                        help='dst1:all ratio in percentage')


def main():
    args = arg_parser.parse_args()
    benchmark(args.host, args.port,
              args.switch_num, args.duration,
              args.dstip[0], args.dstip[1], args.ratio)


if __name__ == '__main__':
    main()
