# **************************************
# Multiprocessing
# **************************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)


from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    a = Process(target=counter, args=(25_000_000,))
    b = Process(target=counter, args=(25_000_000,))
    c = Process(target=counter, args=(25_000_000,))
    d = Process(target=counter, args=(25_000_000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print('You have {} amount of cpu cores'.format(cpu_count()))

    print('finished in: {} seconds'.format(time.perf_counter() / 1000))


if __name__ == '__main__':
    main()
