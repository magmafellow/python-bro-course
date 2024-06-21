# thread = a flow of execution. Like a separate order of instructions.
#          However each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock),
#          allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of its time waiting for external events (user input, web scraping)
#            use multithreading


import threading
import time


# These are io bound tasks
def eat_breakfast():
    time.sleep(3)
    print('You eat breakfast')


def drink_coffee():
    time.sleep(4)
    print('You drink coffee')


def study():
    time.sleep(5)
    print('You finish studying')


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

u = threading.Thread(target=study)
u.start()

# x.join()  # Main Thread is going to wait for x job before it can move on
# y.join()
# u.join()

# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
