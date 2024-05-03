import datetime


def logger(path):

    def __logger(old_function):

        def new_function(*args, **kwargs):
            start = datetime.datetime.now()
            result = old_function(*args, **kwargs)

            with open(path, 'a') as file:
                file.write(f'Start: {start}\n'
                           f'Function: {old_function.__name__} \n'
                           f'Args and kwargs: {args}, {kwargs}\n'
                           f'Return value: {result}\n\n')
            return result

        return new_function

    return __logger


def gen_lists(some_list):
    for el in some_list:
        if type(el) == list:
            yield from gen_lists(el)
        else:
            yield el


@logger(path='log_my_func.log')
def flat_generator(list_of_lists):

    for list_ in list_of_lists:
        list_ = [('None' if x is None else x) for x in list_]
        for element in list_:
            if type(element) == list:
                element = gen_lists(element)
                yield from element
            elif element == 'None':
                yield None
            else:
                yield element


if __name__ == '__main__':
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    flat_generator(list_of_lists_2)
