def logging_time(original_fn):
    import time
    from functools import wraps
    @wraps(original_fn)
    def wrapper(*args, **kwargs):
        start_time = time.process_time()
        result = original_fn(*args, **kwargs)

        end_time = time.process_time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time - start_time))
        return result
    return wrapper

@logging_time
def fun_1():
    a_list = ['사람', '자전거'] # => dictionary
    dict_comp = { k : v for k, v in zip(a_list,[ len(att) for att in a_list ])}
    print(dict_comp)

fun_1()
@logging_time
def fun_2():
    a_list = ['사람', '자전거']
    dict = {i: len(i) for i in a_list}
    print(dict)

fun_2()