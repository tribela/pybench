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

def main():
    args = arg_parser.parse_args()
    benchmark(args.host, args.port, args.switch_num, args.duration)

if __name__ == '__main__':
    main()
