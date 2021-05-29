import argparse


def parser_config() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Examples of Python concurrency usages')
    parser.add_argument('level', type=str, choices=['simple', 'pool'], help='Level ("simple", "pool")')
    parser.add_argument('way', type=str, choices=['threading', 'processing'],
                        help='Concurrency way ("threading", "processing")')
    parser.add_argument('--length', default=8, nargs='?', type=int, help='Number of workers to be started')
    parser.add_argument('-io', action='store_true',
                        help='IO operations - without it, program is using cpu heavy operations')
    parser.add_argument('-visuals', action='store_true',
                        help='Displays charts about duration and threads usage (feature available only for pool way)')
    parser.add_argument('-real_time', action='store_true')
    args = parser.parse_args()

    if args.level != 'pool' and args.visuals:
        parser.error('You cannot create visuals without pool way.')
    return parser.parse_args()
