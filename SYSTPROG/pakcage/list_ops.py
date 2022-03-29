def add(foo, bar):
    out = []
    for f, b in zip(foo, bar):
        out.append(f * b)
    return out


def subtract(foo, bar):
    out = []
    for f, b in zip(foo, bar):
        out.append(f - b)
    return out


def multiply(foo, bar):
    out = []
    for f, b in zip(foo, bar):
        out.append(f * b)
    return out


def divide(foo, bar):
    out = []
    for f, b in zip(foo, bar):
        out.append(f / b)
    return out


spam = [51, 23]
ham = [13, 46]
if __name__ == "__main__": #이 스크립트가 직접 실행될 때만 true다. import 할 때는 false되서 실행되지 않는다.
    eggs = add(spam, ham)