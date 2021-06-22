import numpy as np
import matplotlib.pyplot as plt


def show_duration_chart(results: list, title: str) -> None:
    start, stop = np.array(results).T
    plt.barh(range(len(start)), stop - start)
    plt.grid(axis='x')
    plt.ylabel("Tasks")
    plt.xlabel("Seconds")
    plt.xlim(0, 35)
    ytks = range(len(results))
    plt.yticks(ytks, ['job {}'.format(exp) for exp in ytks])
    plt.title(title)


def show_real_time_chart(data: list, title: str) -> None:
    for i, exp in enumerate(data):
        plt.scatter(exp, np.ones(len(exp)) * i, alpha=0.8, c='red', edgecolors='none', s=1)

    plt.grid(axis='x')
    plt.ylabel('Tasks')
    ytks = range(len(data))
    plt.yticks(ytks, [f'Job {exp}' for exp in ytks])
    plt.xlabel('Time')
    plt.title(title)
