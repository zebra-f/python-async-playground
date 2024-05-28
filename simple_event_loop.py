from time import time

def put_to_sleep(duration):
    start_time = time()
    while time() - start_time < duration:
        yield

def task1():
    i = 0
    while True:
        yield from put_to_sleep(2)
        print(f'1.{i}: finished')
        i += 1

def task2():
    i = 0
    while True:
        yield from put_to_sleep(3)
        print(f'2.{i}: finished')
        i += 1

def simple_event_loop():
    iterator1 = task1()
    iterator2 = task2()
    while True:
        for task in [iterator1, iterator2]:
            next(task)


# def task1():
#     i = 0
#     start_time = time()
#     while True:
#         if time() - start_time < 2:
#             yield i
#             continue
#         start_time = time()
#         print(f'1.{i}: finished')
#         i += 1
# 
# def task2():
#     i = 0
#     start_time = time()
#     while True:
#         if time() - start_time < 3:
#             yield i
#             continue
#         start_time = time()
#         print(f'2.{i}: finished')
#         i += 1
