import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
    def calc_time():
        start_time = time.time()
        func()
        end_time = time.time()
        time_duration = end_time - start_time
        print(f'{func.__name__} run speed: {round(time_duration,2)}s')
    return calc_time

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()