import matplotlib.pyplot as plt

from processing_examples.pool_processing import pool_processing
from threading_examples.pool_threading import pool_threading
from threading_examples.simple_threading import simple_threading
from processing_examples.simple_processing import simple_processing
from utils.function_selection import function_selection
from utils.parser_config import parser_config
from utils.visuals import show_duration_chart, show_real_time_chart

WAYS_OF_CONCURRENCY_MAPPING = {
    'simple': {
        'threading': simple_threading,
        'processing': simple_processing
    },
    'pool': {
        'threading': pool_threading,
        'processing': pool_processing
    }
}


def main() -> None:
    args = parser_config()

    ways = WAYS_OF_CONCURRENCY_MAPPING[args.level]
    function_to_be_triggered = function_selection(args)

    if args.visuals:
        if args.real_time:
            show_real_time_chart(
                ways[args.way](function_to_be_triggered, length=args.length if hasattr(args, 'length') else 10),
                args.way
            )
        else:
            show_duration_chart(
                ways[args.way](function_to_be_triggered, length=args.length if hasattr(args, 'length') else 10),
                args.way
            )
        plt.show()
    else:
        ways[args.way](function_to_be_triggered, length=args.length if hasattr(args, 'length') else 10)


if __name__ == '__main__':
    main()
