import datetime


def rat_fun(arg1: int = 0, arg2: int = 0):
    return print(f"rat {arg1} {arg2}")


documents = []
use_in = 2


def people_by_number():
    doc_flag = 0
    for document in documents:
        if use_in in document.values():
            print(f'{document["name"]}')
            print('----------------------------------------')
            print('commands: p for people, s for shelf, l for list, a for add, q for quit')
            doc_flag = 1
    if doc_flag == 0:
        print('document not found')
        print('----------------------------------------')
        print('commands: p for people, s for shelf, l for list, a for add, q for quit')


def decor1(fun, log_path):

    lp = log_path

    def new_fun(*args, **kwargs):
        res = fun()
        a = f"function {fun.__name__} "
        b = f"at {str(datetime.datetime.now())} "
        c = f"with args {str(args)}, and kwargs {str(kwargs)}\n"

        with open(lp, 'a', encoding='utf=8') as f:
            f.write(a)
            f.write(b)
            f.write(c)

        return res
    return new_fun


def decor2(log_path):
    def dec(fun):
        def new_fun(*args, **kwargs):
            lp = log_path
            res = dec(*args, **kwargs)
            a = f"function {fun.__name__} "
            b = f"at {str(datetime.datetime.now())} "
            c = f"with args {str(args)}, and kwargs {str(kwargs)}\n"

            with open(lp, 'a', encoding='utf=8') as f:
                f.write(a)
                f.write(b)
                f.write(c)

            return res
        return new_fun
    return dec


rat = decor1(rat_fun, 'log.txt')


@decor2('log.txt')
def rat2():
    rat_fun()


rat()

docs = decor1(people_by_number, 'log.txt')


docs()
