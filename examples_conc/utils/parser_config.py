import argparse


def parser_config() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Examples of Python concurrency usages')
    parser.add_argument('level', type=str, choices=['simple', 'pool', 'asyncio'],
                        help='Level ("simple", "pool", "asyncio")')
    parser.add_argument('way', type=str, choices=['threading', 'processing', 'asyncio'],
                        help='Concurrency way ("threading", "processing", "asyncio")')
    parser.add_argument('--length', default=10, nargs='?', type=int, help='Number of workers to be started')
    parser.add_argument('-io', action='store_true',
                        help='IO operations - without it, program is using cpu heavy operations')
    parser.add_argument('-visuals', action='store_true',
                        help='Displays charts about duration and threads usage (feature available only for pool way)')
    parser.add_argument('-real_time', action='store_true')
    args = parser.parse_args()

    if args.level != 'pool' and args.visuals and not args.way == 'asyncio':
        parser.error('You cannot create visuals without pool way or for asyncio.')
    return parser.parse_args()
